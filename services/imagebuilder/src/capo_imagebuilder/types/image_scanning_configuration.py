"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ecr_configuration
    import capo_imagebuilder.types.nullable_boolean


class ImageScanningConfiguration(TypedDict, closed=True):
    image_scanning_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether Amazon Inspector scans for vulnerabilities when you create a new image, and whether Image Builder saves the findings. Amazon Inspector must be enabled in the account. Image tests must also be enabled. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository from your <code>ecrConfiguration</code> settings.</p>"""
    ecr_configuration: NotRequired[
        "capo_imagebuilder.types.ecr_configuration.EcrConfiguration"
    ]
    """<p>Contains Amazon ECR settings for vulnerability scans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanningConfiguration) -> dict:
    out: dict = {}
    if "image_scanning_enabled" in value:
        out["imageScanningEnabled"] = value["image_scanning_enabled"]
    if "ecr_configuration" in value:
        import capo_imagebuilder.types.ecr_configuration

        out["ecrConfiguration"] = (
            capo_imagebuilder.types.ecr_configuration.serialize_json(
                value["ecr_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageScanningConfiguration:
    out: ImageScanningConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageScanningEnabled") is not None:
        out["image_scanning_enabled"] = data["imageScanningEnabled"]
    if data.get("ecrConfiguration") is not None:
        import capo_imagebuilder.types.ecr_configuration

        out["ecr_configuration"] = (
            capo_imagebuilder.types.ecr_configuration.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    return out
