"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.field_arn
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_namespace
    import capo_connectcases.types.field_type


class FieldSummary(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    field_arn: "capo_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""
    name: "capo_connectcases.types.field_name.FieldName"
    """<p>Name of the field.</p>"""
    type: "capo_connectcases.types.field_type.FieldType"
    """<p>The type of a field.</p>"""
    namespace: "capo_connectcases.types.field_namespace.FieldNamespace"
    """<p>The namespace of a field.</p>"""
    attributes: NotRequired["capo_connectcases.types.field_attributes.FieldAttributes"]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSummary) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["fieldArn"] = value["field_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["namespace"] = value["namespace"]
    if "attributes" in value:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> FieldSummary:
    out: FieldSummary = {}  # type: ignore[typeddict-item]
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("FieldSummary.field_id required")
    if data.get("fieldArn") is not None:
        out["field_arn"] = data["fieldArn"]
    else:
        raise DeserializationError("FieldSummary.field_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FieldSummary.name required")
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FieldSummary.type required")
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("FieldSummary.namespace required")
    if data.get("attributes") is not None:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.deserialize_json(
            data["attributes"]
        )
    return out
