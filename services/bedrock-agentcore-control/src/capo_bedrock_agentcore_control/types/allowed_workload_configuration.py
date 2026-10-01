"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedWorkloadConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.hosting_environment_list_type
    import capo_bedrock_agentcore_control.types.workload_identity_name_list_type


class AllowedWorkloadConfiguration(TypedDict, closed=True):
    hosting_environments: NotRequired[
        "capo_bedrock_agentcore_control.types.hosting_environment_list_type.HostingEnvironmentListType"
    ]
    """<p>The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.</p>"""
    workload_identities: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_name_list_type.WorkloadIdentityNameListType"
    ]
    """<p>The list of workload identities that are allowed to invoke the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedWorkloadConfiguration) -> dict:
    out: dict = {}
    if "hosting_environments" in value:
        import capo_bedrock_agentcore_control.types.hosting_environment_list_type

        out["hostingEnvironments"] = (
            capo_bedrock_agentcore_control.types.hosting_environment_list_type.serialize_json(
                value["hosting_environments"]
            )
        )
    if "workload_identities" in value:
        import capo_bedrock_agentcore_control.types.workload_identity_name_list_type

        out["workloadIdentities"] = (
            capo_bedrock_agentcore_control.types.workload_identity_name_list_type.serialize_json(
                value["workload_identities"]
            )
        )
    return out


def deserialize_json(data: dict) -> AllowedWorkloadConfiguration:
    out: AllowedWorkloadConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("hostingEnvironments") is not None:
        import capo_bedrock_agentcore_control.types.hosting_environment_list_type

        out["hosting_environments"] = (
            capo_bedrock_agentcore_control.types.hosting_environment_list_type.deserialize_json(
                data["hostingEnvironments"]
            )
        )
    if data.get("workloadIdentities") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_name_list_type

        out["workload_identities"] = (
            capo_bedrock_agentcore_control.types.workload_identity_name_list_type.deserialize_json(
                data["workloadIdentities"]
            )
        )
    return out
