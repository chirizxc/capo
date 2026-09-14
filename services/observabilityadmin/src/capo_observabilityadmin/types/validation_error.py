"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.field_map


class ValidationError(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>The error message describing the validation issue.</p>"""
    reason: NotRequired["str"]
    """<p>The reason code or category for the validation error.</p>"""
    field_map: NotRequired["capo_observabilityadmin.types.field_map.FieldMap"]
    """<p>A mapping of field names to specific validation issues within the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "field_map" in value:
        import capo_observabilityadmin.types.field_map

        out["FieldMap"] = capo_observabilityadmin.types.field_map.serialize_json(
            value["field_map"]
        )
    return out


def deserialize_json(data: dict) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("FieldMap") is not None:
        import capo_observabilityadmin.types.field_map

        out["field_map"] = capo_observabilityadmin.types.field_map.deserialize_json(
            data["FieldMap"]
        )
    return out
