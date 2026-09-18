"""Generated from Smithy shape ``com.amazonaws.rdsdata#ServiceUnavailableError``."""

from typing_extensions import TypedDict

from capo_rds_data.errors import ServiceError


class ServiceUnavailableError_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableError_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ServiceUnavailableError_:
    out: ServiceUnavailableError_ = {}  # type: ignore[typeddict-item]
    return out


class ServiceUnavailableError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rdsdata#ServiceUnavailableError``."""

    code: str | None = "ServiceUnavailableError"

    def __init__(self, data: ServiceUnavailableError_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableError",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "ServiceUnavailableError":
        return cls(deserialize_json(data), message)
