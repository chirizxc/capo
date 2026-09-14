"""Generated from Smithy shape ``com.amazonaws.snowball#ReturnShippingLabelAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class ReturnShippingLabelAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReturnShippingLabelAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReturnShippingLabelAlreadyExistsException_:
    out: ReturnShippingLabelAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ReturnShippingLabelAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#ReturnShippingLabelAlreadyExistsException``."""

    code: str | None = "ReturnShippingLabelAlreadyExistsException"

    def __init__(
        self,
        data: ReturnShippingLabelAlreadyExistsException_,
        message: str | None = None,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReturnShippingLabelAlreadyExistsException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ReturnShippingLabelAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data), message)
