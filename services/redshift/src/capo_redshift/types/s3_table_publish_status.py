"""Generated from Smithy shape ``com.amazonaws.redshift#S3TablePublishStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.log_type_list
    import capo_redshift.types.s3_table_last_ingestion_time_map
    import capo_redshift.types.string


class S3TablePublishStatus(TypedDict, closed=True):
    s3_tables: NotRequired["capo_redshift.types.log_type_list.LogTypeList"]
    """<p>The system tables currently being published.</p>"""
    s3_table_namespace: NotRequired["capo_redshift.types.string.String"]
    """<p>The namespace in the S3 table bucket that holds the published tables.</p>"""
    s3_table_granularity: NotRequired["capo_redshift.types.string.String"]
    """<p>The scope of system table publishing in effect. Possible values are <code>cluster</code> and <code>account</code>.</p>"""
    enabled_all: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p> <code>true</code> if the cluster is enrolled in all current and future system tables rather than an explicit subset.</p>"""
    last_ingestion_times: NotRequired[
        "capo_redshift.types.s3_table_last_ingestion_time_map.S3TableLastIngestionTimeMap"
    ]
    """<p>A map whose keys are the names of the published system tables and whose values are the time each table last received data. Use this to judge data freshness.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: S3TablePublishStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "s3_tables" in value:
        import capo_redshift.types.log_type_list

        capo_redshift.types.log_type_list.serialize_query(
            value["s3_tables"], pairs, f"{key_prefix}S3Tables"
        )
    if "s3_table_namespace" in value:
        pairs.append(
            (f"{key_prefix}S3TableNamespace", str(value["s3_table_namespace"]))
        )
    if "s3_table_granularity" in value:
        pairs.append(
            (f"{key_prefix}S3TableGranularity", str(value["s3_table_granularity"]))
        )
    if "enabled_all" in value:
        pairs.append(
            (f"{key_prefix}EnabledAll", "true" if value["enabled_all"] else "false")
        )
    if "last_ingestion_times" in value:
        import capo_redshift.types.s3_table_last_ingestion_time_map

        capo_redshift.types.s3_table_last_ingestion_time_map.serialize_query(
            value["last_ingestion_times"], pairs, f"{key_prefix}LastIngestionTimes"
        )


def deserialize_query(el: Element) -> S3TablePublishStatus:
    out: S3TablePublishStatus = {}  # type: ignore[typeddict-item]
    child_s3_tables = el.find("S3Tables")
    if child_s3_tables is not None:
        import capo_redshift.types.log_type_list

        out["s3_tables"] = capo_redshift.types.log_type_list.deserialize_query(
            child_s3_tables
        )
    child_s3_table_namespace = el.find("S3TableNamespace")
    if child_s3_table_namespace is not None:
        out["s3_table_namespace"] = str(child_s3_table_namespace.text or "")
    child_s3_table_granularity = el.find("S3TableGranularity")
    if child_s3_table_granularity is not None:
        out["s3_table_granularity"] = str(child_s3_table_granularity.text or "")
    child_enabled_all = el.find("EnabledAll")
    if child_enabled_all is not None:
        out["enabled_all"] = (child_enabled_all.text or "").lower() == "true"
    child_last_ingestion_times = el.find("LastIngestionTimes")
    if child_last_ingestion_times is not None:
        import capo_redshift.types.s3_table_last_ingestion_time_map

        out["last_ingestion_times"] = (
            capo_redshift.types.s3_table_last_ingestion_time_map.deserialize_query(
                child_last_ingestion_times
            )
        )
    return out
