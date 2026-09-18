"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FastLaunchLaunchTemplateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.launch_template_id
    import capo_imagebuilder.types.non_empty_string


class FastLaunchLaunchTemplateSpecification(TypedDict, closed=True):
    launch_template_id: NotRequired[
        "capo_imagebuilder.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template to use for faster launching for a Windows AMI.</p>"""
    launch_template_name: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the launch template to use for faster launching for a Windows AMI.</p>"""
    launch_template_version: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the launch template to use for faster launching for a Windows AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FastLaunchLaunchTemplateSpecification) -> dict:
    out: dict = {}
    if "launch_template_id" in value:
        out["launchTemplateId"] = value["launch_template_id"]
    if "launch_template_name" in value:
        out["launchTemplateName"] = value["launch_template_name"]
    if "launch_template_version" in value:
        out["launchTemplateVersion"] = value["launch_template_version"]
    return out


def deserialize_json(data: dict) -> FastLaunchLaunchTemplateSpecification:
    out: FastLaunchLaunchTemplateSpecification = {}  # type: ignore[typeddict-item]
    if data.get("launchTemplateId") is not None:
        out["launch_template_id"] = data["launchTemplateId"]
    if data.get("launchTemplateName") is not None:
        out["launch_template_name"] = data["launchTemplateName"]
    if data.get("launchTemplateVersion") is not None:
        out["launch_template_version"] = data["launchTemplateVersion"]
    return out
