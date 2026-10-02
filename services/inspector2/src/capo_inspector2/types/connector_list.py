"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.connector

ConnectorList: TypeAlias = list["capo_inspector2.types.connector.Connector"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorList) -> list:
    import capo_inspector2.types.connector

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.connector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorList:
    import capo_inspector2.types.connector

    out: ConnectorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_inspector2.types.connector.deserialize_json(item))
    return out
