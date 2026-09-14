"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.data_value_list
    import capo_iottwinmaker.types.data_value_map
    import capo_iottwinmaker.types.double
    import capo_iottwinmaker.types.expression
    import capo_iottwinmaker.types.integer
    import capo_iottwinmaker.types.long
    import capo_iottwinmaker.types.relationship_value
    import capo_iottwinmaker.types.string


class DataValue(TypedDict, closed=True):
    boolean_value: NotRequired["capo_iottwinmaker.types.boolean.Boolean"]
    """<p>A Boolean value.</p>"""
    double_value: NotRequired["capo_iottwinmaker.types.double.Double"]
    """<p>A double value.</p>"""
    integer_value: NotRequired["capo_iottwinmaker.types.integer.Integer"]
    """<p>An integer value.</p>"""
    long_value: NotRequired["capo_iottwinmaker.types.long.Long"]
    """<p>A long value.</p>"""
    string_value: NotRequired["capo_iottwinmaker.types.string.String"]
    """<p>A string value.</p>"""
    list_value: NotRequired["capo_iottwinmaker.types.data_value_list.DataValueList"]
    """<p>A list of multiple values.</p>"""
    map_value: NotRequired["capo_iottwinmaker.types.data_value_map.DataValueMap"]
    """<p>An object that maps strings to multiple <code>DataValue</code> objects.</p>"""
    relationship_value: NotRequired[
        "capo_iottwinmaker.types.relationship_value.RelationshipValue"
    ]
    """<p>A value that relates a component to another component.</p>"""
    expression: NotRequired["capo_iottwinmaker.types.expression.Expression"]
    """<p>An expression that produces the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataValue) -> dict:
    out: dict = {}
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "double_value" in value:
        out["doubleValue"] = (
            "NaN"
            if value["double_value"] != value["double_value"]
            else "Infinity"
            if value["double_value"] == float("inf")
            else "-Infinity"
            if value["double_value"] == float("-inf")
            else value["double_value"]
        )
    if "integer_value" in value:
        out["integerValue"] = value["integer_value"]
    if "long_value" in value:
        out["longValue"] = value["long_value"]
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "list_value" in value:
        import capo_iottwinmaker.types.data_value_list

        out["listValue"] = capo_iottwinmaker.types.data_value_list.serialize_json(
            value["list_value"]
        )
    if "map_value" in value:
        import capo_iottwinmaker.types.data_value_map

        out["mapValue"] = capo_iottwinmaker.types.data_value_map.serialize_json(
            value["map_value"]
        )
    if "relationship_value" in value:
        import capo_iottwinmaker.types.relationship_value

        out["relationshipValue"] = (
            capo_iottwinmaker.types.relationship_value.serialize_json(
                value["relationship_value"]
            )
        )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> DataValue:
    out: DataValue = {}  # type: ignore[typeddict-item]
    if data.get("booleanValue") is not None:
        out["boolean_value"] = data["booleanValue"]
    if data.get("doubleValue") is not None:
        out["double_value"] = float(data["doubleValue"])
    if data.get("integerValue") is not None:
        out["integer_value"] = data["integerValue"]
    if data.get("longValue") is not None:
        out["long_value"] = data["longValue"]
    if data.get("stringValue") is not None:
        out["string_value"] = data["stringValue"]
    if data.get("listValue") is not None:
        import capo_iottwinmaker.types.data_value_list

        out["list_value"] = capo_iottwinmaker.types.data_value_list.deserialize_json(
            data["listValue"]
        )
    if data.get("mapValue") is not None:
        import capo_iottwinmaker.types.data_value_map

        out["map_value"] = capo_iottwinmaker.types.data_value_map.deserialize_json(
            data["mapValue"]
        )
    if data.get("relationshipValue") is not None:
        import capo_iottwinmaker.types.relationship_value

        out["relationship_value"] = (
            capo_iottwinmaker.types.relationship_value.deserialize_json(
                data["relationshipValue"]
            )
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
