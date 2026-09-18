"""Generated from Smithy shape ``com.amazonaws.appflow#DestinationFieldProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.supported_write_operation_list


class DestinationFieldProperties(TypedDict, closed=True):
    is_creatable: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if the destination field can be created by the current user. </p>"""
    is_nullable: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if the destination field can have a null value. </p>"""
    is_upsertable: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if the flow run can either insert new rows in the destination field if they do not already exist, or update them if they do. </p>"""
    is_updatable: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies whether the field can be updated during an <code>UPDATE</code> or <code>UPSERT</code> write operation. </p>"""
    is_defaulted_on_create: "capo_appflow.types.boolean.Boolean"
    """<p>Specifies whether the field can use the default value during a Create operation.</p>"""
    supported_write_operations: NotRequired[
        "capo_appflow.types.supported_write_operation_list.SupportedWriteOperationList"
    ]
    """<p> A list of supported write operations. For each write operation listed, this field can be used in <code>idFieldNames</code> when that write operation is present as a destination option. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationFieldProperties) -> dict:
    out: dict = {}
    out["isCreatable"] = value.get("is_creatable", False)
    out["isNullable"] = value.get("is_nullable", False)
    out["isUpsertable"] = value.get("is_upsertable", False)
    out["isUpdatable"] = value.get("is_updatable", False)
    out["isDefaultedOnCreate"] = value.get("is_defaulted_on_create", False)
    if "supported_write_operations" in value:
        import capo_appflow.types.supported_write_operation_list

        out["supportedWriteOperations"] = (
            capo_appflow.types.supported_write_operation_list.serialize_json(
                value["supported_write_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationFieldProperties:
    out: DestinationFieldProperties = {}  # type: ignore[typeddict-item]
    if data.get("isCreatable") is not None:
        out["is_creatable"] = data["isCreatable"]
    else:
        out["is_creatable"] = False
    if data.get("isNullable") is not None:
        out["is_nullable"] = data["isNullable"]
    else:
        out["is_nullable"] = False
    if data.get("isUpsertable") is not None:
        out["is_upsertable"] = data["isUpsertable"]
    else:
        out["is_upsertable"] = False
    if data.get("isUpdatable") is not None:
        out["is_updatable"] = data["isUpdatable"]
    else:
        out["is_updatable"] = False
    if data.get("isDefaultedOnCreate") is not None:
        out["is_defaulted_on_create"] = data["isDefaultedOnCreate"]
    else:
        out["is_defaulted_on_create"] = False
    if data.get("supportedWriteOperations") is not None:
        import capo_appflow.types.supported_write_operation_list

        out["supported_write_operations"] = (
            capo_appflow.types.supported_write_operation_list.deserialize_json(
                data["supportedWriteOperations"]
            )
        )
    return out
