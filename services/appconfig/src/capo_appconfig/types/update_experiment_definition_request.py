"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateExperimentDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.identifier
    import capo_appconfig.types.rule
    import capo_appconfig.types.treatment_input
    import capo_appconfig.types.treatment_input_list


class UpdateExperimentDefinitionRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The application ID or name.</p>"""
    experiment_definition_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The experiment definition ID or name.</p>"""
    treatments: NotRequired[
        "capo_appconfig.types.treatment_input_list.TreatmentInputList"
    ]
    """<p>The updated list of treatments to evaluate during the experiment. Each treatment defines a distinct variation compared to the control.</p>"""
    control: NotRequired["capo_appconfig.types.treatment_input.TreatmentInput"]
    """<p>An updated control treatment.</p>"""
    hypothesis: NotRequired["capo_appconfig.types.description.Description"]
    """<p>An updated hypothesis.</p>"""
    audience_rule: NotRequired["capo_appconfig.types.rule.Rule"]
    """<p>An updated audience rule.</p>"""
    audience_description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>An updated audience description.</p>"""
    launch_criteria: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Updated launch criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentDefinitionRequest) -> dict:
    out: dict = {}
    if "treatments" in value:
        import capo_appconfig.types.treatment_input_list

        out["Treatments"] = capo_appconfig.types.treatment_input_list.serialize_json(
            value["treatments"]
        )
    if "control" in value:
        import capo_appconfig.types.treatment_input

        out["Control"] = capo_appconfig.types.treatment_input.serialize_json(
            value["control"]
        )
    if "hypothesis" in value:
        out["Hypothesis"] = value["hypothesis"]
    if "audience_rule" in value:
        out["AudienceRule"] = value["audience_rule"]
    if "audience_description" in value:
        out["AudienceDescription"] = value["audience_description"]
    if "launch_criteria" in value:
        out["LaunchCriteria"] = value["launch_criteria"]
    return out


def deserialize_json(data: dict) -> UpdateExperimentDefinitionRequest:
    out: UpdateExperimentDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Treatments") is not None:
        import capo_appconfig.types.treatment_input_list

        out["treatments"] = capo_appconfig.types.treatment_input_list.deserialize_json(
            data["Treatments"]
        )
    if data.get("Control") is not None:
        import capo_appconfig.types.treatment_input

        out["control"] = capo_appconfig.types.treatment_input.deserialize_json(
            data["Control"]
        )
    if data.get("Hypothesis") is not None:
        out["hypothesis"] = data["Hypothesis"]
    if data.get("AudienceRule") is not None:
        out["audience_rule"] = data["AudienceRule"]
    if data.get("AudienceDescription") is not None:
        out["audience_description"] = data["AudienceDescription"]
    if data.get("LaunchCriteria") is not None:
        out["launch_criteria"] = data["LaunchCriteria"]
    return out
