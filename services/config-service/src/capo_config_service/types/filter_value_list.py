"""Generated from Smithy shape ``com.amazonaws.configservice#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.string

FilterValueList: TypeAlias = list["capo_config_service.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterValueList:
    return [item for item in data if item is not None]
