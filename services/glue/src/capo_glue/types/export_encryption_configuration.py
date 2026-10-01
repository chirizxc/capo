"""Generated from Smithy shape ``com.amazonaws.glue#ExportEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.kms_key_arn_string
    import capo_glue.types.sse_algorithm


class ExportEncryptionConfiguration(TypedDict, closed=True):
    sse_algorithm: NotRequired["capo_glue.types.sse_algorithm.SseAlgorithm"]
    """<p>The server-side encryption algorithm used for the exported data. Valid values are <code>AES256</code> and <code>aws:kms</code>.</p>"""
    kms_key_arn: NotRequired["capo_glue.types.kms_key_arn_string.KmsKeyArnString"]
    """<p>The ARN of the KMS key used to encrypt the exported data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportEncryptionConfiguration) -> dict:
    out: dict = {}
    if "sse_algorithm" in value:
        out["SseAlgorithm"] = value["sse_algorithm"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportEncryptionConfiguration:
    out: ExportEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SseAlgorithm") is not None:
        out["sse_algorithm"] = data["SseAlgorithm"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
