"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.experiment_definition_status
    import capo_appconfig.types.flag_key
    import capo_appconfig.types.id
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.name


class ExperimentDefinitionSummary(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The experiment definition ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the experiment definition.</p>"""
    hypothesis: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The hypothesis that the experiment is designed to validate.</p>"""
    status: NotRequired[
        "capo_appconfig.types.experiment_definition_status.ExperimentDefinitionStatus"
    ]
    """<p>The current status of the experiment definition.</p>"""
    configuration_profile_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID associated with the experiment.</p>"""
    environment_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The environment ID where the experiment runs.</p>"""
    flag_key: NotRequired["capo_appconfig.types.flag_key.FlagKey"]
    """<p>The key of the feature flag used by the experiment.</p>"""
    created_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment definition was created, in ISO 8601 format.</p>"""
    updated_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment definition was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDefinitionSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "hypothesis" in value:
        out["Hypothesis"] = value["hypothesis"]
    if "status" in value:
        import capo_appconfig.types.experiment_definition_status

        out["Status"] = (
            capo_appconfig.types.experiment_definition_status.serialize_json(
                value["status"]
            )
        )
    if "configuration_profile_id" in value:
        out["ConfigurationProfileId"] = value["configuration_profile_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "flag_key" in value:
        out["FlagKey"] = value["flag_key"]
    if "created_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["CreatedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["UpdatedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ExperimentDefinitionSummary:
    out: ExperimentDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Hypothesis") is not None:
        out["hypothesis"] = data["Hypothesis"]
    if data.get("Status") is not None:
        import capo_appconfig.types.experiment_definition_status

        out["status"] = (
            capo_appconfig.types.experiment_definition_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ConfigurationProfileId") is not None:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("FlagKey") is not None:
        out["flag_key"] = data["FlagKey"]
    if data.get("CreatedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["created_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["updated_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["UpdatedAt"]
        )
    return out
