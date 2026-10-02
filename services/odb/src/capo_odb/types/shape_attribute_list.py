"""Generated from Smithy shape ``com.amazonaws.odb#ShapeAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.shape_attribute

ShapeAttributeList: TypeAlias = list["capo_odb.types.shape_attribute.ShapeAttribute"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShapeAttributeList) -> list:
    import capo_odb.types.shape_attribute

    out: list = []
    for item in value:
        out.append(capo_odb.types.shape_attribute.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ShapeAttributeList:
    import capo_odb.types.shape_attribute

    out: ShapeAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_odb.types.shape_attribute.deserialize_aws_json_1_0(item))
    return out
