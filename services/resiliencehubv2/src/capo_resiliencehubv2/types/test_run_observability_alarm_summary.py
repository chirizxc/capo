"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunObservabilityAlarmSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.cloud_watch_alarm_arn


class TestRunObservabilityAlarmSummary(TypedDict, closed=True):
    alarm_arn: "capo_resiliencehubv2.types.cloud_watch_alarm_arn.CloudWatchAlarmArn"
    """<p>The ARN of the CloudWatch alarm.</p>"""
    alarm_name: "str"
    """<p>The name of the CloudWatch alarm.</p>"""
    region: "str"
    """<p>The Region of the CloudWatch alarm.</p>"""
    account_id: "str"
    """<p>The account ID that owns the CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunObservabilityAlarmSummary) -> dict:
    out: dict = {}
    out["alarmArn"] = value["alarm_arn"]
    out["alarmName"] = value["alarm_name"]
    out["region"] = value["region"]
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> TestRunObservabilityAlarmSummary:
    out: TestRunObservabilityAlarmSummary = {}  # type: ignore[typeddict-item]
    if data.get("alarmArn") is not None:
        out["alarm_arn"] = data["alarmArn"]
    else:
        raise DeserializationError(
            "TestRunObservabilityAlarmSummary.alarm_arn required"
        )
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        raise DeserializationError(
            "TestRunObservabilityAlarmSummary.alarm_name required"
        )
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        raise DeserializationError("TestRunObservabilityAlarmSummary.region required")
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "TestRunObservabilityAlarmSummary.account_id required"
        )
    return out
