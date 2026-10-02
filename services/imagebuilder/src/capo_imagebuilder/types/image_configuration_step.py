"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageConfigurationStep``."""

from typing import Literal, TypeAlias, cast

ImageConfigurationStep: TypeAlias = Literal[
    "ASSOCIATE_LICENSES",
    "UPDATE_LAUNCH_TEMPLATES",
    "PUT_SSM_PARAMETERS",
    "UPDATE_FAST_LAUNCH_CONFIGURATIONS",
    "EXPORT_AMI",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfigurationStep) -> str:
    return value


def deserialize_json(data: str) -> ImageConfigurationStep:
    return cast(ImageConfigurationStep, data)
