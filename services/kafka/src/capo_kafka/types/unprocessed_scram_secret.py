"""Generated from Smithy shape ``com.amazonaws.kafka#UnprocessedScramSecret``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string


class UnprocessedScramSecret(TypedDict, closed=True):
    error_code: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Error code for associate/disassociate failure.</p>"""
    error_message: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Error message for associate/disassociate failure.</p>"""
    secret_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>AWS Secrets Manager secret ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedScramSecret) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> UnprocessedScramSecret:
    out: UnprocessedScramSecret = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    return out
