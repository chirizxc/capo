"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#InvalidStateException``."""

from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import ServiceError


class InvalidStateException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridgev2#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None
    ) -> "InvalidStateException":
        return cls(deserialize_cbor(data), message)
