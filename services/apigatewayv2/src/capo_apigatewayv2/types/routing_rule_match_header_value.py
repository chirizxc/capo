"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#RoutingRuleMatchHeaderValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.selection_expression
    import capo_apigatewayv2.types.selection_key


class RoutingRuleMatchHeaderValue(TypedDict, closed=True):
    header: NotRequired["capo_apigatewayv2.types.selection_key.SelectionKey"]
    value_glob: NotRequired[
        "capo_apigatewayv2.types.selection_expression.SelectionExpression"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingRuleMatchHeaderValue) -> dict:
    out: dict = {}
    if "header" in value:
        out["header"] = value["header"]
    if "value_glob" in value:
        out["valueGlob"] = value["value_glob"]
    return out


def deserialize_json(data: dict) -> RoutingRuleMatchHeaderValue:
    out: RoutingRuleMatchHeaderValue = {}  # type: ignore[typeddict-item]
    if data.get("header") is not None:
        out["header"] = data["header"]
    if data.get("valueGlob") is not None:
        out["value_glob"] = data["valueGlob"]
    return out
