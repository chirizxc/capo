"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdateDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.expression
    import capo_iot_wireless.types.expression_type
    import capo_iot_wireless.types.role_arn


class UpdateDestinationRequest(TypedDict, closed=True):
    name: "capo_iot_wireless.types.destination_name.DestinationName"
    """<p>The new name of the resource.</p>"""
    expression_type: NotRequired[
        "capo_iot_wireless.types.expression_type.ExpressionType"
    ]
    """<p>The type of value in <code>Expression</code>.</p>"""
    expression: NotRequired["capo_iot_wireless.types.expression.Expression"]
    """<p>The new rule name or topic rule to send messages to.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>A new description of the resource.</p>"""
    role_arn: NotRequired["capo_iot_wireless.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDestinationRequest) -> dict:
    out: dict = {}
    if "expression_type" in value:
        import capo_iot_wireless.types.expression_type

        out["ExpressionType"] = capo_iot_wireless.types.expression_type.serialize_json(
            value["expression_type"]
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateDestinationRequest:
    out: UpdateDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExpressionType") is not None:
        import capo_iot_wireless.types.expression_type

        out["expression_type"] = (
            capo_iot_wireless.types.expression_type.deserialize_json(
                data["ExpressionType"]
            )
        )
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
