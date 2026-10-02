"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterOAuthClientCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class KafkaClusterOAuthClientCredentials(TypedDict, closed=True):
    token_request_secret_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret containing the OAuth client credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterOAuthClientCredentials) -> dict:
    out: dict = {}
    if "token_request_secret_arn" in value:
        out["tokenRequestSecretArn"] = value["token_request_secret_arn"]
    return out


def deserialize_json(data: dict) -> KafkaClusterOAuthClientCredentials:
    out: KafkaClusterOAuthClientCredentials = {}  # type: ignore[typeddict-item]
    if data.get("tokenRequestSecretArn") is not None:
        out["token_request_secret_arn"] = data["tokenRequestSecretArn"]
    return out
