"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorScanConfigurationItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.connector_scan_configuration_item

ConnectorScanConfigurationItemList: TypeAlias = list[
    "capo_inspector2.types.connector_scan_configuration_item.ConnectorScanConfigurationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorScanConfigurationItemList) -> list:
    import capo_inspector2.types.connector_scan_configuration_item

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.connector_scan_configuration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectorScanConfigurationItemList:
    import capo_inspector2.types.connector_scan_configuration_item

    out: ConnectorScanConfigurationItemList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_inspector2.types.connector_scan_configuration_item.deserialize_json(
                item
            )
        )
    return out
