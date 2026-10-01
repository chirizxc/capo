"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.experiment_run_status
    import capo_appconfig.types.id
    import capo_appconfig.types.integer
    import capo_appconfig.types.iso8601_date_time


class ExperimentRunSummary(TypedDict, closed=True):
    experiment_definition_id: NotRequired["capo_appconfig.types.id.Id"]
    """<p>The experiment definition ID.</p>"""
    run: "capo_appconfig.types.integer.Integer"
    """<p>The experiment run number.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the experiment run.</p>"""
    status: NotRequired[
        "capo_appconfig.types.experiment_run_status.ExperimentRunStatus"
    ]
    """<p>The current status of the experiment run.</p>"""
    started_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run started, in ISO 8601 format.</p>"""
    updated_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run was last updated, in ISO 8601 format.</p>"""
    ended_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the experiment run ended, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> ExperimentRunSummary:
    out: ExperimentRunSummary = {}  # type: ignore[typeddict-item]
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
    return out
