"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PutIntelligenceConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.intelligence_kms_key_arn


class PutIntelligenceConfigurationInput(TypedDict, closed=True):
    kms_key_arn: NotRequired[
        "capo_cloudwatchomni.types.intelligence_kms_key_arn.IntelligenceKmsKeyArn"
    ]
    """Optional KMS key ARN to configure customer-managed encryption for anomaly data."""
    remove_kms_key: NotRequired["bool"]
    """Set to true to disassociate the configured KMS key. Mutually exclusive with kmsKeyArn; the service returns ValidationException if both are provided."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeating a request with the same token applies the update at most once instead of reprocessing it."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PutIntelligenceConfigurationInput) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "remove_kms_key" in value:
        out["removeKmsKey"] = value["remove_kms_key"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> PutIntelligenceConfigurationInput:
    out: PutIntelligenceConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("removeKmsKey") is not None:
        out["remove_kms_key"] = data["removeKmsKey"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
