"""Generated from Smithy shape ``com.amazonaws.servicequotas#AWSServiceAccessNotEnabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import capo_service_quotas.types.exception_message


class AWSServiceAccessNotEnabledException_(TypedDict, closed=True):
    message: NotRequired["capo_service_quotas.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AWSServiceAccessNotEnabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AWSServiceAccessNotEnabledException_:
    out: AWSServiceAccessNotEnabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class AWSServiceAccessNotEnabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#AWSServiceAccessNotEnabledException``."""

    code: str | None = "AWSServiceAccessNotEnabledException"

    def __init__(
        self, data: AWSServiceAccessNotEnabledException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AWSServiceAccessNotEnabledException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "AWSServiceAccessNotEnabledException":
        return cls(deserialize_aws_json_1_1(data), message)
