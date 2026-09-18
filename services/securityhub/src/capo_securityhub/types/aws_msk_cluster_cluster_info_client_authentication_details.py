"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details
    import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details


class AwsMskClusterClusterInfoClientAuthenticationDetails(TypedDict, closed=True):
    sasl: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.AwsMskClusterClusterInfoClientAuthenticationSaslDetails"
    ]
    """<p> Provides details for client authentication using SASL.</p>"""
    unauthenticated: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails"
    ]
    """<p> Provides details for allowing no client authentication.</p>"""
    tls: NotRequired[
        "capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.AwsMskClusterClusterInfoClientAuthenticationTlsDetails"
    ]
    """<p> Provides details for client authentication using TLS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterClusterInfoClientAuthenticationDetails) -> dict:
    out: dict = {}
    if "sasl" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details

        out["Sasl"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.serialize_json(
                value["sasl"]
            )
        )
    if "unauthenticated" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details

        out["Unauthenticated"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.serialize_json(
                value["unauthenticated"]
            )
        )
    if "tls" in value:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details

        out["Tls"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.serialize_json(
                value["tls"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsMskClusterClusterInfoClientAuthenticationDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationDetails = {}  # type: ignore[typeddict-item]
    if data.get("Sasl") is not None:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details

        out["sasl"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_sasl_details.deserialize_json(
                data["Sasl"]
            )
        )
    if data.get("Unauthenticated") is not None:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details

        out["unauthenticated"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_unauthenticated_details.deserialize_json(
                data["Unauthenticated"]
            )
        )
    if data.get("Tls") is not None:
        import capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details

        out["tls"] = (
            capo_securityhub.types.aws_msk_cluster_cluster_info_client_authentication_tls_details.deserialize_json(
                data["Tls"]
            )
        )
    return out
