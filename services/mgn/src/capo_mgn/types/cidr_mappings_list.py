"""Generated from Smithy shape ``com.amazonaws.mgn#CidrMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.cidr_mapping

CidrMappingsList: TypeAlias = list["capo_mgn.types.cidr_mapping.CidrMapping"]


# --- restJson1 ser/de ---
def serialize_json(value: CidrMappingsList) -> list:
    import capo_mgn.types.cidr_mapping

    out: list = []
    for item in value:
        out.append(capo_mgn.types.cidr_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> CidrMappingsList:
    import capo_mgn.types.cidr_mapping

    out: CidrMappingsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.cidr_mapping.deserialize_json(item))
    return out
