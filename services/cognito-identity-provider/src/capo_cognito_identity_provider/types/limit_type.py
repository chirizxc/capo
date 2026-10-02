"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LimitType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.limit_definition_type


class LimitType(TypedDict, closed=True):
    limit_definition: (
        "capo_cognito_identity_provider.types.limit_definition_type.LimitDefinitionType"
    )
    """<p>The definition that identifies this limit, including the class and attributes.</p>"""
    provisioned_limit_value: (
        "capo_cognito_identity_provider.types.integer_type.IntegerType"
    )
    """<p>The provisioned limit value, in requests per second (RPS). This is the rate that Amazon Cognito currently enforces for your account.</p>"""
    free_limit_value: "capo_cognito_identity_provider.types.integer_type.IntegerType"
    """<p>The default (free) limit value, in requests per second (RPS). This is the rate included at no additional cost.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LimitType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.limit_definition_type

    out["LimitDefinition"] = (
        capo_cognito_identity_provider.types.limit_definition_type.serialize_aws_json_1_1(
            value["limit_definition"]
        )
    )
    out["ProvisionedLimitValue"] = value.get("provisioned_limit_value", 0)
    out["FreeLimitValue"] = value.get("free_limit_value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LimitType:
    out: LimitType = {}  # type: ignore[typeddict-item]
    if data.get("LimitDefinition") is not None:
        import capo_cognito_identity_provider.types.limit_definition_type

        out["limit_definition"] = (
            capo_cognito_identity_provider.types.limit_definition_type.deserialize_aws_json_1_1(
                data["LimitDefinition"]
            )
        )
    else:
        raise DeserializationError("LimitType.limit_definition required")
    if data.get("ProvisionedLimitValue") is not None:
        out["provisioned_limit_value"] = data["ProvisionedLimitValue"]
    else:
        out["provisioned_limit_value"] = 0
    if data.get("FreeLimitValue") is not None:
        out["free_limit_value"] = data["FreeLimitValue"]
    else:
        out["free_limit_value"] = 0
    return out
