"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_container_image_scan_configuration


class ConnectorScanConfiguration(TypedDict, closed=True):
    container_image_scanning: NotRequired[
        "capo_inspector2.types.connector_container_image_scan_configuration.ConnectorContainerImageScanConfiguration"
    ]
    """<p>The container image scanning configuration, including push and pull duration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorScanConfiguration) -> dict:
    out: dict = {}
    if "container_image_scanning" in value:
        import capo_inspector2.types.connector_container_image_scan_configuration

        out["containerImageScanning"] = (
            capo_inspector2.types.connector_container_image_scan_configuration.serialize_json(
                value["container_image_scanning"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorScanConfiguration:
    out: ConnectorScanConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("containerImageScanning") is not None:
        import capo_inspector2.types.connector_container_image_scan_configuration

        out["container_image_scanning"] = (
            capo_inspector2.types.connector_container_image_scan_configuration.deserialize_json(
                data["containerImageScanning"]
            )
        )
    return out
