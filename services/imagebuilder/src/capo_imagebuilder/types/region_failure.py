"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RegionFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.account_id
    import capo_imagebuilder.types.image_configuration_step
    import capo_imagebuilder.types.non_empty_max_length_string
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.region_failure_status


class RegionFailure(TypedDict, closed=True):
    region: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Region where the failure occurred.</p>"""
    status: NotRequired[
        "capo_imagebuilder.types.region_failure_status.RegionFailureStatus"
    ]
    """<p>The failure status for the Region. Indicates whether the process failed, was canceled, or timed out.</p>"""
    image_configuration_step: NotRequired[
        "capo_imagebuilder.types.image_configuration_step.ImageConfigurationStep"
    ]
    """<p>The image configuration step where the failure occurred. Image Builder sets this property when the failure happened during post-distribution configuration, such as launch template updates or virtual machine (VM) export. This property doesn't appear for failures that occurred while Image Builder copied the image to the Region.</p>"""
    error_message: NotRequired[
        "capo_imagebuilder.types.non_empty_max_length_string.NonEmptyMaxLengthString"
    ]
    """<p>The error message for the failure in the Region.</p>"""
    target_account_id: NotRequired["capo_imagebuilder.types.account_id.AccountId"]
    """<p>The account ID of the account that the image was distributed to in the Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionFailure) -> dict:
    out: dict = {}
    if "region" in value:
        out["region"] = value["region"]
    if "status" in value:
        import capo_imagebuilder.types.region_failure_status

        out["status"] = capo_imagebuilder.types.region_failure_status.serialize_json(
            value["status"]
        )
    if "image_configuration_step" in value:
        import capo_imagebuilder.types.image_configuration_step

        out["imageConfigurationStep"] = (
            capo_imagebuilder.types.image_configuration_step.serialize_json(
                value["image_configuration_step"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "target_account_id" in value:
        out["targetAccountId"] = value["target_account_id"]
    return out


def deserialize_json(data: dict) -> RegionFailure:
    out: RegionFailure = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("status") is not None:
        import capo_imagebuilder.types.region_failure_status

        out["status"] = capo_imagebuilder.types.region_failure_status.deserialize_json(
            data["status"]
        )
    if data.get("imageConfigurationStep") is not None:
        import capo_imagebuilder.types.image_configuration_step

        out["image_configuration_step"] = (
            capo_imagebuilder.types.image_configuration_step.deserialize_json(
                data["imageConfigurationStep"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("targetAccountId") is not None:
        out["target_account_id"] = data["targetAccountId"]
    return out
