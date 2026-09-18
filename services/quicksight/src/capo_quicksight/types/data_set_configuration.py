"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_group_schema_list
    import capo_quicksight.types.data_set_schema
    import capo_quicksight.types.string


class DataSetConfiguration(TypedDict, closed=True):
    placeholder: NotRequired["capo_quicksight.types.string.String"]
    """<p>Placeholder.</p>"""
    data_set_schema: NotRequired["capo_quicksight.types.data_set_schema.DataSetSchema"]
    """<p>Dataset schema.</p>"""
    column_group_schema_list: NotRequired[
        "capo_quicksight.types.column_group_schema_list.ColumnGroupSchemaList"
    ]
    """<p>A structure containing the list of column group schemas.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetConfiguration) -> dict:
    out: dict = {}
    if "placeholder" in value:
        out["Placeholder"] = value["placeholder"]
    if "data_set_schema" in value:
        import capo_quicksight.types.data_set_schema

        out["DataSetSchema"] = capo_quicksight.types.data_set_schema.serialize_json(
            value["data_set_schema"]
        )
    if "column_group_schema_list" in value:
        import capo_quicksight.types.column_group_schema_list

        out["ColumnGroupSchemaList"] = (
            capo_quicksight.types.column_group_schema_list.serialize_json(
                value["column_group_schema_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetConfiguration:
    out: DataSetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Placeholder") is not None:
        out["placeholder"] = data["Placeholder"]
    if data.get("DataSetSchema") is not None:
        import capo_quicksight.types.data_set_schema

        out["data_set_schema"] = capo_quicksight.types.data_set_schema.deserialize_json(
            data["DataSetSchema"]
        )
    if data.get("ColumnGroupSchemaList") is not None:
        import capo_quicksight.types.column_group_schema_list

        out["column_group_schema_list"] = (
            capo_quicksight.types.column_group_schema_list.deserialize_json(
                data["ColumnGroupSchemaList"]
            )
        )
    return out
