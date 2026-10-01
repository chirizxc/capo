"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_profile_type
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.profile_id


class AccessProfileSummary(TypedDict, closed=True):
    profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId"
    """The unique ID of the access profile."""
    arn: "capo_cloudwatchomni.types.arn.Arn"
    """The ARN of this access profile."""
    name: "str"
    """A name that identifies the access profile."""
    description: NotRequired["str"]
    """An optional description of the access profile."""
    profile_type: NotRequired[
        "capo_cloudwatchomni.types.access_profile_type.AccessProfileType"
    ]
    """Who manages the access profile."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessProfileSummary) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "profile_type" in value:
        import capo_cloudwatchomni.types.access_profile_type

        out["profileType"] = (
            capo_cloudwatchomni.types.access_profile_type.serialize_cbor(
                value["profile_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AccessProfileSummary:
    out: AccessProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("AccessProfileSummary.profile_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AccessProfileSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AccessProfileSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("profileType") is not None:
        import capo_cloudwatchomni.types.access_profile_type

        out["profile_type"] = (
            capo_cloudwatchomni.types.access_profile_type.deserialize_cbor(
                data["profileType"]
            )
        )
    return out
