"""Generated from Smithy shape ``com.amazonaws.quicksight#DlpSettingStatus``."""

from typing import Literal, TypeAlias, cast

DlpSettingStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DlpSettingStatus) -> str:
    return value


def deserialize_json(data: str) -> DlpSettingStatus:
    return cast(DlpSettingStatus, data)
