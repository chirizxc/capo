"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#AccessPolicyDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.access_policy_type
    import capo_opensearchserverless.types.policy_description
    import capo_opensearchserverless.types.policy_name
    import capo_opensearchserverless.types.policy_version


class AccessPolicyDetail(TypedDict, closed=True):
    type: NotRequired[
        "capo_opensearchserverless.types.access_policy_type.AccessPolicyType"
    ]
    """<p>The type of access policy.</p>"""
    name: NotRequired["capo_opensearchserverless.types.policy_name.PolicyName"]
    """<p>The name of the policy.</p>"""
    policy_version: NotRequired[
        "capo_opensearchserverless.types.policy_version.PolicyVersion"
    ]
    """<p>The version of the policy.</p>"""
    description: NotRequired[
        "capo_opensearchserverless.types.policy_description.PolicyDescription"
    ]
    """<p>The description of the policy.</p>"""
    policy: NotRequired["object"]
    """<p>The JSON policy document without any whitespaces.</p>"""
    created_date: NotRequired["int"]
    """<p>The date the policy was created.</p>"""
    last_modified_date: NotRequired["int"]
    """<p>The timestamp of when the policy was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessPolicyDetail) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "name" in value:
        out["name"] = value["name"]
    if "policy_version" in value:
        out["policyVersion"] = value["policy_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "created_date" in value:
        out["createdDate"] = value["created_date"]
    if "last_modified_date" in value:
        out["lastModifiedDate"] = value["last_modified_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessPolicyDetail:
    out: AccessPolicyDetail = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("policyVersion") is not None:
        out["policy_version"] = data["policyVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("createdDate") is not None:
        out["created_date"] = data["createdDate"]
    if data.get("lastModifiedDate") is not None:
        out["last_modified_date"] = data["lastModifiedDate"]
    return out
