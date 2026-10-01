"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.workspace_encryption_configuration
    import capo_iotsitewise.types.workspace_name


class UpdateWorkspaceRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace to update.</p>"""
    workspace_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A new description for the workspace.</p>"""
    encryption_configuration: NotRequired[
        "capo_iotsitewise.types.workspace_encryption_configuration.WorkspaceEncryptionConfiguration"
    ]
    """<p>The encryption configuration for the workspace. Omit this field to leave encryption unchanged. After a customer managed key configuration becomes active, the key can't be changed; supplying the same key is accepted.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceRequest) -> dict:
    out: dict = {}
    if "workspace_description" in value:
        out["workspaceDescription"] = value["workspace_description"]
    if "encryption_configuration" in value:
        import capo_iotsitewise.types.workspace_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_iotsitewise.types.workspace_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceRequest:
    out: UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceDescription") is not None:
        out["workspace_description"] = data["workspaceDescription"]
    if data.get("encryptionConfiguration") is not None:
        import capo_iotsitewise.types.workspace_encryption_configuration

        out["encryption_configuration"] = (
            capo_iotsitewise.types.workspace_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
