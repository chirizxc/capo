"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateCloudWatchAlarmTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min10_max86400
    import capo_medialive.types.__string
    import capo_medialive.types.__string_max64
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_pattern_s
    import capo_medialive.types.cloud_watch_alarm_template_comparison_operator
    import capo_medialive.types.cloud_watch_alarm_template_statistic
    import capo_medialive.types.cloud_watch_alarm_template_target_resource_type
    import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data


class UpdateCloudWatchAlarmTemplateRequest(TypedDict, closed=True):
    comparison_operator: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
    ]
    datapoints_to_alarm: NotRequired[
        "capo_medialive.types.__integer_min1.__integerMin1"
    ]
    """The number of datapoints within the evaluation period that must be breaching to trigger the alarm."""
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    evaluation_periods: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """The number of periods over which data is compared to the specified threshold."""
    group_identifier: NotRequired[
        "capo_medialive.types.__string_pattern_s.__stringPatternS"
    ]
    """A cloudwatch alarm template group's identifier. Can be either be its id or current name."""
    identifier: "capo_medialive.types.__string.__string"
    """A cloudwatch alarm template's identifier. Can be either be its id or current name."""
    metric_name: NotRequired["capo_medialive.types.__string_max64.__stringMax64"]
    """The name of the metric associated with the alarm. Must be compatible with targetResourceType."""
    name: NotRequired[
        "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    period: NotRequired[
        "capo_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
    ]
    """The period, in seconds, over which the specified statistic is applied."""
    statistic: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
    ]
    target_resource_type: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
    ]
    threshold: NotRequired["capo_medialive.types.__double.__double"]
    """The threshold value to compare with the specified statistic."""
    treat_missing_data: NotRequired[
        "capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCloudWatchAlarmTemplateRequest) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import capo_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparisonOperator"] = (
            capo_medialive.types.cloud_watch_alarm_template_comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "datapoints_to_alarm" in value:
        out["datapointsToAlarm"] = value["datapoints_to_alarm"]
    if "description" in value:
        out["description"] = value["description"]
    if "evaluation_periods" in value:
        out["evaluationPeriods"] = value["evaluation_periods"]
    if "group_identifier" in value:
        out["groupIdentifier"] = value["group_identifier"]
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "name" in value:
        out["name"] = value["name"]
    if "period" in value:
        out["period"] = value["period"]
    if "statistic" in value:
        import capo_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            capo_medialive.types.cloud_watch_alarm_template_statistic.serialize_json(
                value["statistic"]
            )
        )
    if "target_resource_type" in value:
        import capo_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["targetResourceType"] = (
            capo_medialive.types.cloud_watch_alarm_template_target_resource_type.serialize_json(
                value["target_resource_type"]
            )
        )
    if "threshold" in value:
        out["threshold"] = (
            "NaN"
            if value["threshold"] != value["threshold"]
            else "Infinity"
            if value["threshold"] == float("inf")
            else "-Infinity"
            if value["threshold"] == float("-inf")
            else value["threshold"]
        )
    if "treat_missing_data" in value:
        import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treatMissingData"] = (
            capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.serialize_json(
                value["treat_missing_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCloudWatchAlarmTemplateRequest:
    out: UpdateCloudWatchAlarmTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("comparisonOperator") is not None:
        import capo_medialive.types.cloud_watch_alarm_template_comparison_operator

        out["comparison_operator"] = (
            capo_medialive.types.cloud_watch_alarm_template_comparison_operator.deserialize_json(
                data["comparisonOperator"]
            )
        )
    if data.get("datapointsToAlarm") is not None:
        out["datapoints_to_alarm"] = data["datapointsToAlarm"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("evaluationPeriods") is not None:
        out["evaluation_periods"] = data["evaluationPeriods"]
    if data.get("groupIdentifier") is not None:
        out["group_identifier"] = data["groupIdentifier"]
    if data.get("metricName") is not None:
        out["metric_name"] = data["metricName"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("period") is not None:
        out["period"] = data["period"]
    if data.get("statistic") is not None:
        import capo_medialive.types.cloud_watch_alarm_template_statistic

        out["statistic"] = (
            capo_medialive.types.cloud_watch_alarm_template_statistic.deserialize_json(
                data["statistic"]
            )
        )
    if data.get("targetResourceType") is not None:
        import capo_medialive.types.cloud_watch_alarm_template_target_resource_type

        out["target_resource_type"] = (
            capo_medialive.types.cloud_watch_alarm_template_target_resource_type.deserialize_json(
                data["targetResourceType"]
            )
        )
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    if data.get("treatMissingData") is not None:
        import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data

        out["treat_missing_data"] = (
            capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.deserialize_json(
                data["treatMissingData"]
            )
        )
    return out
