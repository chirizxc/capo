"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#RecordIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.value_as_string

RecordIdentifierList: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordIdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecordIdentifierList:
    return [item for item in data if item is not None]
