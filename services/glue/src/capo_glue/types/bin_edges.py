"""Generated from Smithy shape ``com.amazonaws.glue#BinEdges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.generic_string

BinEdges: TypeAlias = list["capo_glue.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BinEdges) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BinEdges:
    return [item for item in data if item is not None]
