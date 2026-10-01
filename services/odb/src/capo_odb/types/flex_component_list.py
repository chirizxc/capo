"""Generated from Smithy shape ``com.amazonaws.odb#FlexComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.flex_component_summary

FlexComponentList: TypeAlias = list[
    "capo_odb.types.flex_component_summary.FlexComponentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlexComponentList) -> list:
    import capo_odb.types.flex_component_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.flex_component_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FlexComponentList:
    import capo_odb.types.flex_component_summary

    out: FlexComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_odb.types.flex_component_summary.deserialize_aws_json_1_0(item))
    return out
