"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.max24_hour_send
    import capo_pinpoint_email.types.max_send_rate
    import capo_pinpoint_email.types.sent_last24_hours


class SendQuota(TypedDict, closed=True):
    max24_hour_send: "capo_pinpoint_email.types.max24_hour_send.Max24HourSend"
    """<p>The maximum number of emails that you can send in the current AWS Region over a 24-hour period. This value is also called your <i>sending quota</i>.</p>"""
    max_send_rate: "capo_pinpoint_email.types.max_send_rate.MaxSendRate"
    """<p>The maximum number of emails that you can send per second in the current AWS Region. This value is also called your <i>maximum sending rate</i> or your <i>maximum TPS (transactions per second) rate</i>.</p>"""
    sent_last24_hours: "capo_pinpoint_email.types.sent_last24_hours.SentLast24Hours"
    """<p>The number of emails sent from your Amazon Pinpoint account in the current AWS Region over the past 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendQuota) -> dict:
    out: dict = {}
    out["Max24HourSend"] = (
        "NaN"
        if value.get("max24_hour_send", 0) != value.get("max24_hour_send", 0)
        else "Infinity"
        if value.get("max24_hour_send", 0) == float("inf")
        else "-Infinity"
        if value.get("max24_hour_send", 0) == float("-inf")
        else value.get("max24_hour_send", 0)
    )
    out["MaxSendRate"] = (
        "NaN"
        if value.get("max_send_rate", 0) != value.get("max_send_rate", 0)
        else "Infinity"
        if value.get("max_send_rate", 0) == float("inf")
        else "-Infinity"
        if value.get("max_send_rate", 0) == float("-inf")
        else value.get("max_send_rate", 0)
    )
    out["SentLast24Hours"] = (
        "NaN"
        if value.get("sent_last24_hours", 0) != value.get("sent_last24_hours", 0)
        else "Infinity"
        if value.get("sent_last24_hours", 0) == float("inf")
        else "-Infinity"
        if value.get("sent_last24_hours", 0) == float("-inf")
        else value.get("sent_last24_hours", 0)
    )
    return out


def deserialize_json(data: dict) -> SendQuota:
    out: SendQuota = {}  # type: ignore[typeddict-item]
    if data.get("Max24HourSend") is not None:
        out["max24_hour_send"] = float(data["Max24HourSend"])
    else:
        out["max24_hour_send"] = 0
    if data.get("MaxSendRate") is not None:
        out["max_send_rate"] = float(data["MaxSendRate"])
    else:
        out["max_send_rate"] = 0
    if data.get("SentLast24Hours") is not None:
        out["sent_last24_hours"] = float(data["SentLast24Hours"])
    else:
        out["sent_last24_hours"] = 0
    return out
