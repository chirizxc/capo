"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorContainerImageScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.container_image_pull_date_rescan_duration
    import capo_inspector2.types.container_image_rescan_duration


class ConnectorContainerImageScanConfiguration(TypedDict, closed=True):
    push_duration: NotRequired[
        "capo_inspector2.types.container_image_rescan_duration.ContainerImageRescanDuration"
    ]
    """<p>The amount of time after a container image is pushed to a repository during which Amazon Inspector continues to rescan the image for vulnerabilities. Valid values are <code>LIFETIME</code>, <code>DAYS_3</code>, <code>DAYS_7</code>, <code>DAYS_14</code>, <code>DAYS_30</code>, <code>DAYS_60</code>, <code>DAYS_90</code>, and <code>DAYS_180</code>.</p>"""
    pull_duration: NotRequired[
        "capo_inspector2.types.container_image_pull_date_rescan_duration.ContainerImagePullDateRescanDuration"
    ]
    """<p>The amount of time after a container image is last pulled from a repository during which Amazon Inspector continues to rescan the image for vulnerabilities. Valid values are <code>DAYS_3</code>, <code>DAYS_7</code>, <code>DAYS_14</code>, <code>DAYS_30</code>, <code>DAYS_60</code>, <code>DAYS_90</code>, and <code>DAYS_180</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorContainerImageScanConfiguration) -> dict:
    out: dict = {}
    if "push_duration" in value:
        out["pushDuration"] = value["push_duration"]
    if "pull_duration" in value:
        out["pullDuration"] = value["pull_duration"]
    return out


def deserialize_json(data: dict) -> ConnectorContainerImageScanConfiguration:
    out: ConnectorContainerImageScanConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("pushDuration") is not None:
        out["push_duration"] = data["pushDuration"]
    if data.get("pullDuration") is not None:
        out["pull_duration"] = data["pullDuration"]
    return out
