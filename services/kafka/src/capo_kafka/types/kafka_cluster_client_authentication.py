"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterClientAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.kafka_cluster_mtls_authentication
    import capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication
    import capo_kafka.types.kafka_cluster_sasl_scram_authentication


class KafkaClusterClientAuthentication(TypedDict, closed=True):
    sasl_scram: NotRequired[
        "capo_kafka.types.kafka_cluster_sasl_scram_authentication.KafkaClusterSaslScramAuthentication"
    ]
    """<p>Details for SASL/SCRAM client authentication.</p>"""
    mtls: NotRequired[
        "capo_kafka.types.kafka_cluster_mtls_authentication.KafkaClusterMTLSAuthentication"
    ]
    """<p>Details for mTLS client authentication.</p>"""
    sasl_o_auth_bearer: NotRequired[
        "capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication.KafkaClusterSaslOAuthBearerAuthentication"
    ]
    """<p>Details for SASL/OAUTHBEARER client authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterClientAuthentication) -> dict:
    out: dict = {}
    if "sasl_scram" in value:
        import capo_kafka.types.kafka_cluster_sasl_scram_authentication

        out["saslScram"] = (
            capo_kafka.types.kafka_cluster_sasl_scram_authentication.serialize_json(
                value["sasl_scram"]
            )
        )
    if "mtls" in value:
        import capo_kafka.types.kafka_cluster_mtls_authentication

        out["mTLS"] = capo_kafka.types.kafka_cluster_mtls_authentication.serialize_json(
            value["mtls"]
        )
    if "sasl_o_auth_bearer" in value:
        import capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication

        out["saslOAuthBearer"] = (
            capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication.serialize_json(
                value["sasl_o_auth_bearer"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterClientAuthentication:
    out: KafkaClusterClientAuthentication = {}  # type: ignore[typeddict-item]
    if data.get("saslScram") is not None:
        import capo_kafka.types.kafka_cluster_sasl_scram_authentication

        out["sasl_scram"] = (
            capo_kafka.types.kafka_cluster_sasl_scram_authentication.deserialize_json(
                data["saslScram"]
            )
        )
    if data.get("mTLS") is not None:
        import capo_kafka.types.kafka_cluster_mtls_authentication

        out["mtls"] = (
            capo_kafka.types.kafka_cluster_mtls_authentication.deserialize_json(
                data["mTLS"]
            )
        )
    if data.get("saslOAuthBearer") is not None:
        import capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication

        out["sasl_o_auth_bearer"] = (
            capo_kafka.types.kafka_cluster_sasl_o_auth_bearer_authentication.deserialize_json(
                data["saslOAuthBearer"]
            )
        )
    return out
