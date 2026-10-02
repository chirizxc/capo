"""Generated from Smithy shape ``com.amazonaws.guardduty#CloudDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.cloud_provider
    import capo_guardduty.types.string


class CloudDetails(TypedDict, closed=True):
    provider: NotRequired["capo_guardduty.types.cloud_provider.CloudProvider"]
    """<p>The cloud provider. Currently, only <code>AWS</code> is supported.</p>"""
    region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services Region in which the investigated resource resides.</p>"""
    account: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID of the investigated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudDetails) -> dict:
    out: dict = {}
    if "provider" in value:
        import capo_guardduty.types.cloud_provider

        out["provider"] = capo_guardduty.types.cloud_provider.serialize_json(
            value["provider"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "account" in value:
        out["account"] = value["account"]
    return out


def deserialize_json(data: dict) -> CloudDetails:
    out: CloudDetails = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_guardduty.types.cloud_provider

        out["provider"] = capo_guardduty.types.cloud_provider.deserialize_json(
            data["provider"]
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("account") is not None:
        out["account"] = data["account"]
    return out
