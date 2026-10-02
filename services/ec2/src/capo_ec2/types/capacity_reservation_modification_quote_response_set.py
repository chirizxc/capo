"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationModificationQuoteResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_modification_quote

CapacityReservationModificationQuoteResponseSet: TypeAlias = list[
    "capo_ec2.types.capacity_reservation_modification_quote.CapacityReservationModificationQuote"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationModificationQuoteResponseSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_reservation_modification_quote

        capo_ec2.types.capacity_reservation_modification_quote.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> CapacityReservationModificationQuoteResponseSet:
    import capo_ec2.types.capacity_reservation_modification_quote

    out: CapacityReservationModificationQuoteResponseSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_reservation_modification_quote.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityReservationModificationQuoteResponseSet:
    import capo_ec2.types.capacity_reservation_modification_quote

    out: CapacityReservationModificationQuoteResponseSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_reservation_modification_quote.deserialize_ec2_query(
                child
            )
        )
    return out
