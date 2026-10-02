"""Generated from Smithy shape ``com.amazonaws.vpclattice#CidrRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.cidr_range

CidrRangeList: TypeAlias = list["capo_vpc_lattice.types.cidr_range.CidrRange"]


# --- restJson1 ser/de ---
def serialize_json(value: CidrRangeList) -> list:
    return list(value)


def deserialize_json(data: list) -> CidrRangeList:
    return [item for item in data if item is not None]
