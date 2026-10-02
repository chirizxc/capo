"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.experiment_definition_status
    import capo_appconfig.types.flag_key
    import capo_appconfig.types.id
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.kms_key_identifier
    import capo_appconfig.types.name
    import capo_appconfig.types.rule
    import capo_appconfig.types.treatment
    import capo_appconfig.types.treatment_list


class ExperimentDefinition(TypedDict, closed=True):
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
    """<p>The current status of the experiment definition. Valid values: <code>ACTIVE</code>, <code>IDLE</code>, <code>ARCHIVED</code>.</p>"""
    configuration_profile_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The configuration profile ID associated with the experiment.</p>"""
    environment_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The environment ID where the experiment runs.</p>"""
    flag_key: NotRequired["capo_appconfig.types.flag_key.FlagKey"]
    """<p>The key of the feature flag used by the experiment.</p>"""
    audience_rule: NotRequired["capo_appconfig.types.rule.Rule"]
    """<p>The rule that defines which users are eligible to be assigned to treatments.</p>"""
    audience_description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the intended audience for the experiment.</p>"""
    launch_criteria: NotRequired["capo_appconfig.types.description.Description"]
    """<p>The conditions under which the winning treatment should be launched.</p>"""
    treatments: NotRequired["capo_appconfig.types.treatment_list.TreatmentList"]
    """<p>The list of treatments defined for the experiment.</p>"""
    control: NotRequired["capo_appconfig.types.treatment.Treatment"]
    """<p>The control treatment used as the baseline for comparison.</p>"""
    created_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment definition was created, in ISO 8601 format.</p>"""
    updated_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment definition was last updated, in ISO 8601 format.</p>"""
    kms_key_identifier: NotRequired[
        "capo_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt experiment data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDefinition) -> dict:
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
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> ExperimentDefinition:
    out: ExperimentDefinition = {}  # type: ignore[typeddict-item]
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
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
