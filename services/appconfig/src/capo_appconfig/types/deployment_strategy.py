"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.growth_type
    import capo_appconfig.types.id
    import capo_appconfig.types.minutes_between0_and24_hours
    import capo_appconfig.types.name
    import capo_appconfig.types.percentage
    import capo_appconfig.types.replicate_to


class DeploymentStrategy(TypedDict, closed=True):
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The deployment strategy ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the deployment strategy.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The description of the deployment strategy.</p>"""
    deployment_duration_in_minutes: (
        "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>Total amount of time the deployment lasted.</p>"""
    growth_type: NotRequired["capo_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grew over time.</p>"""
    growth_factor: NotRequired["capo_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets that received a deployed configuration during each interval.</p>"""
    final_bake_time_in_minutes: (
        "capo_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>The amount of time that AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>"""
    replicate_to: NotRequired["capo_appconfig.types.replicate_to.ReplicateTo"]
    """<p>Save the deployment strategy to a Systems Manager (SSM) document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategy) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "replicate_to" in value:
        import capo_appconfig.types.replicate_to

        out["ReplicateTo"] = capo_appconfig.types.replicate_to.serialize_json(
            value["replicate_to"]
        )
    return out


def deserialize_json(data: dict) -> DeploymentStrategy:
    out: DeploymentStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("ReplicateTo") is not None:
        import capo_appconfig.types.replicate_to

        out["replicate_to"] = capo_appconfig.types.replicate_to.deserialize_json(
            data["ReplicateTo"]
        )
    return out
