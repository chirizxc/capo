"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeSecurityHubV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.features
    import capo_securityhub.types.iso_string
    import capo_securityhub.types.non_empty_string


class DescribeSecurityHubV2Response(TypedDict, closed=True):
    hub_v2_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the service resource.</p>"""
    subscribed_at: NotRequired["capo_securityhub.types.iso_string.IsoString"]
    """<p>The date and time when the service was enabled in the account.</p>"""
    features: NotRequired["capo_securityhub.types.features.Features"]
    """<p>A map of opt-in features and their current status and metadata for the account in the current Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityHubV2Response) -> dict:
    out: dict = {}
    if "hub_v2_arn" in value:
        out["HubV2Arn"] = value["hub_v2_arn"]
    if "subscribed_at" in value:
        out["SubscribedAt"] = value["subscribed_at"]
    if "features" in value:
        import capo_securityhub.types.features

        out["Features"] = capo_securityhub.types.features.serialize_json(
            value["features"]
        )
    return out


def deserialize_json(data: dict) -> DescribeSecurityHubV2Response:
    out: DescribeSecurityHubV2Response = {}  # type: ignore[typeddict-item]
    if data.get("HubV2Arn") is not None:
        out["hub_v2_arn"] = data["HubV2Arn"]
    if data.get("SubscribedAt") is not None:
        out["subscribed_at"] = data["SubscribedAt"]
    if data.get("Features") is not None:
        import capo_securityhub.types.features

        out["features"] = capo_securityhub.types.features.deserialize_json(
            data["Features"]
        )
    return out
