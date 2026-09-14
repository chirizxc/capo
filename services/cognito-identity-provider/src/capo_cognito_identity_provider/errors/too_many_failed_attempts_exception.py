"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TooManyFailedAttemptsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import ServiceError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.message_type


class TooManyFailedAttemptsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_cognito_identity_provider.types.message_type.MessageType"
    ]
    """<p>The message returned when Amazon Cognito returns a <code>TooManyFailedAttempts</code> exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TooManyFailedAttemptsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TooManyFailedAttemptsException_:
    out: TooManyFailedAttemptsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TooManyFailedAttemptsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cognitoidentityprovider#TooManyFailedAttemptsException``."""

    code: str | None = "TooManyFailedAttemptsException"

    def __init__(
        self, data: TooManyFailedAttemptsException_, message: str | None = None
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyFailedAttemptsException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "TooManyFailedAttemptsException":
        return cls(deserialize_aws_json_1_1(data), message)
