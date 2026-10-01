"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#S3TablePublishStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.s3_table_granularity
    import capo_redshift_serverless.types.s3_table_last_ingestion_time_map
    import capo_redshift_serverless.types.s3_table_name_list


class S3TablePublishStatus(TypedDict, closed=True):
    s3_tables: NotRequired[
        "capo_redshift_serverless.types.s3_table_name_list.S3TableNameList"
    ]
    """<p>The system tables currently being published.</p>"""
    s3_table_namespace: NotRequired["str"]
    """<p>The identifier of the namespace in the S3 table bucket that holds the published tables.</p>"""
    s3_table_granularity: NotRequired[
        "capo_redshift_serverless.types.s3_table_granularity.S3TableGranularity"
    ]
    """<p>The scope currently in effect. Values are <code>namespace</code> or <code>account</code>.</p>"""
    enabled_all: NotRequired["bool"]
    """<p> <code>true</code> when the namespace is enrolled in every current and future system table rather than an explicit list of tables.</p>"""
    last_ingestion_times: NotRequired[
        "capo_redshift_serverless.types.s3_table_last_ingestion_time_map.S3TableLastIngestionTimeMap"
    ]
    """<p>A map of system table name to the time that table last received data, as an ISO-8601 timestamp. A table that has not yet been ingested is absent from the map. Use it to judge data freshness.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablePublishStatus) -> dict:
    out: dict = {}
    if "s3_tables" in value:
        import capo_redshift_serverless.types.s3_table_name_list

        out["s3Tables"] = (
            capo_redshift_serverless.types.s3_table_name_list.serialize_aws_json_1_1(
                value["s3_tables"]
            )
        )
    if "s3_table_namespace" in value:
        out["s3TableNamespace"] = value["s3_table_namespace"]
    if "s3_table_granularity" in value:
        out["s3TableGranularity"] = value["s3_table_granularity"]
    if "enabled_all" in value:
        out["enabledAll"] = value["enabled_all"]
    if "last_ingestion_times" in value:
        import capo_redshift_serverless.types.s3_table_last_ingestion_time_map

        out["lastIngestionTimes"] = (
            capo_redshift_serverless.types.s3_table_last_ingestion_time_map.serialize_aws_json_1_1(
                value["last_ingestion_times"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3TablePublishStatus:
    out: S3TablePublishStatus = {}  # type: ignore[typeddict-item]
    if data.get("s3Tables") is not None:
        import capo_redshift_serverless.types.s3_table_name_list

        out["s3_tables"] = (
            capo_redshift_serverless.types.s3_table_name_list.deserialize_aws_json_1_1(
                data["s3Tables"]
            )
        )
    if data.get("s3TableNamespace") is not None:
        out["s3_table_namespace"] = data["s3TableNamespace"]
    if data.get("s3TableGranularity") is not None:
        out["s3_table_granularity"] = data["s3TableGranularity"]
    if data.get("enabledAll") is not None:
        out["enabled_all"] = data["enabledAll"]
    if data.get("lastIngestionTimes") is not None:
        import capo_redshift_serverless.types.s3_table_last_ingestion_time_map

        out["last_ingestion_times"] = (
            capo_redshift_serverless.types.s3_table_last_ingestion_time_map.deserialize_aws_json_1_1(
                data["lastIngestionTimes"]
            )
        )
    return out
