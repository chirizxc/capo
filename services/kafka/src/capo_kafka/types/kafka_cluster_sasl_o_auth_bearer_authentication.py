"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterSaslOAuthBearerAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.kafka_cluster_o_auth_client_credentials
    import capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion
    import capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer
    import capo_kafka.types.token_endpoint_authentication_method


class KafkaClusterSaslOAuthBearerAuthentication(TypedDict, closed=True):
    token_endpoint_url: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The HTTPS URL of the OAuth token endpoint that vends OAuth Bearer tokens per RFC 6749.</p>"""
    client_credentials: NotRequired[
        "capo_kafka.types.kafka_cluster_o_auth_client_credentials.KafkaClusterOAuthClientCredentials"
    ]
    """<p>Details for SASL/OAUTHBEARER using standard client_credentials grant.</p>"""
    iam_jwt_bearer: NotRequired[
        "capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer.KafkaClusterOAuthIamJwtBearer"
    ]
    """<p>Details for SASL/OAUTHBEARER using JWT Bearer assertion grant (RFC 7523).</p>"""
    client_credentials_assertion: NotRequired[
        "capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion.KafkaClusterOAuthClientCredentialsAssertion"
    ]
    """<p>Details for SASL/OAUTHBEARER using client credentials grant with JWT client assertion.</p>"""
    token_endpoint_authentication_method: NotRequired[
        "capo_kafka.types.token_endpoint_authentication_method.TokenEndpointAuthenticationMethod"
    ]
    """<p>How client credentials are sent to the identity provider. Valid values are POST, BASIC, or NONE.</p>"""
    scope: NotRequired["capo_kafka.types.__string.__string"]
    """<p>OAuth scope to request.</p>"""
    token_endpoint_tls_certificate_arn: NotRequired[
        "capo_kafka.types.__string.__string"
    ]
    """<p>Secrets Manager ARN containing a custom CA certificate for the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterSaslOAuthBearerAuthentication) -> dict:
    out: dict = {}
    if "token_endpoint_url" in value:
        out["tokenEndpointUrl"] = value["token_endpoint_url"]
    if "client_credentials" in value:
        import capo_kafka.types.kafka_cluster_o_auth_client_credentials

        out["clientCredentials"] = (
            capo_kafka.types.kafka_cluster_o_auth_client_credentials.serialize_json(
                value["client_credentials"]
            )
        )
    if "iam_jwt_bearer" in value:
        import capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer

        out["iamJwtBearer"] = (
            capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer.serialize_json(
                value["iam_jwt_bearer"]
            )
        )
    if "client_credentials_assertion" in value:
        import capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion

        out["clientCredentialsAssertion"] = (
            capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion.serialize_json(
                value["client_credentials_assertion"]
            )
        )
    if "token_endpoint_authentication_method" in value:
        import capo_kafka.types.token_endpoint_authentication_method

        out["tokenEndpointAuthenticationMethod"] = (
            capo_kafka.types.token_endpoint_authentication_method.serialize_json(
                value["token_endpoint_authentication_method"]
            )
        )
    if "scope" in value:
        out["scope"] = value["scope"]
    if "token_endpoint_tls_certificate_arn" in value:
        out["tokenEndpointTlsCertificateArn"] = value[
            "token_endpoint_tls_certificate_arn"
        ]
    return out


def deserialize_json(data: dict) -> KafkaClusterSaslOAuthBearerAuthentication:
    out: KafkaClusterSaslOAuthBearerAuthentication = {}  # type: ignore[typeddict-item]
    if data.get("tokenEndpointUrl") is not None:
        out["token_endpoint_url"] = data["tokenEndpointUrl"]
    if data.get("clientCredentials") is not None:
        import capo_kafka.types.kafka_cluster_o_auth_client_credentials

        out["client_credentials"] = (
            capo_kafka.types.kafka_cluster_o_auth_client_credentials.deserialize_json(
                data["clientCredentials"]
            )
        )
    if data.get("iamJwtBearer") is not None:
        import capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer

        out["iam_jwt_bearer"] = (
            capo_kafka.types.kafka_cluster_o_auth_iam_jwt_bearer.deserialize_json(
                data["iamJwtBearer"]
            )
        )
    if data.get("clientCredentialsAssertion") is not None:
        import capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion

        out["client_credentials_assertion"] = (
            capo_kafka.types.kafka_cluster_o_auth_client_credentials_assertion.deserialize_json(
                data["clientCredentialsAssertion"]
            )
        )
    if data.get("tokenEndpointAuthenticationMethod") is not None:
        import capo_kafka.types.token_endpoint_authentication_method

        out["token_endpoint_authentication_method"] = (
            capo_kafka.types.token_endpoint_authentication_method.deserialize_json(
                data["tokenEndpointAuthenticationMethod"]
            )
        )
    if data.get("scope") is not None:
        out["scope"] = data["scope"]
    if data.get("tokenEndpointTlsCertificateArn") is not None:
        out["token_endpoint_tls_certificate_arn"] = data[
            "tokenEndpointTlsCertificateArn"
        ]
    return out
