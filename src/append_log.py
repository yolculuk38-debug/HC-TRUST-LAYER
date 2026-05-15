#!/usr/bin/env python3
"""
Immutable-style Append-Only Changelog Script

Creates or appends to immutable revision history logs for records.
Each record gets a log file (records/logs/<record_id>.log.json) that
tracks all changes in an append-only manner.

Usage:
  python src/append_log.py

Exit codes:
  0 - Success
  1 - Error during processing
"""

import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime


def calculate_content_hash(content):
    """
    Calculate SHA-256 hash of content.
    
    Args:
        content: String or dict content to hash
        
    Returns:
        Hex string of SHA-256 hash (lowercase, 64 chars)
    """
    if isinstance(content, str):
        content_bytes = content.encode('utf-8')
    else:
        content_bytes = json.dumps(content, separators=(',', ':')).encode('utf-8')
    
    return hashlib.sha256(content_bytes).hexdigest()


def get_record_hash(record):
    """
    Calculate hash of record data (excluding prev_hash and hash fields).
    
    Args:
        record: Record dict
        
    Returns:
        SHA-256 hash hex string
    """
    # Create a hashable version of the record without hash fields
    record_copy = {k: v for k, v in record.items() if k not in ['hash', 'prev_hash']}
    return calculate_content_hash(record_copy)


def read_log_file(log_path):
    """
    Read existing log file.
    
    Args:
        log_path: Path to log file
        
    Returns:
        List of log entries, or empty list if file doesn't exist
    """
    if not log_path.exists():
        return []
    
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                return []
            # Each line is a JSON entry
            entries = []
            for line in content.split('\n'):
                if line.strip():
                    entries.append(json.loads(line))
            return entries
    except Exception as e:
        print(f"ERROR: Failed to read log {log_path}: {e}", file=sys.stderr)
        return []


def append_log_entry(log_path, entry):
    """
    Append entry to log file in append-only manner (one entry per line).
    
    Args:
        log_path: Path to log file
        entry: Entry dict to append
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # Create parent directory if needed
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Append entry as JSON line
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry, separators=(',', ':')) + '\n')
        
        return True
    except Exception as e:
        print(f"ERROR: Failed to write log {log_path}: {e}", file=sys.stderr)
        return False


def process_record_file(record_path, logs_dir):
    """
    Process a single record file and update its log.
    
    Args:
        record_path: Path to record file
        logs_dir: Directory where logs are stored
        
    Returns:
        Tuple (success: bool, message: str)
    """
    try:
        with open(record_path, 'r', encoding='utf-8') as f:
            record = json.load(f)
    except Exception as e:
        return False, f"Failed to read {record_path}: {e}"
    
    # Extract record_id
    record_id = record.get('record_id') or record.get('id')
    if not record_id:
        return False, f"No record_id found in {record_path}"
    
    # Prepare log entry
    log_entry = {
        'record_id': record_id,
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'content_hash': record.get('content_hash', ''),
        'verification_status': record.get('verification_status', 'unknown'),
        'status': record.get('status', 'unknown'),
        'prev_hash': record.get('prev_hash', ''),
        'hash': record.get('hash', ''),
        'source_file': str(record_path.relative_to(Path.cwd()))
    }
    
    # Check if we need to append
    log_path = logs_dir / f"{record_id}.log.json"
    existing_entries = read_log_file(log_path)
    
    # Only append if content_hash changed or this is a new log
    should_append = False
    
    if not existing_entries:
        should_append = True
        reason = "new log"
    else:
        last_entry = existing_entries[-1]
        if last_entry.get('content_hash') != log_entry['content_hash']:
            should_append = True
            reason = "content_hash changed"
        else:
            reason = "no change (content_hash same)"
    
    if should_append:
        if append_log_entry(log_path, log_entry):
            return True, f"PASS: {record_id} ({reason})"
        else:
            return False, f"Failed to append log for {record_id}"
    else:
        return True, f"INFO: {record_id} - {reason}, skipped"


def find_record_files():
    """
    Find all record files in pending, verified, and archived directories.
    
    Returns:
        Sorted list of Path objects
    """
    records_dir = Path('records')
    record_files = []
    
    for subdir in ['pending', 'verified', 'archive']:
        dir_path = records_dir / subdir
        if dir_path.exists():
            record_files.extend(sorted(dir_path.glob('*.json')))
    
    return sorted(set(record_files))


def main():
    """Main entry point."""
    logs_dir = Path('records/logs')
    
    # Find all record files
    record_files = find_record_files()
    
    if not record_files:
        print("INFO: No record files found")
        return 0
    
    print(f"Processing {len(record_files)} record file(s) for append-only changelog...")
    print()
    
    success_count = 0
    info_count = 0
    failed_count = 0
    
    for record_path in record_files:
        success, message = process_record_file(record_path, logs_dir)
        
        if success:
            if "INFO:" in message:
                info_count += 1
                print(f"ℹ️  {message}")
            else:
                success_count += 1
                print(f"✅ {message}")
        else:
            failed_count += 1
            print(f"❌ {message}")
    
    print()
    print(f"Results: {success_count} appended, {info_count} info, {failed_count} failed")
    
    if failed_count > 0:
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
