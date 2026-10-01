"""Generated from Smithy shape ``com.amazonaws.ec2#ModificationTerms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.modification_reservation_update


class ModificationTerms(TypedDict, closed=True):
    reservation_update: NotRequired[
        "capo_ec2.types.modification_reservation_update.ModificationReservationUpdate"
    ]
    """<p>The changes that will be applied to the Capacity Reservation if you accept the modification terms.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModificationTerms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reservation_update" in value:
        import capo_ec2.types.modification_reservation_update

        capo_ec2.types.modification_reservation_update.serialize_ec2_query(
            value["reservation_update"], pairs, f"{key_prefix}ReservationUpdate"
        )


def deserialize_ec2_query(el: Element) -> ModificationTerms:
    out: ModificationTerms = {}  # type: ignore[typeddict-item]
    child_reservation_update = el.find("reservationUpdate")
    if child_reservation_update is not None:
        import capo_ec2.types.modification_reservation_update

        out["reservation_update"] = (
            capo_ec2.types.modification_reservation_update.deserialize_ec2_query(
                child_reservation_update
            )
        )
    return out
