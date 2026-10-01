"""Generated from Smithy shape ``com.amazonaws.connect#IsolatedRegionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.aws_region

IsolatedRegionsList: TypeAlias = list["capo_connect.types.aws_region.AwsRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: IsolatedRegionsList) -> list:
    return list(value)


def deserialize_json(data: list) -> IsolatedRegionsList:
    return [item for item in data if item is not None]
