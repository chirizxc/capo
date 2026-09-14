"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.boolean
    import capo_config_service.types.date
    import capo_config_service.types.recorder_status
    import capo_config_service.types.service_principal
    import capo_config_service.types.string


class ConfigurationRecorderStatus(TypedDict, closed=True):
    arn: NotRequired[
        "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the configuration recorder.</p>"""
    name: NotRequired["capo_config_service.types.string.String"]
    """<p>The name of the configuration recorder.</p>"""
    last_start_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time the recorder was last started.</p>"""
    last_stop_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time the recorder was last stopped.</p>"""
    recording: "capo_config_service.types.boolean.Boolean"
    """<p>Specifies whether or not the recorder is currently recording.</p>"""
    last_status: NotRequired["capo_config_service.types.recorder_status.RecorderStatus"]
    """<p>The status of the latest recording event processed by the recorder.</p>"""
    last_error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>The latest error code from when the recorder last failed.</p>"""
    last_error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>The latest error message from when the recorder last failed.</p>"""
    last_status_change_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time of the latest change in status of an recording event processed by the recorder.</p>"""
    service_principal: NotRequired[
        "capo_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, the service principal of the linked Amazon Web Services service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderStatus) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "last_start_time" in value:
        import capo_config_service.types.date

        out["lastStartTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_start_time"]
        )
    if "last_stop_time" in value:
        import capo_config_service.types.date

        out["lastStopTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_stop_time"]
        )
    out["recording"] = value.get("recording", False)
    if "last_status" in value:
        import capo_config_service.types.recorder_status

        out["lastStatus"] = (
            capo_config_service.types.recorder_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "last_error_code" in value:
        out["lastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["lastErrorMessage"] = value["last_error_message"]
    if "last_status_change_time" in value:
        import capo_config_service.types.date

        out["lastStatusChangeTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_status_change_time"]
            )
        )
    if "service_principal" in value:
        out["servicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorderStatus:
    out: ConfigurationRecorderStatus = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("lastStartTime") is not None:
        import capo_config_service.types.date

        out["last_start_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStartTime"]
            )
        )
    if data.get("lastStopTime") is not None:
        import capo_config_service.types.date

        out["last_stop_time"] = capo_config_service.types.date.deserialize_aws_json_1_1(
            data["lastStopTime"]
        )
    if data.get("recording") is not None:
        out["recording"] = data["recording"]
    else:
        out["recording"] = False
    if data.get("lastStatus") is not None:
        import capo_config_service.types.recorder_status

        out["last_status"] = (
            capo_config_service.types.recorder_status.deserialize_aws_json_1_1(
                data["lastStatus"]
            )
        )
    if data.get("lastErrorCode") is not None:
        out["last_error_code"] = data["lastErrorCode"]
    if data.get("lastErrorMessage") is not None:
        out["last_error_message"] = data["lastErrorMessage"]
    if data.get("lastStatusChangeTime") is not None:
        import capo_config_service.types.date

        out["last_status_change_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStatusChangeTime"]
            )
        )
    if data.get("servicePrincipal") is not None:
        out["service_principal"] = data["servicePrincipal"]
    return out
