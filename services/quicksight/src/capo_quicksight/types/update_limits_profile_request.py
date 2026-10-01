"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateLimitsProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.profile_description
    import capo_quicksight.types.profile_id
    import capo_quicksight.types.profile_name
    import capo_quicksight.types.resource_limits_map


class UpdateLimitsProfileRequest(TypedDict, closed=True):
    profile_id: "capo_quicksight.types.profile_id.ProfileId"
    """<p>The unique identifier for the limits profile to update.</p>"""
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the limits profile.</p>"""
    profile_name: NotRequired["capo_quicksight.types.profile_name.ProfileName"]
    """<p>A new display name for the limits profile.</p>"""
    description: NotRequired[
        "capo_quicksight.types.profile_description.ProfileDescription"
    ]
    """<p>A new description for the limits profile.</p>"""
    resource_limits: NotRequired[
        "capo_quicksight.types.resource_limits_map.ResourceLimitsMap"
    ]
    """<p>A map of resource types to their updated limit values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLimitsProfileRequest) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["profileName"] = value["profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resource_limits" in value:
        import capo_quicksight.types.resource_limits_map

        out["resourceLimits"] = (
            capo_quicksight.types.resource_limits_map.serialize_json(
                value["resource_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateLimitsProfileRequest:
    out: UpdateLimitsProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceLimits") is not None:
        import capo_quicksight.types.resource_limits_map

        out["resource_limits"] = (
            capo_quicksight.types.resource_limits_map.deserialize_json(
                data["resourceLimits"]
            )
        )
    return out
