"""Generated from Smithy shape ``com.amazonaws.opensearch#JWTOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.jwks_url
    import capo_opensearch.types.string


class JWTOptionsOutput(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True if JWT use is enabled.</p>"""
    subject_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>The key used for matching the JWT subject attribute.</p>"""
    roles_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>The key used for matching the JWT roles attribute.</p>"""
    jwks_url: NotRequired["capo_opensearch.types.jwks_url.JwksUrl"]
    """<p>The configured JWKS URL endpoint from which the cluster retrieves public keys to verify JWT requests.</p>"""
    public_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>The key used to verify the signature of incoming JWT requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JWTOptionsOutput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    if "jwks_url" in value:
        out["JwksUrl"] = value["jwks_url"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    return out


def deserialize_json(data: dict) -> JWTOptionsOutput:
    out: JWTOptionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SubjectKey") is not None:
        out["subject_key"] = data["SubjectKey"]
    if data.get("RolesKey") is not None:
        out["roles_key"] = data["RolesKey"]
    if data.get("JwksUrl") is not None:
        out["jwks_url"] = data["JwksUrl"]
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    return out
