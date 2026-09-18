"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainIspPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.isp_name
    import capo_sesv2.types.percentage
    import capo_sesv2.types.volume


class DomainIspPlacement(TypedDict, closed=True):
    isp_name: NotRequired["capo_sesv2.types.isp_name.IspName"]
    """<p>The name of the email provider that the inbox placement data applies to.</p>"""
    inbox_raw_count: NotRequired["capo_sesv2.types.volume.Volume"]
    """<p>The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.</p>"""
    spam_raw_count: NotRequired["capo_sesv2.types.volume.Volume"]
    """<p>The total number of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.</p>"""
    inbox_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' inboxes.</p>"""
    spam_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of messages that were sent from the selected domain to the specified email provider that arrived in recipients' spam or junk mail folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainIspPlacement) -> dict:
    out: dict = {}
    if "isp_name" in value:
        out["IspName"] = value["isp_name"]
    if "inbox_raw_count" in value:
        out["InboxRawCount"] = value["inbox_raw_count"]
    if "spam_raw_count" in value:
        out["SpamRawCount"] = value["spam_raw_count"]
    if "inbox_percentage" in value:
        out["InboxPercentage"] = (
            "NaN"
            if value["inbox_percentage"] != value["inbox_percentage"]
            else "Infinity"
            if value["inbox_percentage"] == float("inf")
            else "-Infinity"
            if value["inbox_percentage"] == float("-inf")
            else value["inbox_percentage"]
        )
    if "spam_percentage" in value:
        out["SpamPercentage"] = (
            "NaN"
            if value["spam_percentage"] != value["spam_percentage"]
            else "Infinity"
            if value["spam_percentage"] == float("inf")
            else "-Infinity"
            if value["spam_percentage"] == float("-inf")
            else value["spam_percentage"]
        )
    return out


def deserialize_json(data: dict) -> DomainIspPlacement:
    out: DomainIspPlacement = {}  # type: ignore[typeddict-item]
    if data.get("IspName") is not None:
        out["isp_name"] = data["IspName"]
    if data.get("InboxRawCount") is not None:
        out["inbox_raw_count"] = data["InboxRawCount"]
    if data.get("SpamRawCount") is not None:
        out["spam_raw_count"] = data["SpamRawCount"]
    if data.get("InboxPercentage") is not None:
        out["inbox_percentage"] = float(data["InboxPercentage"])
    if data.get("SpamPercentage") is not None:
        out["spam_percentage"] = float(data["SpamPercentage"])
    return out
