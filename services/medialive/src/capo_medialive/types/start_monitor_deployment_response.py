"""Generated from Smithy shape ``com.amazonaws.medialive#StartMonitorDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__boolean
    import capo_medialive.types.__list_of__string_min7_max11_pattern_aws097
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_min1_max2048
    import capo_medialive.types.__string_min7_max11_pattern_aws097
    import capo_medialive.types.__string_pattern_arn_medialive_signal_map
    import capo_medialive.types.__timestamp_iso8601
    import capo_medialive.types.failed_media_resource_map
    import capo_medialive.types.media_resource_map
    import capo_medialive.types.monitor_deployment
    import capo_medialive.types.signal_map_status
    import capo_medialive.types.successful_monitor_deployment
    import capo_medialive.types.tag_map


class StartMonitorDeploymentResponse(TypedDict, closed=True):
    arn: NotRequired[
        "capo_medialive.types.__string_pattern_arn_medialive_signal_map.__stringPatternArnMedialiveSignalMap"
    ]
    """A signal map's ARN (Amazon Resource Name)"""
    cloud_watch_alarm_template_group_ids: NotRequired[
        "capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.__listOf__stringMin7Max11PatternAws097"
    ]
    created_at: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    discovery_entry_point_arn: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A top-level supported AWS resource ARN to discovery a signal map from."""
    error_message: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """Error message associated with a failed creation or failed update attempt of a signal map."""
    event_bridge_rule_template_group_ids: NotRequired[
        "capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.__listOf__stringMin7Max11PatternAws097"
    ]
    failed_media_resource_map: NotRequired[
        "capo_medialive.types.failed_media_resource_map.FailedMediaResourceMap"
    ]
    id: NotRequired[
        "capo_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """A signal map's id."""
    last_discovered_at: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    last_successful_monitor_deployment: NotRequired[
        "capo_medialive.types.successful_monitor_deployment.SuccessfulMonitorDeployment"
    ]
    media_resource_map: NotRequired[
        "capo_medialive.types.media_resource_map.MediaResourceMap"
    ]
    modified_at: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    monitor_changes_pending_deployment: NotRequired[
        "capo_medialive.types.__boolean.__boolean"
    ]
    """If true, there are pending monitor changes for this signal map that can be deployed."""
    monitor_deployment: NotRequired[
        "capo_medialive.types.monitor_deployment.MonitorDeployment"
    ]
    name: NotRequired[
        "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    status: NotRequired["capo_medialive.types.signal_map_status.SignalMapStatus"]
    tags: NotRequired["capo_medialive.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: StartMonitorDeploymentResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "cloud_watch_alarm_template_group_ids" in value:
        import capo_medialive.types.__list_of__string_min7_max11_pattern_aws097

        out["cloudWatchAlarmTemplateGroupIds"] = (
            capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.serialize_json(
                value["cloud_watch_alarm_template_group_ids"]
            )
        )
    if "created_at" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["createdAt"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "discovery_entry_point_arn" in value:
        out["discoveryEntryPointArn"] = value["discovery_entry_point_arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "event_bridge_rule_template_group_ids" in value:
        import capo_medialive.types.__list_of__string_min7_max11_pattern_aws097

        out["eventBridgeRuleTemplateGroupIds"] = (
            capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.serialize_json(
                value["event_bridge_rule_template_group_ids"]
            )
        )
    if "failed_media_resource_map" in value:
        import capo_medialive.types.failed_media_resource_map

        out["failedMediaResourceMap"] = (
            capo_medialive.types.failed_media_resource_map.serialize_json(
                value["failed_media_resource_map"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "last_discovered_at" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["lastDiscoveredAt"] = (
            capo_medialive.types.__timestamp_iso8601.serialize_json(
                value["last_discovered_at"]
            )
        )
    if "last_successful_monitor_deployment" in value:
        import capo_medialive.types.successful_monitor_deployment

        out["lastSuccessfulMonitorDeployment"] = (
            capo_medialive.types.successful_monitor_deployment.serialize_json(
                value["last_successful_monitor_deployment"]
            )
        )
    if "media_resource_map" in value:
        import capo_medialive.types.media_resource_map

        out["mediaResourceMap"] = (
            capo_medialive.types.media_resource_map.serialize_json(
                value["media_resource_map"]
            )
        )
    if "modified_at" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["modifiedAt"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["modified_at"]
        )
    if "monitor_changes_pending_deployment" in value:
        out["monitorChangesPendingDeployment"] = value[
            "monitor_changes_pending_deployment"
        ]
    if "monitor_deployment" in value:
        import capo_medialive.types.monitor_deployment

        out["monitorDeployment"] = (
            capo_medialive.types.monitor_deployment.serialize_json(
                value["monitor_deployment"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import capo_medialive.types.signal_map_status

        out["status"] = capo_medialive.types.signal_map_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartMonitorDeploymentResponse:
    out: StartMonitorDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("cloudWatchAlarmTemplateGroupIds") is not None:
        import capo_medialive.types.__list_of__string_min7_max11_pattern_aws097

        out["cloud_watch_alarm_template_group_ids"] = (
            capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.deserialize_json(
                data["cloudWatchAlarmTemplateGroupIds"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_medialive.types.__timestamp_iso8601

        out["created_at"] = capo_medialive.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("discoveryEntryPointArn") is not None:
        out["discovery_entry_point_arn"] = data["discoveryEntryPointArn"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("eventBridgeRuleTemplateGroupIds") is not None:
        import capo_medialive.types.__list_of__string_min7_max11_pattern_aws097

        out["event_bridge_rule_template_group_ids"] = (
            capo_medialive.types.__list_of__string_min7_max11_pattern_aws097.deserialize_json(
                data["eventBridgeRuleTemplateGroupIds"]
            )
        )
    if data.get("failedMediaResourceMap") is not None:
        import capo_medialive.types.failed_media_resource_map

        out["failed_media_resource_map"] = (
            capo_medialive.types.failed_media_resource_map.deserialize_json(
                data["failedMediaResourceMap"]
            )
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("lastDiscoveredAt") is not None:
        import capo_medialive.types.__timestamp_iso8601

        out["last_discovered_at"] = (
            capo_medialive.types.__timestamp_iso8601.deserialize_json(
                data["lastDiscoveredAt"]
            )
        )
    if data.get("lastSuccessfulMonitorDeployment") is not None:
        import capo_medialive.types.successful_monitor_deployment

        out["last_successful_monitor_deployment"] = (
            capo_medialive.types.successful_monitor_deployment.deserialize_json(
                data["lastSuccessfulMonitorDeployment"]
            )
        )
    if data.get("mediaResourceMap") is not None:
        import capo_medialive.types.media_resource_map

        out["media_resource_map"] = (
            capo_medialive.types.media_resource_map.deserialize_json(
                data["mediaResourceMap"]
            )
        )
    if data.get("modifiedAt") is not None:
        import capo_medialive.types.__timestamp_iso8601

        out["modified_at"] = capo_medialive.types.__timestamp_iso8601.deserialize_json(
            data["modifiedAt"]
        )
    if data.get("monitorChangesPendingDeployment") is not None:
        out["monitor_changes_pending_deployment"] = data[
            "monitorChangesPendingDeployment"
        ]
    if data.get("monitorDeployment") is not None:
        import capo_medialive.types.monitor_deployment

        out["monitor_deployment"] = (
            capo_medialive.types.monitor_deployment.deserialize_json(
                data["monitorDeployment"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_medialive.types.signal_map_status

        out["status"] = capo_medialive.types.signal_map_status.deserialize_json(
            data["status"]
        )
    if data.get("tags") is not None:
        import capo_medialive.types.tag_map

        out["tags"] = capo_medialive.types.tag_map.deserialize_json(data["tags"])
    return out
