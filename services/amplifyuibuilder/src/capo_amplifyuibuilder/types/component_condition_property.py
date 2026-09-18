"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentConditionProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.component_property

ComponentConditionProperty = TypedDict(
    "ComponentConditionProperty",
    {
        "property": NotRequired["str"],
        "field": NotRequired["str"],
        "operator": NotRequired["str"],
        "operand": NotRequired["str"],
        "then": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "else": NotRequired[
            "capo_amplifyuibuilder.types.component_property.ComponentProperty"
        ],
        "operand_type": NotRequired["str"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConditionProperty) -> dict:
    out: dict = {}
    if "property" in value:
        out["property"] = value["property"]
    if "field" in value:
        out["field"] = value["field"]
    if "operator" in value:
        out["operator"] = value["operator"]
    if "operand" in value:
        out["operand"] = value["operand"]
    if "then" in value:
        import capo_amplifyuibuilder.types.component_property

        out["then"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["then"]
        )
    if "else" in value:
        import capo_amplifyuibuilder.types.component_property

        out["else"] = capo_amplifyuibuilder.types.component_property.serialize_json(
            value["else"]
        )
    if "operand_type" in value:
        out["operandType"] = value["operand_type"]
    return out


def deserialize_json(data: dict) -> ComponentConditionProperty:
    out: ComponentConditionProperty = {}  # type: ignore[typeddict-item]
    if data.get("property") is not None:
        out["property"] = data["property"]
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    if data.get("operand") is not None:
        out["operand"] = data["operand"]
    if data.get("then") is not None:
        import capo_amplifyuibuilder.types.component_property

        out["then"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["then"]
        )
    if data.get("else") is not None:
        import capo_amplifyuibuilder.types.component_property

        out["else"] = capo_amplifyuibuilder.types.component_property.deserialize_json(
            data["else"]
        )
    if data.get("operandType") is not None:
        out["operand_type"] = data["operandType"]
    return out
