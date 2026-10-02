"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationModificationQuoteState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

CapacityReservationModificationQuoteState: TypeAlias = Literal[
    "active",
    "expired",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: CapacityReservationModificationQuoteState) -> str:
    return value


def from_ec2_query_text(text: str) -> CapacityReservationModificationQuoteState:
    return cast(CapacityReservationModificationQuoteState, text)


def serialize_ec2_query(
    value: CapacityReservationModificationQuoteState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> CapacityReservationModificationQuoteState:
    return from_ec2_query_text(el.text or "")
