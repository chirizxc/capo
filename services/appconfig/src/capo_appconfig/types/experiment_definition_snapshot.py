"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentDefinitionSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.flag_key
    import capo_appconfig.types.id
    import capo_appconfig.types.name
    import capo_appconfig.types.rule
    import capo_appconfig.types.treatment
    import capo_appconfig.types.treatment_list


class ExperimentDefinitionSnapshot(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID at the time the run was started.</p>"""
    id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The experiment definition ID.</p>"""
    name: NotRequired["capo_appconfig.types.name.Name"]
    """<p>The name of the experiment definition at the time the run was started.</p>"""
    hypothesis: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The hypothesis at the time the run was started.</p>"""
    configuration_profile_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID at the time the run was started.</p>"""
    environment_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The environment ID at the time the run was started.</p>"""
    flag_key: NotRequired["capo_appconfig.types.flag_key.FlagKey"]
    """<p>The feature flag key at the time the run was started.</p>"""
    audience_rule: NotRequired["capo_appconfig.types.rule.Rule"]
    """<p>The audience rule at the time the run was started.</p>"""
    audience_description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The audience description at the time the run was started.</p>"""
    launch_criteria: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The launch criteria at the time the run was started.</p>"""
    treatments: NotRequired["capo_appconfig.types.treatment_list.TreatmentList"]
    """<p>The treatments at the time the run was started.</p>"""
    control: NotRequired["capo_appconfig.types.treatment.Treatment"]
    """<p>The control treatment at the time the run was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDefinitionSnapshot) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "hypothesis" in value:
        out["Hypothesis"] = value["hypothesis"]
    if "configuration_profile_id" in value:
        out["ConfigurationProfileId"] = value["configuration_profile_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "flag_key" in value:
        out["FlagKey"] = value["flag_key"]
    if "audience_rule" in value:
        out["AudienceRule"] = value["audience_rule"]
    if "audience_description" in value:
        out["AudienceDescription"] = value["audience_description"]
    if "launch_criteria" in value:
        out["LaunchCriteria"] = value["launch_criteria"]
    if "treatments" in value:
        import capo_appconfig.types.treatment_list

        out["Treatments"] = capo_appconfig.types.treatment_list.serialize_json(
            value["treatments"]
        )
    if "control" in value:
        import capo_appconfig.types.treatment

        out["Control"] = capo_appconfig.types.treatment.serialize_json(value["control"])
    return out


def deserialize_json(data: dict) -> ExperimentDefinitionSnapshot:
    out: ExperimentDefinitionSnapshot = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Hypothesis") is not None:
        out["hypothesis"] = data["Hypothesis"]
    if data.get("ConfigurationProfileId") is not None:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    if data.get("EnvironmentId") is not None:
        out["environment_id"] = data["EnvironmentId"]
    if data.get("FlagKey") is not None:
        out["flag_key"] = data["FlagKey"]
    if data.get("AudienceRule") is not None:
        out["audience_rule"] = data["AudienceRule"]
    if data.get("AudienceDescription") is not None:
        out["audience_description"] = data["AudienceDescription"]
    if data.get("LaunchCriteria") is not None:
        out["launch_criteria"] = data["LaunchCriteria"]
    if data.get("Treatments") is not None:
        import capo_appconfig.types.treatment_list

        out["treatments"] = capo_appconfig.types.treatment_list.deserialize_json(
            data["Treatments"]
        )
    if data.get("Control") is not None:
        import capo_appconfig.types.treatment

        out["control"] = capo_appconfig.types.treatment.deserialize_json(
            data["Control"]
        )
    return out
