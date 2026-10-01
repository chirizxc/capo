"""Generated from Smithy shape ``com.amazonaws.devopsagent#AWSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.monitor_account_type
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.validation_status


class AWSConfiguration(TypedDict, closed=True):
    assumable_role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>Role ARN to be assumed by AIDevOps to operate on behalf of customer.</p>"""
    account_id: "str"
    """<p>AWS Account Id corresponding to provided resources.</p>"""
    account_type: "capo_devops_agent.types.monitor_account_type.MonitorAccountType"
    """<p>Account Type 'monitor' for AIDevOps monitoring.</p>"""
    agent_elevated_role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]
    """<p>Optional IAM role ARN to be assumed by AIDevOps for elevated directed actions on behalf of the customer. Used for mutating operations gated by elevatedActionsEnabled on the AgentSpace. When not provided, only non-elevated directed actions are available for this AWS account.</p>"""
    agent_elevated_role_arn_status: NotRequired[
        "capo_devops_agent.types.validation_status.ValidationStatus"
    ]
    """<p>Validation status of the agentElevatedRoleArn. Updated asynchronously after the customer registers an elevated role. Possible values: PENDING_CONFIRMATION (validation in progress), VALID (role validated), INVALID (validation failed).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSConfiguration) -> dict:
    out: dict = {}
    out["assumableRoleArn"] = value["assumable_role_arn"]
    out["accountId"] = value["account_id"]
    import capo_devops_agent.types.monitor_account_type

    out["accountType"] = capo_devops_agent.types.monitor_account_type.serialize_json(
        value["account_type"]
    )
    if "agent_elevated_role_arn" in value:
        out["agentElevatedRoleArn"] = value["agent_elevated_role_arn"]
    if "agent_elevated_role_arn_status" in value:
        import capo_devops_agent.types.validation_status

        out["agentElevatedRoleArnStatus"] = (
            capo_devops_agent.types.validation_status.serialize_json(
                value["agent_elevated_role_arn_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AWSConfiguration:
    out: AWSConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("assumableRoleArn") is not None:
        out["assumable_role_arn"] = data["assumableRoleArn"]
    else:
        raise DeserializationError("AWSConfiguration.assumable_role_arn required")
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AWSConfiguration.account_id required")
    if data.get("accountType") is not None:
        import capo_devops_agent.types.monitor_account_type

        out["account_type"] = (
            capo_devops_agent.types.monitor_account_type.deserialize_json(
                data["accountType"]
            )
        )
    else:
        raise DeserializationError("AWSConfiguration.account_type required")
    if data.get("agentElevatedRoleArn") is not None:
        out["agent_elevated_role_arn"] = data["agentElevatedRoleArn"]
    if data.get("agentElevatedRoleArnStatus") is not None:
        import capo_devops_agent.types.validation_status

        out["agent_elevated_role_arn_status"] = (
            capo_devops_agent.types.validation_status.deserialize_json(
                data["agentElevatedRoleArnStatus"]
            )
        )
    return out
