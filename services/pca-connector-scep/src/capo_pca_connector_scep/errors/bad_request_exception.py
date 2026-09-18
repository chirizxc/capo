"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#BadRequestException``."""

from typing_extensions import TypedDict

from capo_pca_connector_scep.errors import DeserializationError, ServiceError


class BadRequestException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("BadRequestException_.message required")
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.pcaconnectorscep#BadRequestException``."""

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
