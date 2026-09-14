"""Generated from Smithy shape ``com.amazonaws.sesv2#PlacementStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.percentage


class PlacementStatistics(TypedDict, closed=True):
    inbox_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that arrived in recipients' inboxes during the predictive inbox placement test.</p>"""
    spam_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that arrived in recipients' spam or junk mail folders during the predictive inbox placement test.</p>"""
    missing_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that didn't arrive in recipients' inboxes at all during the predictive inbox placement test.</p>"""
    spf_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.</p>"""
    dkim_percentage: NotRequired["capo_sesv2.types.percentage.Percentage"]
    """<p>The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlacementStatistics) -> dict:
    out: dict = {}
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
    if "missing_percentage" in value:
        out["MissingPercentage"] = (
            "NaN"
            if value["missing_percentage"] != value["missing_percentage"]
            else "Infinity"
            if value["missing_percentage"] == float("inf")
            else "-Infinity"
            if value["missing_percentage"] == float("-inf")
            else value["missing_percentage"]
        )
    if "spf_percentage" in value:
        out["SpfPercentage"] = (
            "NaN"
            if value["spf_percentage"] != value["spf_percentage"]
            else "Infinity"
            if value["spf_percentage"] == float("inf")
            else "-Infinity"
            if value["spf_percentage"] == float("-inf")
            else value["spf_percentage"]
        )
    if "dkim_percentage" in value:
        out["DkimPercentage"] = (
            "NaN"
            if value["dkim_percentage"] != value["dkim_percentage"]
            else "Infinity"
            if value["dkim_percentage"] == float("inf")
            else "-Infinity"
            if value["dkim_percentage"] == float("-inf")
            else value["dkim_percentage"]
        )
    return out


def deserialize_json(data: dict) -> PlacementStatistics:
    out: PlacementStatistics = {}  # type: ignore[typeddict-item]
    if data.get("InboxPercentage") is not None:
        out["inbox_percentage"] = float(data["InboxPercentage"])
    if data.get("SpamPercentage") is not None:
        out["spam_percentage"] = float(data["SpamPercentage"])
    if data.get("MissingPercentage") is not None:
        out["missing_percentage"] = float(data["MissingPercentage"])
    if data.get("SpfPercentage") is not None:
        out["spf_percentage"] = float(data["SpfPercentage"])
    if data.get("DkimPercentage") is not None:
        out["dkim_percentage"] = float(data["DkimPercentage"])
    return out
