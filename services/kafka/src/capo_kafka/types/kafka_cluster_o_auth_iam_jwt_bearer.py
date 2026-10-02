"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterOAuthIamJwtBearer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.jwt_signing_algorithm


class KafkaClusterOAuthIamJwtBearer(TypedDict, closed=True):
    audience: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The audience for the JWT Bearer assertion.</p>"""
    signing_algorithm: NotRequired[
        "capo_kafka.types.jwt_signing_algorithm.JwtSigningAlgorithm"
    ]
    """<p>The signing algorithm for the JWT Bearer assertion.</p>"""
    token_request_secret_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the signing key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterOAuthIamJwtBearer) -> dict:
    out: dict = {}
    if "audience" in value:
        out["audience"] = value["audience"]
    if "signing_algorithm" in value:
        import capo_kafka.types.jwt_signing_algorithm

        out["signingAlgorithm"] = capo_kafka.types.jwt_signing_algorithm.serialize_json(
            value["signing_algorithm"]
        )
    if "token_request_secret_arn" in value:
        out["tokenRequestSecretArn"] = value["token_request_secret_arn"]
    return out


def deserialize_json(data: dict) -> KafkaClusterOAuthIamJwtBearer:
    out: KafkaClusterOAuthIamJwtBearer = {}  # type: ignore[typeddict-item]
    if data.get("audience") is not None:
        out["audience"] = data["audience"]
    if data.get("signingAlgorithm") is not None:
        import capo_kafka.types.jwt_signing_algorithm

        out["signing_algorithm"] = (
            capo_kafka.types.jwt_signing_algorithm.deserialize_json(
                data["signingAlgorithm"]
            )
        )
    if data.get("tokenRequestSecretArn") is not None:
        out["token_request_secret_arn"] = data["tokenRequestSecretArn"]
    return out
