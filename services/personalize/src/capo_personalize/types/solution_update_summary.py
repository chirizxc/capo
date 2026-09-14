"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.perform_auto_training
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.solution_update_config
    import capo_personalize.types.status


class SolutionUpdateSummary(TypedDict, closed=True):
    solution_update_config: NotRequired[
        "capo_personalize.types.solution_update_config.SolutionUpdateConfig"
    ]
    """<p>The configuration details of the solution.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the solution update. A solution update can be in one of the following states:</p> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p>"""
    perform_auto_training: NotRequired[
        "capo_personalize.types.perform_auto_training.PerformAutoTraining"
    ]
    """<p>Whether the solution automatically creates solution versions.</p>"""
    perform_incremental_update: NotRequired[
        "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the solution update was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution update was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a solution update fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionUpdateSummary) -> dict:
    out: dict = {}
    if "solution_update_config" in value:
        import capo_personalize.types.solution_update_config

        out["solutionUpdateConfig"] = (
            capo_personalize.types.solution_update_config.serialize_aws_json_1_1(
                value["solution_update_config"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "perform_auto_training" in value:
        out["performAutoTraining"] = value["perform_auto_training"]
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionUpdateSummary:
    out: SolutionUpdateSummary = {}  # type: ignore[typeddict-item]
    if data.get("solutionUpdateConfig") is not None:
        import capo_personalize.types.solution_update_config

        out["solution_update_config"] = (
            capo_personalize.types.solution_update_config.deserialize_aws_json_1_1(
                data["solutionUpdateConfig"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("performAutoTraining") is not None:
        out["perform_auto_training"] = data["performAutoTraining"]
    if data.get("performIncrementalUpdate") is not None:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
    if data.get("creationDateTime") is not None:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if data.get("lastUpdatedDateTime") is not None:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
