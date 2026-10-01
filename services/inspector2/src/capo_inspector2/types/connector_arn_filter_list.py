"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn_filter

ConnectorArnFilterList: TypeAlias = list[
    "capo_inspector2.types.connector_arn_filter.ConnectorArnFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorArnFilterList) -> list:
    import capo_inspector2.types.connector_arn_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.connector_arn_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorArnFilterList:
    import capo_inspector2.types.connector_arn_filter

    out: ConnectorArnFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_inspector2.types.connector_arn_filter.deserialize_json(item))
    return out
