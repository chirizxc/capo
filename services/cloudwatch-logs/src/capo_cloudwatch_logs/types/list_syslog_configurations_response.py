"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListSyslogConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.syslog_configurations


class ListSyslogConfigurationsResponse(TypedDict, closed=True):
    syslog_configurations: NotRequired[
        "capo_cloudwatch_logs.types.syslog_configurations.SyslogConfigurations"
    ]
    """<p>The list of syslog configurations.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. The token expires after 24 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSyslogConfigurationsResponse) -> dict:
    out: dict = {}
    if "syslog_configurations" in value:
        import capo_cloudwatch_logs.types.syslog_configurations

        out["syslogConfigurations"] = (
            capo_cloudwatch_logs.types.syslog_configurations.serialize_aws_json_1_1(
                value["syslog_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSyslogConfigurationsResponse:
    out: ListSyslogConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("syslogConfigurations") is not None:
        import capo_cloudwatch_logs.types.syslog_configurations

        out["syslog_configurations"] = (
            capo_cloudwatch_logs.types.syslog_configurations.deserialize_aws_json_1_1(
                data["syslogConfigurations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
