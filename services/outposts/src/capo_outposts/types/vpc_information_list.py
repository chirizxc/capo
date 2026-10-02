"""Generated from Smithy shape ``com.amazonaws.outposts#VpcInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.vpc_information

VpcInformationList: TypeAlias = list[
    "capo_outposts.types.vpc_information.VpcInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: VpcInformationList) -> list:
    import capo_outposts.types.vpc_information

    out: list = []
    for item in value:
        out.append(capo_outposts.types.vpc_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> VpcInformationList:
    import capo_outposts.types.vpc_information

    out: VpcInformationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_outposts.types.vpc_information.deserialize_json(item))
    return out
