"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchDeleteError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.batch_delete_error_code


class BatchDeleteError(TypedDict, closed=True):
    resource_arn: "str"
    """ARN of the configuration that failed to delete."""
    code: "capo_application_signals.types.batch_delete_error_code.BatchDeleteErrorCode"
    """Error code indicating the type of failure."""
    message: "str"
    """Descriptive error message."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteError) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_application_signals.types.batch_delete_error_code

    out["Code"] = capo_application_signals.types.batch_delete_error_code.serialize_json(
        value["code"]
    )
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteError:
    out: BatchDeleteError = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("BatchDeleteError.resource_arn required")
    if data.get("Code") is not None:
        import capo_application_signals.types.batch_delete_error_code

        out["code"] = (
            capo_application_signals.types.batch_delete_error_code.deserialize_json(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteError.code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("BatchDeleteError.message required")
    return out
