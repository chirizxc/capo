"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewHealthStatusException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_billing.types.error_message


class BillingViewHealthStatusException_(TypedDict, closed=True):
    message: "capo_billing.types.error_message.ErrorMessage"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewHealthStatusException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewHealthStatusException_:
    out: BillingViewHealthStatusException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BillingViewHealthStatusException_.message required")
    return out


class BillingViewHealthStatusException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billing#BillingViewHealthStatusException``."""

    code: str | None = "BillingViewHealthStatusException"

    def __init__(
        self, data: BillingViewHealthStatusException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BillingViewHealthStatusException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None
    ) -> "BillingViewHealthStatusException":
        return cls(deserialize_aws_json_1_0(data), message)
