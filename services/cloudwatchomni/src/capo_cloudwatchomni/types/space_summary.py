"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SpaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.space_status


class SpaceSummary(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    name: "str"
    """A name that identifies the space."""
    space_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the space."""
    domain_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """The Amazon Resource Name (ARN) of the domain the space belongs to. Absent when the space is not associated with a domain, so callers must tolerate its absence."""
    region: "str"
    """The region where this space was created."""
    owner_account_id: "capo_cloudwatchomni.types.account_id.AccountId"
    """AWS account ID that owns this space."""
    status: "capo_cloudwatchomni.types.space_status.SpaceStatus"
    """The status of the space."""
    status_reason: NotRequired["str"]
    """Reason for the current space status."""
    created_at: "datetime.datetime"
    """The timestamp when the space was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the space was last updated."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SpaceSummary) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
    out["spaceArn"] = value["space_arn"]
    if "domain_arn" in value:
        out["domainArn"] = value["domain_arn"]
    out["region"] = value["region"]
    out["ownerAccountId"] = value["owner_account_id"]
    import capo_cloudwatchomni.types.space_status

    out["status"] = capo_cloudwatchomni.types.space_status.serialize_cbor(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    return out


def deserialize_cbor(data: dict) -> SpaceSummary:
    out: SpaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("SpaceSummary.space_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpaceSummary.name required")
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    else:
        raise DeserializationError("SpaceSummary.space_arn required")
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        raise DeserializationError("SpaceSummary.region required")
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError("SpaceSummary.owner_account_id required")
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.space_status

        out["status"] = capo_cloudwatchomni.types.space_status.deserialize_cbor(
            data["status"]
        )
    else:
        raise DeserializationError("SpaceSummary.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SpaceSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("SpaceSummary.updated_at required")
    return out
