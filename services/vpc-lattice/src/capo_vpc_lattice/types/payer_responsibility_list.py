"""Generated from Smithy shape ``com.amazonaws.vpclattice#PayerResponsibilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.payer_responsibility_entry

PayerResponsibilityList: TypeAlias = list[
    "capo_vpc_lattice.types.payer_responsibility_entry.PayerResponsibilityEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: PayerResponsibilityList) -> list:
    import capo_vpc_lattice.types.payer_responsibility_entry

    out: list = []
    for item in value:
        out.append(
            capo_vpc_lattice.types.payer_responsibility_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PayerResponsibilityList:
    import capo_vpc_lattice.types.payer_responsibility_entry

    out: PayerResponsibilityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_vpc_lattice.types.payer_responsibility_entry.deserialize_json(item)
        )
    return out
