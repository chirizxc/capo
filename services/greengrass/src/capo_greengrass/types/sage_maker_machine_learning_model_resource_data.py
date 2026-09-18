"""Generated from Smithy shape ``com.amazonaws.greengrass#SageMakerMachineLearningModelResourceData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.resource_download_owner_setting


class SageMakerMachineLearningModelResourceData(TypedDict, closed=True):
    destination_path: NotRequired["capo_greengrass.types.__string.__string"]
    """The absolute local path of the resource inside the Lambda environment."""
    owner_setting: NotRequired[
        "capo_greengrass.types.resource_download_owner_setting.ResourceDownloadOwnerSetting"
    ]
    sage_maker_job_arn: NotRequired["capo_greengrass.types.__string.__string"]
    """The ARN of the Amazon SageMaker training job that represents the source model."""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerMachineLearningModelResourceData) -> dict:
    out: dict = {}
    if "destination_path" in value:
        out["DestinationPath"] = value["destination_path"]
    if "owner_setting" in value:
        import capo_greengrass.types.resource_download_owner_setting

        out["OwnerSetting"] = (
            capo_greengrass.types.resource_download_owner_setting.serialize_json(
                value["owner_setting"]
            )
        )
    if "sage_maker_job_arn" in value:
        out["SageMakerJobArn"] = value["sage_maker_job_arn"]
    return out


def deserialize_json(data: dict) -> SageMakerMachineLearningModelResourceData:
    out: SageMakerMachineLearningModelResourceData = {}  # type: ignore[typeddict-item]
    if data.get("DestinationPath") is not None:
        out["destination_path"] = data["DestinationPath"]
    if data.get("OwnerSetting") is not None:
        import capo_greengrass.types.resource_download_owner_setting

        out["owner_setting"] = (
            capo_greengrass.types.resource_download_owner_setting.deserialize_json(
                data["OwnerSetting"]
            )
        )
    if data.get("SageMakerJobArn") is not None:
        out["sage_maker_job_arn"] = data["SageMakerJobArn"]
    return out
