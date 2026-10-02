"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LambdaTransformConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.lambda_function_arn


class LambdaTransformConfiguration(TypedDict, closed=True):
    arn: NotRequired[
        "capo_bedrock_agentcore_control.types.lambda_function_arn.LambdaFunctionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to transform data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaTransformConfiguration) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaTransformConfiguration:
    out: LambdaTransformConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
