"""Generated from Smithy shape ``com.amazonaws.appmesh#ClientPolicyTls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.client_tls_certificate
    import capo_app_mesh.types.port_set
    import capo_app_mesh.types.tls_validation_context


class ClientPolicyTls(TypedDict, closed=True):
    enforce: NotRequired["bool"]
    """<p>Whether the policy is enforced. The default is <code>True</code>, if a value isn't specified.</p>"""
    ports: NotRequired["capo_app_mesh.types.port_set.PortSet"]
    """<p>One or more ports that the policy is enforced for.</p>"""
    certificate: NotRequired[
        "capo_app_mesh.types.client_tls_certificate.ClientTlsCertificate"
    ]
    """<p>A reference to an object that represents a client's TLS certificate.</p>"""
    validation: "capo_app_mesh.types.tls_validation_context.TlsValidationContext"
    """<p>A reference to an object that represents a TLS validation context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientPolicyTls) -> dict:
    out: dict = {}
    if "enforce" in value:
        out["enforce"] = value["enforce"]
    if "ports" in value:
        import capo_app_mesh.types.port_set

        out["ports"] = capo_app_mesh.types.port_set.serialize_json(value["ports"])
    if "certificate" in value:
        import capo_app_mesh.types.client_tls_certificate

        out["certificate"] = capo_app_mesh.types.client_tls_certificate.serialize_json(
            value["certificate"]
        )
    import capo_app_mesh.types.tls_validation_context

    out["validation"] = capo_app_mesh.types.tls_validation_context.serialize_json(
        value["validation"]
    )
    return out


def deserialize_json(data: dict) -> ClientPolicyTls:
    out: ClientPolicyTls = {}  # type: ignore[typeddict-item]
    if data.get("enforce") is not None:
        out["enforce"] = data["enforce"]
    if data.get("ports") is not None:
        import capo_app_mesh.types.port_set

        out["ports"] = capo_app_mesh.types.port_set.deserialize_json(data["ports"])
    if data.get("certificate") is not None:
        import capo_app_mesh.types.client_tls_certificate

        out["certificate"] = (
            capo_app_mesh.types.client_tls_certificate.deserialize_json(
                data["certificate"]
            )
        )
    if data.get("validation") is not None:
        import capo_app_mesh.types.tls_validation_context

        out["validation"] = capo_app_mesh.types.tls_validation_context.deserialize_json(
            data["validation"]
        )
    else:
        raise DeserializationError("ClientPolicyTls.validation required")
    return out
