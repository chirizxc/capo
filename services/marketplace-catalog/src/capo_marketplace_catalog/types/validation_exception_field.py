"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.change_type
    import capo_marketplace_catalog.types.entity_id
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.exception_message_content
    import capo_marketplace_catalog.types.field_name
    import capo_marketplace_catalog.types.validation_exception_reason


class ValidationExceptionField(TypedDict, closed=True):
    reason: NotRequired[
        "capo_marketplace_catalog.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason the field failed validation.</p>"""
    entity_type: NotRequired["capo_marketplace_catalog.types.entity_type.EntityType"]
    """<p>The entity type the failing field applies to, if the field is on a specific entity. For example, <code>AmiProduct@1.0</code>.</p>"""
    entity_id: NotRequired["capo_marketplace_catalog.types.entity_id.EntityId"]
    """<p>The entity identifier the failing field applies to, if the field is on a specific entity.</p>"""
    change_type: NotRequired["capo_marketplace_catalog.types.change_type.ChangeType"]
    """<p>The change type the failing field applies to, if the field is part of a change request. For example, <code>AddDeliveryOptions</code>.</p>"""
    field: NotRequired["capo_marketplace_catalog.types.field_name.FieldName"]
    """<p>The name of the request field that failed validation, expressed as a JSON path (for example, <code>Details.DeliveryOptions[0].Type</code>).</p>"""
    message: NotRequired[
        "capo_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]
    """<p>A human-readable message describing why the field failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    if "reason" in value:
        import capo_marketplace_catalog.types.validation_exception_reason

        out["Reason"] = (
            capo_marketplace_catalog.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "entity_type" in value:
        out["EntityType"] = value["entity_type"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "change_type" in value:
        out["ChangeType"] = value["change_type"]
    if "field" in value:
        out["Field"] = value["field"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        import capo_marketplace_catalog.types.validation_exception_reason

        out["reason"] = (
            capo_marketplace_catalog.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    if data.get("EntityType") is not None:
        out["entity_type"] = data["EntityType"]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("ChangeType") is not None:
        out["change_type"] = data["ChangeType"]
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
