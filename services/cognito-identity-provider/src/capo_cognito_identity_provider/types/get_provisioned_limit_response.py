"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetProvisionedLimitResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.limit_type


class GetProvisionedLimitResponse(TypedDict, closed=True):
    limit: "capo_cognito_identity_provider.types.limit_type.LimitType"
    """<p>The provisioned and default limit values for the requested limit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProvisionedLimitResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.limit_type

    out["Limit"] = (
        capo_cognito_identity_provider.types.limit_type.serialize_aws_json_1_1(
            value["limit"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProvisionedLimitResponse:
    out: GetProvisionedLimitResponse = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        import capo_cognito_identity_provider.types.limit_type

        out["limit"] = (
            capo_cognito_identity_provider.types.limit_type.deserialize_aws_json_1_1(
                data["Limit"]
            )
        )
    else:
        raise DeserializationError("GetProvisionedLimitResponse.limit required")
    return out
