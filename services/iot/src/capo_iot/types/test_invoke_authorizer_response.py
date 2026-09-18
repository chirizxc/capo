"""Generated from Smithy shape ``com.amazonaws.iot#TestInvokeAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.is_authenticated
    import capo_iot.types.policy_documents
    import capo_iot.types.principal_id
    import capo_iot.types.seconds


class TestInvokeAuthorizerResponse(TypedDict, closed=True):
    is_authenticated: NotRequired["capo_iot.types.is_authenticated.IsAuthenticated"]
    """<p>True if the token is authenticated, otherwise false.</p>"""
    principal_id: NotRequired["capo_iot.types.principal_id.PrincipalId"]
    """<p>The principal ID.</p>"""
    policy_documents: NotRequired["capo_iot.types.policy_documents.PolicyDocuments"]
    """<p>IAM policy documents.</p>"""
    refresh_after_in_seconds: NotRequired["capo_iot.types.seconds.Seconds"]
    """<p>The number of seconds after which the temporary credentials are refreshed.</p>"""
    disconnect_after_in_seconds: NotRequired["capo_iot.types.seconds.Seconds"]
    """<p>The number of seconds after which the connection is terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestInvokeAuthorizerResponse) -> dict:
    out: dict = {}
    if "is_authenticated" in value:
        out["isAuthenticated"] = value["is_authenticated"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "policy_documents" in value:
        import capo_iot.types.policy_documents

        out["policyDocuments"] = capo_iot.types.policy_documents.serialize_json(
            value["policy_documents"]
        )
    if "refresh_after_in_seconds" in value:
        out["refreshAfterInSeconds"] = value["refresh_after_in_seconds"]
    if "disconnect_after_in_seconds" in value:
        out["disconnectAfterInSeconds"] = value["disconnect_after_in_seconds"]
    return out


def deserialize_json(data: dict) -> TestInvokeAuthorizerResponse:
    out: TestInvokeAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if data.get("isAuthenticated") is not None:
        out["is_authenticated"] = data["isAuthenticated"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("policyDocuments") is not None:
        import capo_iot.types.policy_documents

        out["policy_documents"] = capo_iot.types.policy_documents.deserialize_json(
            data["policyDocuments"]
        )
    if data.get("refreshAfterInSeconds") is not None:
        out["refresh_after_in_seconds"] = data["refreshAfterInSeconds"]
    if data.get("disconnectAfterInSeconds") is not None:
        out["disconnect_after_in_seconds"] = data["disconnectAfterInSeconds"]
    return out
