"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ForbiddenException``."""

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import ServiceError


class ForbiddenException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ForbiddenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ForbiddenException_:
    out: ForbiddenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ForbiddenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#ForbiddenException``."""

    code: str | None = "ForbiddenException"

    def __init__(self, data: ForbiddenException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ForbiddenException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ForbiddenException":
        return cls(deserialize_json(data), message)
