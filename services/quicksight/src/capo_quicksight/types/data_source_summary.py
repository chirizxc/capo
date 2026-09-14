"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_source_type
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.timestamp


class DataSourceSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The arn of the datasource.</p>"""
    data_source_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The unique ID of the data source.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the data source.</p>"""
    type: NotRequired["capo_quicksight.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time that the data source was created. This value is expressed in MM-DD-YYYY HH:MM:SS format.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The date and time the data source was last updated. This value is expressed in MM-DD-YYYY HH:MM:SS format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_quicksight.types.data_source_type

        out["Type"] = capo_quicksight.types.data_source_type.serialize_json(
            value["type"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> DataSourceSummary:
    out: DataSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("DataSourceId") is not None:
        out["data_source_id"] = data["DataSourceId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_quicksight.types.data_source_type

        out["type"] = capo_quicksight.types.data_source_type.deserialize_json(
            data["Type"]
        )
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
