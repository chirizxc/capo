"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#LimitExceededException``."""

from typing_extensions import TypedDict

from capo_apigatewaymanagementapi.errors import ServiceError


class LimitExceededException_(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.apigatewaymanagementapi#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "LimitExceededException":
        return cls(deserialize_json(data), message)
