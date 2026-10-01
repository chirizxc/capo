"""Generated from Smithy shape ``com.amazonaws.s3control#S3ObjectLockEventHoldDuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_object_lock_event_hold_duration_days
    import capo_s3_control.types.s3_object_lock_event_hold_duration_years


class S3ObjectLockEventHoldDuration(TypedDict, closed=True):
    days: NotRequired[
        "capo_s3_control.types.s3_object_lock_event_hold_duration_days.S3ObjectLockEventHoldDurationDays"
    ]
    """<p>The number of days for the event hold duration. The minimum value is 1 and the maximum value is 36,500.</p>"""
    years: NotRequired[
        "capo_s3_control.types.s3_object_lock_event_hold_duration_years.S3ObjectLockEventHoldDurationYears"
    ]
    """<p>The number of years for the event hold duration. The minimum value is 1 and the maximum value is 100.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3ObjectLockEventHoldDuration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "years" in value:
        SubElement(el, "Years").text = str(value["years"])


def deserialize_xml(el: Element) -> S3ObjectLockEventHoldDuration:
    out: S3ObjectLockEventHoldDuration = {}  # type: ignore[typeddict-item]
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_years = el.find("Years")
    if child_years is not None:
        out["years"] = int(child_years.text or "")
    return out
