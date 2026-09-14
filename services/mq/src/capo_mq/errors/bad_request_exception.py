"""Generated from Smithy shape ``com.amazonaws.mq#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mq.errors import ServiceError

if TYPE_CHECKING:
    import capo_mq.types.__string


class BadRequestException_(TypedDict, closed=True):
    error_attribute: NotRequired["capo_mq.types.__string.__string"]
    """<p>The attribute which caused the error.</p>"""
    message: NotRequired["capo_mq.types.__string.__string"]
    """<p>The explanation of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "error_attribute" in value:
        out["errorAttribute"] = value["error_attribute"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("errorAttribute") is not None:
        out["error_attribute"] = data["errorAttribute"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mq#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "BadRequestException":
        return cls(deserialize_json(data), message)
