"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AccessProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.access_profile_type
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.assume_status
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.space_id


class AccessProfile(TypedDict, closed=True):
    profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId"
    """The unique ID of the access profile."""
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The ID of the space the profile belongs to."""
    arn: "capo_cloudwatchomni.types.arn.Arn"
    """The ARN of this access profile."""
    name: "str"
    """A name that identifies the access profile."""
    description: NotRequired["str"]
    """An optional description of the access profile."""
    created_at: "datetime.datetime"
    """The timestamp when the access profile was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the access profile was last updated."""
    assume_status: NotRequired["capo_cloudwatchomni.types.assume_status.AssumeStatus"]
    """The calling principal's authorization to assume this access profile."""
    profile_type: NotRequired[
        "capo_cloudwatchomni.types.access_profile_type.AccessProfileType"
    ]
    """Who manages the access profile."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessProfile) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["spaceId"] = value["space_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    if "assume_status" in value:
        import capo_cloudwatchomni.types.assume_status

        out["assumeStatus"] = capo_cloudwatchomni.types.assume_status.serialize_cbor(
            value["assume_status"]
        )
    if "profile_type" in value:
        import capo_cloudwatchomni.types.access_profile_type

        out["profileType"] = (
            capo_cloudwatchomni.types.access_profile_type.serialize_cbor(
                value["profile_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AccessProfile:
    out: AccessProfile = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("AccessProfile.profile_id required")
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("AccessProfile.space_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AccessProfile.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AccessProfile.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AccessProfile.created_at required")
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AccessProfile.updated_at required")
    if data.get("assumeStatus") is not None:
        import capo_cloudwatchomni.types.assume_status

        out["assume_status"] = capo_cloudwatchomni.types.assume_status.deserialize_cbor(
            data["assumeStatus"]
        )
    if data.get("profileType") is not None:
        import capo_cloudwatchomni.types.access_profile_type

        out["profile_type"] = (
            capo_cloudwatchomni.types.access_profile_type.deserialize_cbor(
                data["profileType"]
            )
        )
    return out
