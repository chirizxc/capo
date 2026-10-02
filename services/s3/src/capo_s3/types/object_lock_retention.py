"""Generated from Smithy shape ``com.amazonaws.s3#ObjectLockRetention``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.date
    import capo_s3.types.event_hold_duration
    import capo_s3.types.object_lock_event_hold
    import capo_s3.types.object_lock_retention_mode


class ObjectLockRetention(TypedDict, closed=True):
    mode: NotRequired[
        "capo_s3.types.object_lock_retention_mode.ObjectLockRetentionMode"
    ]
    """<p>Indicates the Retention mode for the specified object.</p>"""
    retain_until_date: NotRequired["capo_s3.types.date.Date"]
    """<p>The date on which this Object Lock Retention will expire.</p>"""
    event_hold: NotRequired["capo_s3.types.object_lock_event_hold.ObjectLockEventHold"]
    """<p>The event hold status for the object. Set to <code>ON</code> to enable an event hold or <code>OFF</code> to disable it.</p>"""
    event_hold_duration: NotRequired[
        "capo_s3.types.event_hold_duration.EventHoldDuration"
    ]
    """<p>The event hold duration for the object. Specifies how long the object remains protected after the event hold is released.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectLockRetention, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "mode" in value:
        import capo_s3.types.object_lock_retention_mode

        capo_s3.types.object_lock_retention_mode.serialize_xml(
            value["mode"], el, "Mode"
        )
    if "retain_until_date" in value:
        import capo_s3.types.date

        capo_s3.types.date.serialize_xml(
            value["retain_until_date"], el, "RetainUntilDate"
        )
    if "event_hold" in value:
        import capo_s3.types.object_lock_event_hold

        capo_s3.types.object_lock_event_hold.serialize_xml(
            value["event_hold"], el, "EventHold"
        )
    if "event_hold_duration" in value:
        import capo_s3.types.event_hold_duration

        capo_s3.types.event_hold_duration.serialize_xml(
            value["event_hold_duration"], el, "EventHoldDuration"
        )


def deserialize_xml(el: Element) -> ObjectLockRetention:
    out: ObjectLockRetention = {}  # type: ignore[typeddict-item]
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_s3.types.object_lock_retention_mode

        out["mode"] = capo_s3.types.object_lock_retention_mode.deserialize_xml(
            child_mode
        )
    child_retain_until_date = el.find("RetainUntilDate")
    if child_retain_until_date is not None:
        import capo_s3.types.date

        out["retain_until_date"] = capo_s3.types.date.deserialize_xml(
            child_retain_until_date
        )
    child_event_hold = el.find("EventHold")
    if child_event_hold is not None:
        import capo_s3.types.object_lock_event_hold

        out["event_hold"] = capo_s3.types.object_lock_event_hold.deserialize_xml(
            child_event_hold
        )
    child_event_hold_duration = el.find("EventHoldDuration")
    if child_event_hold_duration is not None:
        import capo_s3.types.event_hold_duration

        out["event_hold_duration"] = capo_s3.types.event_hold_duration.deserialize_xml(
            child_event_hold_duration
        )
    return out
