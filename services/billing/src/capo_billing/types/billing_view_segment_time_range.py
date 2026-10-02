"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewSegmentTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class BillingViewSegmentTimeRange(TypedDict, closed=True):
    begin_date_inclusive: NotRequired["datetime.datetime"]
    """<p> The inclusive start of the time range. This value can't be in the future. </p>"""
    end_date_exclusive: NotRequired["datetime.datetime"]
    """<p> The exclusive end of the time range. This value must be after <code>beginDateInclusive</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewSegmentTimeRange) -> dict:
    out: dict = {}
    if "begin_date_inclusive" in value:
        import capo_billing.types._prelude.timestamp

        out["beginDateInclusive"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["begin_date_inclusive"]
            )
        )
    if "end_date_exclusive" in value:
        import capo_billing.types._prelude.timestamp

        out["endDateExclusive"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_date_exclusive"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewSegmentTimeRange:
    out: BillingViewSegmentTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("beginDateInclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["begin_date_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["beginDateInclusive"]
            )
        )
    if data.get("endDateExclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date_exclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDateExclusive"]
            )
        )
    return out
