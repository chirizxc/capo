"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.arn
    import capo_appconfig.types.description
    import capo_appconfig.types.experiment_run_event_type
    import capo_appconfig.types.iso8601_date_time
    import capo_appconfig.types.nullable_percentage
    import capo_appconfig.types.treatment_overrides
    import capo_appconfig.types.triggered_by


class ExperimentRunEvent(TypedDict, closed=True):
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the event.</p>"""
    associated_deployment: NotRequired["capo_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the deployment associated with this event.</p>"""
    event_type: NotRequired[
        "capo_appconfig.types.experiment_run_event_type.ExperimentRunEventType"
    ]
    """<p>The type of event. Valid values: <code>RUN_STARTED</code>, <code>EXPOSURE_UPDATED</code>, <code>OVERRIDES_UPDATED</code>, <code>RUN_STOPPED</code>.</p>"""
    occurred_at: NotRequired["capo_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The date and time the event occurred, in ISO 8601 format.</p>"""
    triggered_by: NotRequired["capo_appconfig.types.triggered_by.TriggeredBy"]
    """<p>The principal that triggered the event.</p>"""
    exposure_percentage: NotRequired[
        "capo_appconfig.types.nullable_percentage.NullablePercentage"
    ]
    """<p>The exposure percentage at the time of the event.</p>"""
    treatment_overrides: NotRequired[
        "capo_appconfig.types.treatment_overrides.TreatmentOverrides"
    ]
    """<p>The treatment overrides at the time of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunEvent) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "associated_deployment" in value:
        out["AssociatedDeployment"] = value["associated_deployment"]
    if "event_type" in value:
        import capo_appconfig.types.experiment_run_event_type

        out["EventType"] = (
            capo_appconfig.types.experiment_run_event_type.serialize_json(
                value["event_type"]
            )
        )
    if "occurred_at" in value:
        import capo_appconfig.types.iso8601_date_time

        out["OccurredAt"] = capo_appconfig.types.iso8601_date_time.serialize_json(
            value["occurred_at"]
        )
    if "triggered_by" in value:
        import capo_appconfig.types.triggered_by

        out["TriggeredBy"] = capo_appconfig.types.triggered_by.serialize_json(
            value["triggered_by"]
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
    return out


def deserialize_json(data: dict) -> ExperimentRunEvent:
    out: ExperimentRunEvent = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AssociatedDeployment") is not None:
        out["associated_deployment"] = data["AssociatedDeployment"]
    if data.get("EventType") is not None:
        import capo_appconfig.types.experiment_run_event_type

        out["event_type"] = (
            capo_appconfig.types.experiment_run_event_type.deserialize_json(
                data["EventType"]
            )
        )
    if data.get("OccurredAt") is not None:
        import capo_appconfig.types.iso8601_date_time

        out["occurred_at"] = capo_appconfig.types.iso8601_date_time.deserialize_json(
            data["OccurredAt"]
        )
    if data.get("TriggeredBy") is not None:
        import capo_appconfig.types.triggered_by

        out["triggered_by"] = capo_appconfig.types.triggered_by.deserialize_json(
            data["TriggeredBy"]
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
    return out
