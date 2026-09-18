"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_arn
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.expression
    import capo_iot_wireless.types.expression_type
    import capo_iot_wireless.types.role_arn


class GetDestinationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""
    name: NotRequired["capo_iot_wireless.types.destination_name.DestinationName"]
    """<p>The name of the resource.</p>"""
    expression: NotRequired["capo_iot_wireless.types.expression.Expression"]
    """<p>The rule name or topic rule to send messages to.</p>"""
    expression_type: NotRequired[
        "capo_iot_wireless.types.expression_type.ExpressionType"
    ]
    """<p>The type of value in <code>Expression</code>.</p>"""
    description: NotRequired["capo_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    role_arn: NotRequired["capo_iot_wireless.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM Role that authorizes the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDestinationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "expression_type" in value:
        import capo_iot_wireless.types.expression_type

        out["ExpressionType"] = capo_iot_wireless.types.expression_type.serialize_json(
            value["expression_type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetDestinationResponse:
    out: GetDestinationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("ExpressionType") is not None:
        import capo_iot_wireless.types.expression_type

        out["expression_type"] = (
            capo_iot_wireless.types.expression_type.deserialize_json(
                data["ExpressionType"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
