"""Generated from Smithy shape ``com.amazonaws.guardduty#CloudProvider``."""

from typing import Literal, TypeAlias, cast

CloudProvider: TypeAlias = Literal["AWS",]


# --- restJson1 ser/de ---
def serialize_json(value: CloudProvider) -> str:
    return value


def deserialize_json(data: str) -> CloudProvider:
    return cast(CloudProvider, data)
