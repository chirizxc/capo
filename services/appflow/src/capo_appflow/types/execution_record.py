"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.date
    import capo_appflow.types.execution_id
    import capo_appflow.types.execution_result
    import capo_appflow.types.execution_status
    import capo_appflow.types.metadata_catalog_details


class ExecutionRecord(TypedDict, closed=True):
    execution_id: NotRequired["capo_appflow.types.execution_id.ExecutionId"]
    """<p> Specifies the identifier of the given flow run. </p>"""
    execution_status: NotRequired["capo_appflow.types.execution_status.ExecutionStatus"]
    """<p> Specifies the flow run status and whether it is in progress, has completed successfully, or has failed. </p>"""
    execution_result: NotRequired["capo_appflow.types.execution_result.ExecutionResult"]
    """<p> Describes the result of the given flow run. </p>"""
    started_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies the start time of the flow run. </p>"""
    last_updated_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies the time of the most recent update. </p>"""
    data_pull_start_time: NotRequired["capo_appflow.types.date.Date"]
    """<p> The timestamp that determines the first new or updated record to be transferred in the flow run. </p>"""
    data_pull_end_time: NotRequired["capo_appflow.types.date.Date"]
    """<p> The timestamp that indicates the last new or updated record to be transferred in the flow run. </p>"""
    metadata_catalog_details: NotRequired[
        "capo_appflow.types.metadata_catalog_details.MetadataCatalogDetails"
    ]
    """<p>Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionRecord) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    if "execution_status" in value:
        import capo_appflow.types.execution_status

        out["executionStatus"] = capo_appflow.types.execution_status.serialize_json(
            value["execution_status"]
        )
    if "execution_result" in value:
        import capo_appflow.types.execution_result

        out["executionResult"] = capo_appflow.types.execution_result.serialize_json(
            value["execution_result"]
        )
    if "started_at" in value:
        import capo_appflow.types.date

        out["startedAt"] = capo_appflow.types.date.serialize_json(value["started_at"])
    if "last_updated_at" in value:
        import capo_appflow.types.date

        out["lastUpdatedAt"] = capo_appflow.types.date.serialize_json(
            value["last_updated_at"]
        )
    if "data_pull_start_time" in value:
        import capo_appflow.types.date

        out["dataPullStartTime"] = capo_appflow.types.date.serialize_json(
            value["data_pull_start_time"]
        )
    if "data_pull_end_time" in value:
        import capo_appflow.types.date

        out["dataPullEndTime"] = capo_appflow.types.date.serialize_json(
            value["data_pull_end_time"]
        )
    if "metadata_catalog_details" in value:
        import capo_appflow.types.metadata_catalog_details

        out["metadataCatalogDetails"] = (
            capo_appflow.types.metadata_catalog_details.serialize_json(
                value["metadata_catalog_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionRecord:
    out: ExecutionRecord = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    if data.get("executionStatus") is not None:
        import capo_appflow.types.execution_status

        out["execution_status"] = capo_appflow.types.execution_status.deserialize_json(
            data["executionStatus"]
        )
    if data.get("executionResult") is not None:
        import capo_appflow.types.execution_result

        out["execution_result"] = capo_appflow.types.execution_result.deserialize_json(
            data["executionResult"]
        )
    if data.get("startedAt") is not None:
        import capo_appflow.types.date

        out["started_at"] = capo_appflow.types.date.deserialize_json(data["startedAt"])
    if data.get("lastUpdatedAt") is not None:
        import capo_appflow.types.date

        out["last_updated_at"] = capo_appflow.types.date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if data.get("dataPullStartTime") is not None:
        import capo_appflow.types.date

        out["data_pull_start_time"] = capo_appflow.types.date.deserialize_json(
            data["dataPullStartTime"]
        )
    if data.get("dataPullEndTime") is not None:
        import capo_appflow.types.date

        out["data_pull_end_time"] = capo_appflow.types.date.deserialize_json(
            data["dataPullEndTime"]
        )
    if data.get("metadataCatalogDetails") is not None:
        import capo_appflow.types.metadata_catalog_details

        out["metadata_catalog_details"] = (
            capo_appflow.types.metadata_catalog_details.deserialize_json(
                data["metadataCatalogDetails"]
            )
        )
    return out
