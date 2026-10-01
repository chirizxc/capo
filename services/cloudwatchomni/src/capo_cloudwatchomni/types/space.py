"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Space``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.encryption_configuration
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.space_status


class Space(TypedDict, closed=True):
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
    data_access_role_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The ARN of the IAM role used for data access."""
    created_at: "datetime.datetime"
    """The timestamp when the space was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the space was last updated."""
    agent_core_evaluation_role_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """The ARN of the IAM role used by AgentCore online evaluation. Absent when the space was created without one."""
    status: "capo_cloudwatchomni.types.space_status.SpaceStatus"
    """The status of the space."""
    status_reason: NotRequired["str"]
    """Reason for the current space status."""
    encryption_configuration: NotRequired[
        "capo_cloudwatchomni.types.encryption_configuration.EncryptionConfiguration"
    ]
    """How the space's data at rest is encrypted. Always populated: a space with no customer managed key reports `encryptionStrategy` AWS_OWNED and no `kmsKeyArn`."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Space) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
    out["spaceArn"] = value["space_arn"]
    if "domain_arn" in value:
        out["domainArn"] = value["domain_arn"]
    out["region"] = value["region"]
    out["ownerAccountId"] = value["owner_account_id"]
    out["dataAccessRoleArn"] = value["data_access_role_arn"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    if "agent_core_evaluation_role_arn" in value:
        out["agentCoreEvaluationRoleArn"] = value["agent_core_evaluation_role_arn"]
    import capo_cloudwatchomni.types.space_status

    out["status"] = capo_cloudwatchomni.types.space_status.serialize_cbor(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "encryption_configuration" in value:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_cloudwatchomni.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Space:
    out: Space = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("Space.space_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Space.name required")
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    else:
        raise DeserializationError("Space.space_arn required")
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        raise DeserializationError("Space.region required")
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError("Space.owner_account_id required")
    if data.get("dataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["dataAccessRoleArn"]
    else:
        raise DeserializationError("Space.data_access_role_arn required")
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Space.created_at required")
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Space.updated_at required")
    if data.get("agentCoreEvaluationRoleArn") is not None:
        out["agent_core_evaluation_role_arn"] = data["agentCoreEvaluationRoleArn"]
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.space_status

        out["status"] = capo_cloudwatchomni.types.space_status.deserialize_cbor(
            data["status"]
        )
    else:
        raise DeserializationError("Space.status required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("encryptionConfiguration") is not None:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_cloudwatchomni.types.encryption_configuration.deserialize_cbor(
                data["encryptionConfiguration"]
            )
        )
    return out
