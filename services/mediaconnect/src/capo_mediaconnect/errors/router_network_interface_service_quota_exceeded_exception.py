"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceServiceQuotaExceededException``."""

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, ServiceError


class RouterNetworkInterfaceServiceQuotaExceededException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(
    data: dict,
) -> RouterNetworkInterfaceServiceQuotaExceededException_:
    out: RouterNetworkInterfaceServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "RouterNetworkInterfaceServiceQuotaExceededException_.message required"
        )
    return out


class RouterNetworkInterfaceServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceServiceQuotaExceededException``."""

    code: str | None = "RouterNetworkInterfaceServiceQuotaExceededException"

    def __init__(
        self,
        data: RouterNetworkInterfaceServiceQuotaExceededException_,
        message: str | None = None,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RouterNetworkInterfaceServiceQuotaExceededException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "RouterNetworkInterfaceServiceQuotaExceededException":
        return cls(deserialize_json(data), message)
