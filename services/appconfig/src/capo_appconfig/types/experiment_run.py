"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.experiment_definition_snapshot
    import capo_appconfig.types.experiment_run_result
    import capo_appconfig.types.experiment_run_status
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.nullable_percentage
    import capo_appconfig.types.treatment_overrides


class ExperimentRun(TypedDict, closed=True):
    application_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    experiment_definition_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The experiment definition ID.</p>"""
    run: "capo_appconfig.types.integer.Integer"
    """<p>The experiment run number.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the experiment run.</p>"""
    status: NotRequired[
        "capo_appconfig.types.experiment_run_status.ExperimentRunStatus"
    ]
    """<p>The current status of the experiment run. Valid values: <code>RUNNING</code>, <code>DONE</code>.</p>"""
    exposure_percentage: NotRequired[
        "capo_appconfig.types.nullable_percentage.NullablePercentage"
    ]
    """<p>The percentage of the target audience exposed to treatments.</p>"""
    treatment_overrides: NotRequired[
        "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
    ]
    """<p>Treatment assignment overrides that assign specific entity IDs to treatments.</p>"""
    result: NotRequired[
        "capo_appconfig.types.experiment_run_result.ExperimentRunResult"
    ]
    """<p>The result of the experiment run, including the executive summary and launch decision rationale.</p>"""
    started_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run started, in ISO 8601 format.</p>"""
    updated_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run was last updated, in ISO 8601 format.</p>"""
    ended_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run ended, in ISO 8601 format.</p>"""
    experiment_definition_snapshot: NotRequired[
        "capo_appconfig.types.experiment_definition_snapshot.ExperimentDefinitionSnapshot"
    ]
    """<p>A snapshot of the experiment definition at the time the run was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRun) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "experiment_definition_id" in value:
        out["ExperimentDefinitionId"] = value["experiment_definition_id"]
    out["Run"] = value.get("run", 0)
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_appconfig.types.experiment_run_status

        out["Status"] = capo_appconfig.types.experiment_run_status.serialize_json(
            value["status"]
        )
    if "exposure_percentage" in value:
        out["ExposurePercentage"] = (
            "NaN"
            if value["exposure_percentage"] != value["exposure_percentage"]
            else "Infinity"
            if value["exposure_percentage"] == float("inf")
            else "-Infinity"
            if value["exposure_percentage"] == float("-inf")
            else value["exposure_percentage"]
        )
    if "treatment_overrides" in value:
        import capo_appconfig.types.treatment_overrides

        out["TreatmentOverrides"] = (
            capo_appconfig.types.treatment_overrides.serialize_json(
                value["treatment_overrides"]
            )
        )
    if "result" in value:
        import capo_appconfig.types.experiment_run_result

        out["Result"] = capo_appconfig.types.experiment_run_result.serialize_json(
            value["result"]
        )
    if "started_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["StartedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["started_at"]
        )
    if "updated_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["UpdatedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["updated_at"]
        )
    if "ended_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["EndedAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["ended_at"]
        )
    if "experiment_definition_snapshot" in value:
        import capo_appconfig.types.experiment_definition_snapshot

        out["ExperimentDefinitionSnapshot"] = (
            capo_appconfig.types.experiment_definition_snapshot.serialize_json(
                value["experiment_definition_snapshot"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentRun:
    out: ExperimentRun = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ExperimentDefinitionId") is not None:
        out["experiment_definition_id"] = data["ExperimentDefinitionId"]
    if data.get("Run") is not None:
        out["run"] = data["Run"]
    else:
        out["run"] = 0
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_appconfig.types.experiment_run_status

        out["status"] = capo_appconfig.types.experiment_run_status.deserialize_json(
            data["Status"]
        )
    if data.get("ExposurePercentage") is not None:
        out["exposure_percentage"] = float(data["ExposurePercentage"])
    if data.get("TreatmentOverrides") is not None:
        import capo_appconfig.types.treatment_overrides

        out["treatment_overrides"] = (
            capo_appconfig.types.treatment_overrides.deserialize_json(
                data["TreatmentOverrides"]
            )
        )
    if data.get("Result") is not None:
        import capo_appconfig.types.experiment_run_result

        out["result"] = capo_appconfig.types.experiment_run_result.deserialize_json(
            data["Result"]
        )
    if data.get("StartedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["started_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["StartedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["updated_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["UpdatedAt"]
        )
    if data.get("EndedAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["ended_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["EndedAt"]
        )
    if data.get("ExperimentDefinitionSnapshot") is not None:
        import capo_appconfig.types.experiment_definition_snapshot

        out["experiment_definition_snapshot"] = (
            capo_appconfig.types.experiment_definition_snapshot.deserialize_json(
                data["ExperimentDefinitionSnapshot"]
            )
        )
    return out
