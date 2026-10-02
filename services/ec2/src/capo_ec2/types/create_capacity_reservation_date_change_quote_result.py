"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationDateChangeQuoteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_modification_quote


class CreateCapacityReservationDateChangeQuoteResult(TypedDict, closed=True):
    capacity_reservation_modification_quote: NotRequired[
        "capo_ec2.types.capacity_reservation_modification_quote.CapacityReservationModificationQuote"
    ]
    """<p>Information about the Capacity Reservation date change quote.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationDateChangeQuoteResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_modification_quote" in value:
        import capo_ec2.types.capacity_reservation_modification_quote

        capo_ec2.types.capacity_reservation_modification_quote.serialize_ec2_query(
            value["capacity_reservation_modification_quote"],
            pairs,
            f"{key_prefix}CapacityReservationModificationQuote",
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateCapacityReservationDateChangeQuoteResult:
    out: CreateCapacityReservationDateChangeQuoteResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_modification_quote = el.find(
        "capacityReservationModificationQuote"
    )
    if child_capacity_reservation_modification_quote is not None:
        import capo_ec2.types.capacity_reservation_modification_quote

        out["capacity_reservation_modification_quote"] = (
            capo_ec2.types.capacity_reservation_modification_quote.deserialize_ec2_query(
                child_capacity_reservation_modification_quote
            )
        )
    return out
