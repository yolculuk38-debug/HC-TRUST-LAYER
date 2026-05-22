from verification_cli import verify_package_file



def test_verification_cli_exports():
    assert callable(verify_package_file)
