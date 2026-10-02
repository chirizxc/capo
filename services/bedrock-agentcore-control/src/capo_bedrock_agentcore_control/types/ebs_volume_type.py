"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EbsVolumeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of Amazon EBS volume.</p>"""
EbsVolumeType: TypeAlias = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "sc1",
    "st1",
    "gp3",
]


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeType) -> str:
    return value


def deserialize_json(data: str) -> EbsVolumeType:
    return cast(EbsVolumeType, data)
