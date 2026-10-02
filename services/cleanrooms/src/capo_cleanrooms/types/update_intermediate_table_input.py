"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIntermediateTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_column_list
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description


class UpdateIntermediateTableInput(TypedDict, closed=True):
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table to update.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the intermediate table.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the customer-managed KMS key to use for encrypting future population data.</p>"""
    columns: NotRequired[
        "capo_cleanrooms.types.intermediate_table_column_list.IntermediateTableColumnList"
    ]
    """<p>The list of columns with updated type definitions. Only the type of existing columns can be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntermediateTableInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "columns" in value:
        import capo_cleanrooms.types.intermediate_table_column_list

        out["columns"] = (
            capo_cleanrooms.types.intermediate_table_column_list.serialize_json(
                value["columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIntermediateTableInput:
    out: UpdateIntermediateTableInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("columns") is not None:
        import capo_cleanrooms.types.intermediate_table_column_list

        out["columns"] = (
            capo_cleanrooms.types.intermediate_table_column_list.deserialize_json(
                data["columns"]
            )
        )
    return out
