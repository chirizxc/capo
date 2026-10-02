"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterMTLSAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class KafkaClusterMTLSAuthentication(TypedDict, closed=True):
    secret_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterMTLSAuthentication) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> KafkaClusterMTLSAuthentication:
    out: KafkaClusterMTLSAuthentication = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    return out
