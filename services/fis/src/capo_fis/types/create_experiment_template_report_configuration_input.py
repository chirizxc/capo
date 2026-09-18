"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateReportConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_report_configuration_data_sources_input
    import capo_fis.types.experiment_template_report_configuration_outputs_input
    import capo_fis.types.report_configuration_duration


class CreateExperimentTemplateReportConfigurationInput(TypedDict, closed=True):
    outputs: NotRequired[
        "capo_fis.types.experiment_template_report_configuration_outputs_input.ExperimentTemplateReportConfigurationOutputsInput"
    ]
    """<p>The output destinations of the experiment report. </p>"""
    data_sources: NotRequired[
        "capo_fis.types.experiment_template_report_configuration_data_sources_input.ExperimentTemplateReportConfigurationDataSourcesInput"
    ]
    """<p>The data sources for the experiment report.</p>"""
    pre_experiment_duration: NotRequired[
        "capo_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration before the experiment start time for the data sources to include in the report. </p>"""
    post_experiment_duration: NotRequired[
        "capo_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration after the experiment end time for the data sources to include in the report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateReportConfigurationInput) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_fis.types.experiment_template_report_configuration_outputs_input

        out["outputs"] = (
            capo_fis.types.experiment_template_report_configuration_outputs_input.serialize_json(
                value["outputs"]
            )
        )
    if "data_sources" in value:
        import capo_fis.types.experiment_template_report_configuration_data_sources_input

        out["dataSources"] = (
            capo_fis.types.experiment_template_report_configuration_data_sources_input.serialize_json(
                value["data_sources"]
            )
        )
    if "pre_experiment_duration" in value:
        out["preExperimentDuration"] = value["pre_experiment_duration"]
    if "post_experiment_duration" in value:
        out["postExperimentDuration"] = value["post_experiment_duration"]
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateReportConfigurationInput:
    out: CreateExperimentTemplateReportConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("outputs") is not None:
        import capo_fis.types.experiment_template_report_configuration_outputs_input

        out["outputs"] = (
            capo_fis.types.experiment_template_report_configuration_outputs_input.deserialize_json(
                data["outputs"]
            )
        )
    if data.get("dataSources") is not None:
        import capo_fis.types.experiment_template_report_configuration_data_sources_input

        out["data_sources"] = (
            capo_fis.types.experiment_template_report_configuration_data_sources_input.deserialize_json(
                data["dataSources"]
            )
        )
    if data.get("preExperimentDuration") is not None:
        out["pre_experiment_duration"] = data["preExperimentDuration"]
    if data.get("postExperimentDuration") is not None:
        out["post_experiment_duration"] = data["postExperimentDuration"]
    return out
