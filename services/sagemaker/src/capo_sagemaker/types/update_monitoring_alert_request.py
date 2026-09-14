"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateMonitoringAlertRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_alert_name
    import capo_sagemaker.types.monitoring_datapoints_to_alert
    import capo_sagemaker.types.monitoring_evaluation_period
    import capo_sagemaker.types.monitoring_schedule_name


class UpdateMonitoringAlertRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of a monitoring schedule.</p>"""
    monitoring_alert_name: NotRequired[
        "capo_sagemaker.types.monitoring_alert_name.MonitoringAlertName"
    ]
    """<p>The name of a monitoring alert.</p>"""
    datapoints_to_alert: NotRequired[
        "capo_sagemaker.types.monitoring_datapoints_to_alert.MonitoringDatapointsToAlert"
    ]
    """<p>Within <code>EvaluationPeriod</code>, how many execution failures will raise an alert.</p>"""
    evaluation_period: NotRequired[
        "capo_sagemaker.types.monitoring_evaluation_period.MonitoringEvaluationPeriod"
    ]
    """<p>The number of most recent monitoring executions to consider when evaluating alert status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMonitoringAlertRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_alert_name" in value:
        out["MonitoringAlertName"] = value["monitoring_alert_name"]
    if "datapoints_to_alert" in value:
        out["DatapointsToAlert"] = value["datapoints_to_alert"]
    if "evaluation_period" in value:
        out["EvaluationPeriod"] = value["evaluation_period"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMonitoringAlertRequest:
    out: UpdateMonitoringAlertRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitoringScheduleName") is not None:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if data.get("MonitoringAlertName") is not None:
        out["monitoring_alert_name"] = data["MonitoringAlertName"]
    if data.get("DatapointsToAlert") is not None:
        out["datapoints_to_alert"] = data["DatapointsToAlert"]
    if data.get("EvaluationPeriod") is not None:
        out["evaluation_period"] = data["EvaluationPeriod"]
    return out
