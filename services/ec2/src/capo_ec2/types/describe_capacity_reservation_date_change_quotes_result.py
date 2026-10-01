"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationDateChangeQuotesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_modification_quote_response_set
    import capo_ec2.types.string


class DescribeCapacityReservationDateChangeQuotesResult(TypedDict, closed=True):
    capacity_reservation_modification_quotes: NotRequired[
        "capo_ec2.types.capacity_reservation_modification_quote_response_set.CapacityReservationModificationQuoteResponseSet"
    ]
    """<p>Information about the Capacity Reservation date change quotes.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationDateChangeQuotesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_modification_quotes" in value:
        import capo_ec2.types.capacity_reservation_modification_quote_response_set

        capo_ec2.types.capacity_reservation_modification_quote_response_set.serialize_ec2_query(
            value["capacity_reservation_modification_quotes"],
            pairs,
            f"{key_prefix}CapacityReservationModificationQuoteSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityReservationDateChangeQuotesResult:
    out: DescribeCapacityReservationDateChangeQuotesResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_modification_quotes = el.find(
        "capacityReservationModificationQuoteSet"
    )
    if child_capacity_reservation_modification_quotes is not None:
        import capo_ec2.types.capacity_reservation_modification_quote_response_set

        out["capacity_reservation_modification_quotes"] = (
            capo_ec2.types.capacity_reservation_modification_quote_response_set.deserialize_ec2_query(
                child_capacity_reservation_modification_quotes
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
