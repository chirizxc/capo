"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetProvisionedLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.limit_definition_type


class GetProvisionedLimitRequest(TypedDict, closed=True):
    limit_definition: (
        "capo_cognito_identity_provider.types.limit_definition_type.LimitDefinitionType"
    )
    """<p>The limit to retrieve. Specify the limit class and the attributes that identify the limit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProvisionedLimitRequest) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.limit_definition_type

    out["LimitDefinition"] = (
        capo_cognito_identity_provider.types.limit_definition_type.serialize_aws_json_1_1(
            value["limit_definition"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProvisionedLimitRequest:
    out: GetProvisionedLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("LimitDefinition") is not None:
        import capo_cognito_identity_provider.types.limit_definition_type

        out["limit_definition"] = (
            capo_cognito_identity_provider.types.limit_definition_type.deserialize_aws_json_1_1(
                data["LimitDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "GetProvisionedLimitRequest.limit_definition required"
        )
    return out
