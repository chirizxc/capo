"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BadRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import ServiceError

if TYPE_CHECKING:
    import capo_customer_profiles.types.message


class BadRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_customer_profiles.types.message.message"]


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.customerprofiles#BadRequestException``."""

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
