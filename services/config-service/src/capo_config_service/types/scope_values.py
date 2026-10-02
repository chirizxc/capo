"""Generated from Smithy shape ``com.amazonaws.configservice#ScopeValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.scope_value

ScopeValues: TypeAlias = list["capo_config_service.types.scope_value.ScopeValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ScopeValues:
    return [item for item in data if item is not None]
