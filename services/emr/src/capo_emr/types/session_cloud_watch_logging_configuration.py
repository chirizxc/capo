"""Generated from Smithy shape ``com.amazonaws.emr#SessionCloudWatchLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.log_types_map
    import capo_emr.types.xml_string


class SessionCloudWatchLoggingConfiguration(TypedDict, closed=True):
    enabled: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Whether CloudWatch Logs is enabled for the session.</p>"""
    log_group: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the log group where session logs are published.</p>"""
    log_stream_name_prefix: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The prefix applied to the log stream name where session logs are published.</p>"""
    encryption_key_arn: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the logs published to CloudWatch Logs.</p>"""
    log_types: NotRequired["capo_emr.types.log_types_map.LogTypesMap"]
    """<p>A map of log component names (for example, <code>SPARK_DRIVER</code>, <code>SPARK_EXECUTOR</code>) to the list of log types to publish for that component (for example, <code>stdout</code>, <code>stderr</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionCloudWatchLoggingConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream_name_prefix" in value:
        out["LogStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "log_types" in value:
        import capo_emr.types.log_types_map

        out["LogTypes"] = capo_emr.types.log_types_map.serialize_aws_json_1_1(
            value["log_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionCloudWatchLoggingConfiguration:
    out: SessionCloudWatchLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("LogGroup") is not None:
        out["log_group"] = data["LogGroup"]
    if data.get("LogStreamNamePrefix") is not None:
        out["log_stream_name_prefix"] = data["LogStreamNamePrefix"]
    if data.get("EncryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if data.get("LogTypes") is not None:
        import capo_emr.types.log_types_map

        out["log_types"] = capo_emr.types.log_types_map.deserialize_aws_json_1_1(
            data["LogTypes"]
        )
    return out
