"""Generated from Smithy shape ``com.amazonaws.securityhub#AIDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AIDetails(TypedDict, closed=True):
    host_resource_guid: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the host resource that hosts the self-hosted AI resource. Present only on self-hosted AI resources.</p>"""
    host_resource_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The <code>ResourceType</code> of the host resource that hosts the self-hosted AI resource, such as <code>AWS::EC2::Instance</code>. Present only on self-hosted AI resources.</p>"""
    canonical_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The canonical identifier for the AI resource, independent of where it is deployed. Multiple occurrences of the same resource on different hosts share the same <code>CanonicalId</code>. For model resources, the value follows the format <code>model/<purl></code>, such as <code>model/pkg:huggingface/meta-llama/llama-3-8b</code>. Present only on self-hosted AI resources.</p>"""
    self_hosted_ai_model_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>Model</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_agent_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>Agent</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_model_serving_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>ModelServing</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_external_endpoint_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>ExternalEndpoint</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_development_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>Development</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_agent_framework_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>AgentFramework</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_ai_agent_tools_and_identity_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of self-hosted AI resources of <code>ResourceSubCategory</code> <code>AgentToolsAndIdentity</code> detected on the host resource. Present only on host resources.</p>"""
    self_hosted_total_ai_resource_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The total number of all self-hosted AI resources detected on the host resource. Present only on host resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIDetails) -> dict:
    out: dict = {}
    if "host_resource_guid" in value:
        out["HostResourceGuid"] = value["host_resource_guid"]
    if "host_resource_type" in value:
        out["HostResourceType"] = value["host_resource_type"]
    if "canonical_id" in value:
        out["CanonicalId"] = value["canonical_id"]
    if "self_hosted_ai_model_resource_count" in value:
        out["SelfHostedAIModelResourceCount"] = value[
            "self_hosted_ai_model_resource_count"
        ]
    if "self_hosted_ai_agent_resource_count" in value:
        out["SelfHostedAIAgentResourceCount"] = value[
            "self_hosted_ai_agent_resource_count"
        ]
    if "self_hosted_ai_model_serving_resource_count" in value:
        out["SelfHostedAIModelServingResourceCount"] = value[
            "self_hosted_ai_model_serving_resource_count"
        ]
    if "self_hosted_ai_external_endpoint_resource_count" in value:
        out["SelfHostedAIExternalEndpointResourceCount"] = value[
            "self_hosted_ai_external_endpoint_resource_count"
        ]
    if "self_hosted_ai_development_resource_count" in value:
        out["SelfHostedAIDevelopmentResourceCount"] = value[
            "self_hosted_ai_development_resource_count"
        ]
    if "self_hosted_ai_agent_framework_resource_count" in value:
        out["SelfHostedAIAgentFrameworkResourceCount"] = value[
            "self_hosted_ai_agent_framework_resource_count"
        ]
    if "self_hosted_ai_agent_tools_and_identity_resource_count" in value:
        out["SelfHostedAIAgentToolsAndIdentityResourceCount"] = value[
            "self_hosted_ai_agent_tools_and_identity_resource_count"
        ]
    if "self_hosted_total_ai_resource_count" in value:
        out["SelfHostedTotalAIResourceCount"] = value[
            "self_hosted_total_ai_resource_count"
        ]
    return out


def deserialize_json(data: dict) -> AIDetails:
    out: AIDetails = {}  # type: ignore[typeddict-item]
    if data.get("HostResourceGuid") is not None:
        out["host_resource_guid"] = data["HostResourceGuid"]
    if data.get("HostResourceType") is not None:
        out["host_resource_type"] = data["HostResourceType"]
    if data.get("CanonicalId") is not None:
        out["canonical_id"] = data["CanonicalId"]
    if data.get("SelfHostedAIModelResourceCount") is not None:
        out["self_hosted_ai_model_resource_count"] = data[
            "SelfHostedAIModelResourceCount"
        ]
    if data.get("SelfHostedAIAgentResourceCount") is not None:
        out["self_hosted_ai_agent_resource_count"] = data[
            "SelfHostedAIAgentResourceCount"
        ]
    if data.get("SelfHostedAIModelServingResourceCount") is not None:
        out["self_hosted_ai_model_serving_resource_count"] = data[
            "SelfHostedAIModelServingResourceCount"
        ]
    if data.get("SelfHostedAIExternalEndpointResourceCount") is not None:
        out["self_hosted_ai_external_endpoint_resource_count"] = data[
            "SelfHostedAIExternalEndpointResourceCount"
        ]
    if data.get("SelfHostedAIDevelopmentResourceCount") is not None:
        out["self_hosted_ai_development_resource_count"] = data[
            "SelfHostedAIDevelopmentResourceCount"
        ]
    if data.get("SelfHostedAIAgentFrameworkResourceCount") is not None:
        out["self_hosted_ai_agent_framework_resource_count"] = data[
            "SelfHostedAIAgentFrameworkResourceCount"
        ]
    if data.get("SelfHostedAIAgentToolsAndIdentityResourceCount") is not None:
        out["self_hosted_ai_agent_tools_and_identity_resource_count"] = data[
            "SelfHostedAIAgentToolsAndIdentityResourceCount"
        ]
    if data.get("SelfHostedTotalAIResourceCount") is not None:
        out["self_hosted_total_ai_resource_count"] = data[
            "SelfHostedTotalAIResourceCount"
        ]
    return out
