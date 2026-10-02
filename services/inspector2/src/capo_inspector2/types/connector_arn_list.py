"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn

ConnectorArnList: TypeAlias = list["capo_inspector2.types.connector_arn.ConnectorArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorArnList:
    return [item for item in data if item is not None]
