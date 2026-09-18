"""Generated from Smithy shape ``com.amazonaws.opensearch#CognitoOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.identity_pool_id
    import capo_opensearch.types.role_arn
    import capo_opensearch.types.user_pool_id


class CognitoOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether to enable or disable Amazon Cognito authentication for OpenSearch Dashboards.</p>"""
    user_pool_id: NotRequired["capo_opensearch.types.user_pool_id.UserPoolId"]
    """<p>The Amazon Cognito user pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.</p>"""
    identity_pool_id: NotRequired[
        "capo_opensearch.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>The Amazon Cognito identity pool ID that you want OpenSearch Service to use for OpenSearch Dashboards authentication.</p>"""
    role_arn: NotRequired["capo_opensearch.types.role_arn.RoleArn"]
    """<p>The <code>AmazonOpenSearchServiceCognitoAccess</code> role that allows OpenSearch Service to configure your user pool and identity pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CognitoOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CognitoOptions:
    out: CognitoOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
