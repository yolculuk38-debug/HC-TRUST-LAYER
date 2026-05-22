from verification_timeline import (
    build_timeline_event,
    build_verification_timeline,
    evaluate_verification_timeline,
)



def test_complete_verification_timeline():
    timeline = build_verification_timeline(
        record_id="REC-1",
        events=[
            build_timeline_event(
                event_type="FIRST_SEEN",
                timestamp="2026-05-22T07:00:00Z",
            ),
            build_timeline_event(
                event_type="VERIFICATION",
                timestamp="2026-05-22T07:05:00Z",
            ),
        ],
    )

    result = evaluate_verification_timeline(timeline)

    assert result["trusted"] is True



def test_incomplete_verification_timeline():
    timeline = build_verification_timeline(
        record_id="REC-2",
        events=[
            build_timeline_event(
                event_type="FIRST_SEEN",
                timestamp="2026-05-22T07:00:00Z",
            ),
        ],
    )

    result = evaluate_verification_timeline(timeline)

    assert result["trusted"] is False
