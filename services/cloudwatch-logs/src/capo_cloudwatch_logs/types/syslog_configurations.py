"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SyslogConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.syslog_configuration

SyslogConfigurations: TypeAlias = list[
    "capo_cloudwatch_logs.types.syslog_configuration.SyslogConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SyslogConfigurations) -> list:
    import capo_cloudwatch_logs.types.syslog_configuration

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.syslog_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SyslogConfigurations:
    import capo_cloudwatch_logs.types.syslog_configuration

    out: SyslogConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.syslog_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
