"""Generated from Smithy shape ``com.amazonaws.elementalinference#DataSourceSport``."""

from typing import Literal, TypeAlias, cast

DataSourceSport: TypeAlias = Literal[
    "basketball",
    "american-football",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSport) -> str:
    return value


def deserialize_json(data: str) -> DataSourceSport:
    return cast(DataSourceSport, data)
