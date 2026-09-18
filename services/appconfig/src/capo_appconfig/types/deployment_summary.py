"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deployment_state
    import capo_appconfig.types.growth_type
    import capo_appconfig.types.integer
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.minutes_between0_and24_hours
    import capo_appconfig.types.name
    import capo_appconfig.types.percentage
    import capo_appconfig.types.version
    import capo_appconfig.types.version_label


class DeploymentSummary(TypedDict, closed=True):
    deployment_number: "capo_appconfig.types.integer.Integer"
    """<p>The sequence number of the deployment.</p>"""
    configuration_name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the configuration.</p>"""
    configuration_version: NotRequired["capo_appconfig.types.version.Version"]
    """<p>The version of the configuration.</p>"""
    deployment_duration_in_minutes: (
        "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>Total amount of time the deployment lasted.</p>"""
    growth_type: NotRequired["capo_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grows over time.</p>"""
    growth_factor: NotRequired["capo_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets to receive a deployed configuration during each interval.</p>"""
    final_bake_time_in_minutes: (
        "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>The amount of time that AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>"""
    state: NotRequired["capo_appconfig.types.deployment_state.DeploymentState"]
    """<p>The state of the deployment.</p>"""
    percentage_complete: NotRequired["capo_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets for which the deployment is available.</p>"""
    started_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>Time the deployment started.</p>"""
    completed_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>Time the deployment completed.</p>"""
    version_label: NotRequired["capo_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentSummary) -> dict:
    out: dict = {}
    out["DeploymentNumber"] = value.get("deployment_number", 0)
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "configuration_version" in value:
        out["ConfigurationVersion"] = value["configuration_version"]
    out["DeploymentDurationInMinutes"] = value.get("deployment_duration_in_minutes", 0)
    if "growth_type" in value:
        import capo_appconfig.types.growth_type

        out["GrowthType"] = capo_appconfig.types.growth_type.serialize_json(
            value["growth_type"]
        )
    if "growth_factor" in value:
        out["GrowthFactor"] = (
            "NaN"
            if value["growth_factor"] != value["growth_factor"]
            else "Infinity"
            if value["growth_factor"] == float("inf")
            else "-Infinity"
            if value["growth_factor"] == float("-inf")
            else value["growth_factor"]
        )
    out["FinalBakeTimeInMinutes"] = value.get("final_bake_time_in_minutes", 0)
    if "state" in value:
        import capo_appconfig.types.deployment_state

        out["State"] = capo_appconfig.types.deployment_state.serialize_json(
            value["state"]
        )
    if "percentage_complete" in value:
        out["PercentageComplete"] = (
            "NaN"
            if value["percentage_complete"] != value["percentage_complete"]
            else "Infinity"
            if value["percentage_complete"] == float("inf")
            else "-Infinity"
            if value["percentage_complete"] == float("-inf")
            else value["percentage_complete"]
        )
    if "started_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["StartedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["CompletedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["completed_at"]
        )
    if "version_label" in value:
        out["VersionLabel"] = value["version_label"]
    return out


def deserialize_json(data: dict) -> DeploymentSummary:
    out: DeploymentSummary = {}  # type: ignore[typeddict-item]
    if data.get("DeploymentNumber") is not None:
        out["deployment_number"] = data["DeploymentNumber"]
    else:
        out["deployment_number"] = 0
    if data.get("ConfigurationName") is not None:
        out["configuration_name"] = data["ConfigurationName"]
    if data.get("ConfigurationVersion") is not None:
        out["configuration_version"] = data["ConfigurationVersion"]
    if data.get("DeploymentDurationInMinutes") is not None:
        out["deployment_duration_in_minutes"] = data["DeploymentDurationInMinutes"]
    else:
        out["deployment_duration_in_minutes"] = 0
    if data.get("GrowthType") is not None:
        import capo_appconfig.types.growth_type

        out["growth_type"] = capo_appconfig.types.growth_type.deserialize_json(
            data["GrowthType"]
        )
    if data.get("GrowthFactor") is not None:
        out["growth_factor"] = float(data["GrowthFactor"])
    if data.get("FinalBakeTimeInMinutes") is not None:
        out["final_bake_time_in_minutes"] = data["FinalBakeTimeInMinutes"]
    else:
        out["final_bake_time_in_minutes"] = 0
    if data.get("State") is not None:
        import capo_appconfig.types.deployment_state

        out["state"] = capo_appconfig.types.deployment_state.deserialize_json(
            data["State"]
        )
    if data.get("PercentageComplete") is not None:
        out["percentage_complete"] = float(data["PercentageComplete"])
    if data.get("StartedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["started_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["StartedAt"]
        )
    if data.get("CompletedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["completed_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["CompletedAt"]
        )
    if data.get("VersionLabel") is not None:
        out["version_label"] = data["VersionLabel"]
    return out
