"""Generated from Smithy shape ``com.amazonaws.redshift#EnableLoggingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.log_destination_type
    import capo_redshift.types.log_type_list
    import capo_redshift.types.s3_key_prefix_value
    import capo_redshift.types.string


class EnableLoggingMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster on which logging is to be started.</p> <p>Example: <code>examplecluster</code> </p>"""
    bucket_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of an existing S3 bucket where the log files are to be stored.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the same region as the cluster</p> </li> <li> <p>The cluster must have read bucket and put object permissions</p> </li> </ul>"""
    s3_key_prefix: NotRequired[
        "capo_redshift.types.s3_key_prefix_value.S3KeyPrefixValue"
    ]
    r"""<p>The prefix applied to the log file names.</p> <p>Valid characters are any letter from any language, any whitespace character, any numeric character, and the following characters: underscore (<code>_</code>), period (<code>.</code>), colon (<code>:</code>), slash (<code>/</code>), equal (<code>=</code>), plus (<code>+</code>), backslash (<code>\</code>), hyphen (<code>-</code>), at symbol (<code>@</code>).</p>"""
    log_destination_type: NotRequired[
        "capo_redshift.types.log_destination_type.LogDestinationType"
    ]
    """<p>The log destination type. An enum with possible values of <code>s3</code>, <code>cloudwatch</code>, and <code>s3table</code>.</p>"""
    log_exports: NotRequired["capo_redshift.types.log_type_list.LogTypeList"]
    """<p>The collection of exported log types. When <code>LogDestinationType</code> is <code>s3</code> or <code>cloudwatch</code>, possible values are <code>connectionlog</code>, <code>useractivitylog</code>, and <code>userlog</code>. When <code>LogDestinationType</code> is <code>s3table</code>, the values are the names of the system tables to publish. Omitting this parameter, passing an empty list, or including the value <code>all</code> publishes all current and future system tables.</p>"""
    s3_table_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of a customer managed KMS key used to encrypt the S3 tables. This parameter is valid only when <code>LogDestinationType</code> is <code>s3table</code>.</p>"""
    s3_table_granularity: NotRequired["capo_redshift.types.string.String"]
    """<p>The scope of system table publishing. Valid values are <code>cluster</code> and <code>account</code>. A value of <code>cluster</code> scopes publishing to the individual cluster. A value of <code>account</code> scopes publishing to the Amazon Web Services account. This parameter is valid only when <code>LogDestinationType</code> is <code>s3table</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableLoggingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "bucket_name" in value:
        pairs.append((f"{key_prefix}BucketName", str(value["bucket_name"])))
    if "s3_key_prefix" in value:
        pairs.append((f"{key_prefix}S3KeyPrefix", str(value["s3_key_prefix"])))
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
    if "s3_table_kms_key_id" in value:
        pairs.append(
            (f"{key_prefix}S3TableKmsKeyId", str(value["s3_table_kms_key_id"]))
        )
    if "s3_table_granularity" in value:
        pairs.append(
            (f"{key_prefix}S3TableGranularity", str(value["s3_table_granularity"]))
        )


def deserialize_query(el: Element) -> EnableLoggingMessage:
    out: EnableLoggingMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    child_s3_key_prefix = el.find("S3KeyPrefix")
    if child_s3_key_prefix is not None:
        out["s3_key_prefix"] = str(child_s3_key_prefix.text or "")
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
    child_s3_table_kms_key_id = el.find("S3TableKmsKeyId")
    if child_s3_table_kms_key_id is not None:
        out["s3_table_kms_key_id"] = str(child_s3_table_kms_key_id.text or "")
    child_s3_table_granularity = el.find("S3TableGranularity")
    if child_s3_table_granularity is not None:
        out["s3_table_granularity"] = str(child_s3_table_granularity.text or "")
    return out
