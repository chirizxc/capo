"""Generated from Smithy shape ``com.amazonaws.wafv2#DataPointEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.filter_string
    import capo_wafv2.types.monetization_amount_value
    import capo_wafv2.types.request_count
    import capo_wafv2.types.timestamp


class DataPointEntry(TypedDict, closed=True):
    date: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The timestamp for this data point.</p>"""
    monetize_served_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of HTTP 402 Payment Required responses served during this interval.</p>"""
    settled_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of successfully settled payments during this interval.</p>"""
    total_amount: NotRequired[
        "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    ]
    """<p>The total revenue amount during this interval in the specified currency.</p>"""
    category: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The bot category for this data point, when grouped by category.</p>"""
    intent: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The intent classification for this data point, when grouped by intent.</p>"""
    group_by_value: NotRequired["capo_wafv2.types.filter_string.FilterString"]
    """<p>The group-by dimension value for this data point.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataPointEntry) -> dict:
    out: dict = {}
    if "date" in value:
        import capo_wafv2.types.timestamp

        out["Date"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(value["date"])
    out["MonetizeServedCount"] = value.get("monetize_served_count", 0)
    out["SettledCount"] = value.get("settled_count", 0)
    if "total_amount" in value:
        out["TotalAmount"] = value["total_amount"]
    if "category" in value:
        out["Category"] = value["category"]
    if "intent" in value:
        out["Intent"] = value["intent"]
    if "group_by_value" in value:
        out["GroupByValue"] = value["group_by_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataPointEntry:
    out: DataPointEntry = {}  # type: ignore[typeddict-item]
    if data.get("Date") is not None:
        import capo_wafv2.types.timestamp

        out["date"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(data["Date"])
    if data.get("MonetizeServedCount") is not None:
        out["monetize_served_count"] = data["MonetizeServedCount"]
    else:
        out["monetize_served_count"] = 0
    if data.get("SettledCount") is not None:
        out["settled_count"] = data["SettledCount"]
    else:
        out["settled_count"] = 0
    if data.get("TotalAmount") is not None:
        out["total_amount"] = data["TotalAmount"]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Intent") is not None:
        out["intent"] = data["Intent"]
    if data.get("GroupByValue") is not None:
        out["group_by_value"] = data["GroupByValue"]
    return out
