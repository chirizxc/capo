"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#Predicate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.operand_type
    import capo_amplifyuibuilder.types.predicate_list

Predicate = TypedDict(
    "Predicate",
    {
        "or": NotRequired["capo_amplifyuibuilder.types.predicate_list.PredicateList"],
        "and": NotRequired["capo_amplifyuibuilder.types.predicate_list.PredicateList"],
        "field": NotRequired["str"],
        "operator": NotRequired["str"],
        "operand": NotRequired["str"],
        "operand_type": NotRequired[
            "capo_amplifyuibuilder.types.operand_type.OperandType"
        ],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: Predicate) -> dict:
    out: dict = {}
    if "or" in value:
        import capo_amplifyuibuilder.types.predicate_list

        out["or"] = capo_amplifyuibuilder.types.predicate_list.serialize_json(
            value["or"]
        )
    if "and" in value:
        import capo_amplifyuibuilder.types.predicate_list

        out["and"] = capo_amplifyuibuilder.types.predicate_list.serialize_json(
            value["and"]
        )
    if "field" in value:
        out["field"] = value["field"]
    if "operator" in value:
        out["operator"] = value["operator"]
    if "operand" in value:
        out["operand"] = value["operand"]
    if "operand_type" in value:
        out["operandType"] = value["operand_type"]
    return out


def deserialize_json(data: dict) -> Predicate:
    out: Predicate = {}  # type: ignore[typeddict-item]
    if data.get("or") is not None:
        import capo_amplifyuibuilder.types.predicate_list

        out["or"] = capo_amplifyuibuilder.types.predicate_list.deserialize_json(
            data["or"]
        )
    if data.get("and") is not None:
        import capo_amplifyuibuilder.types.predicate_list

        out["and"] = capo_amplifyuibuilder.types.predicate_list.deserialize_json(
            data["and"]
        )
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    if data.get("operand") is not None:
        out["operand"] = data["operand"]
    if data.get("operandType") is not None:
        out["operand_type"] = data["operandType"]
    return out
