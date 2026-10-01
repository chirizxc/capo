"""Generated from Smithy shape ``com.amazonaws.redshift#DisableLoggingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.log_destination_type
    import capo_redshift.types.log_type_list
    import capo_redshift.types.string


class DisableLoggingMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster on which logging is to be stopped.</p> <p>Example: <code>examplecluster</code> </p>"""
    log_destination_type: NotRequired[
        "capo_redshift.types.log_destination_type.LogDestinationType"
    ]
    """<p>The log destination type. An enum with possible values of <code>s3</code>, <code>cloudwatch</code>, and <code>s3table</code>. When set to <code>s3table</code>, stops system table publishing. When omitted, the operation disables audit logging.</p>"""
    log_exports: NotRequired["capo_redshift.types.log_type_list.LogTypeList"]
    """<p>The collection of log types to stop exporting. When <code>LogDestinationType</code> is <code>s3table</code>, the values are the names of the system tables to stop publishing. Omitting this parameter or passing <code>all</code> stops publishing all system tables.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableLoggingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "log_destination_type" in value:
        import capo_redshift.types.log_destination_type

        capo_redshift.types.log_destination_type.serialize_query(
            value["log_destination_type"], pairs, f"{key_prefix}LogDestinationType"
        )
    if "log_exports" in value:
        import capo_redshift.types.log_type_list

        capo_redshift.types.log_type_list.serialize_query(
            value["log_exports"], pairs, f"{key_prefix}LogExports"
        )


def deserialize_query(el: Element) -> DisableLoggingMessage:
    out: DisableLoggingMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_log_destination_type = el.find("LogDestinationType")
    if child_log_destination_type is not None:
        import capo_redshift.types.log_destination_type

        out["log_destination_type"] = (
            capo_redshift.types.log_destination_type.deserialize_query(
                child_log_destination_type
            )
        )
    child_log_exports = el.find("LogExports")
    if child_log_exports is not None:
        import capo_redshift.types.log_type_list

        out["log_exports"] = capo_redshift.types.log_type_list.deserialize_query(
            child_log_exports
        )
    return out
