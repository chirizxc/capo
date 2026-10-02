"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomTransformConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_transform_configuration

CustomTransformConfiguration = TypedDict(
    "CustomTransformConfiguration",
    {
        "lambda": NotRequired[
            "capo_bedrock_agentcore_control.types.lambda_transform_configuration.LambdaTransformConfiguration"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomTransformConfiguration) -> dict:
    out: dict = {}
    if "lambda" in value:
        import capo_bedrock_agentcore_control.types.lambda_transform_configuration

        out["lambda"] = (
            capo_bedrock_agentcore_control.types.lambda_transform_configuration.serialize_json(
                value["lambda"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomTransformConfiguration:
    out: CustomTransformConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("lambda") is not None:
        import capo_bedrock_agentcore_control.types.lambda_transform_configuration

        out["lambda"] = (
            capo_bedrock_agentcore_control.types.lambda_transform_configuration.deserialize_json(
                data["lambda"]
            )
        )
    return out
