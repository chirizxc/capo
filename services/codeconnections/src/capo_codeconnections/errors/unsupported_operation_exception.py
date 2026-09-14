"""Generated from Smithy shape ``com.amazonaws.codeconnections#UnsupportedOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import capo_codeconnections.types.error_message


class UnsupportedOperationException_(TypedDict, closed=True):
    message: NotRequired["capo_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedOperationException_:
    out: UnsupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class UnsupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#UnsupportedOperationException``."""

    code: str | None = "UnsupportedOperationException"

    def __init__(
        self, data: UnsupportedOperationException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedOperationException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "UnsupportedOperationException":
        return cls(deserialize_aws_json_1_0(data), message)
