"""Generated from Smithy shape ``com.amazonaws.personalize#SolutionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.event_type
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.perform_auto_ml
    import capo_personalize.types.perform_hpo
    import capo_personalize.types.perform_incremental_update
    import capo_personalize.types.solution_config
    import capo_personalize.types.status
    import capo_personalize.types.training_hours
    import capo_personalize.types.training_mode
    import capo_personalize.types.training_type
    import capo_personalize.types.tuned_hpo_params


class SolutionVersion(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the solution version.</p>"""
    solution_version_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the solution version.</p>"""
    solution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the solution.</p>"""
    perform_hpo: "capo_personalize.types.perform_hpo.PerformHPO"
    """<p>Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is <code>false</code>.</p>"""
    perform_auto_ml: "capo_personalize.types.perform_auto_ml.PerformAutoML"
    """<p>When true, Amazon Personalize searches for the most optimal recipe according to the solution configuration. When false (the default), Amazon Personalize uses <code>recipeArn</code>.</p>"""
    perform_incremental_update: NotRequired[
        "capo_personalize.types.perform_incremental_update.PerformIncrementalUpdate"
    ]
    """<p>Whether the solution version should perform an incremental update. When set to true, the training will process only the data that has changed since the latest training, similar to when trainingMode is set to UPDATE. This can only be used with solution versions that use the User-Personalization recipe.</p>"""
    recipe_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The ARN of the recipe used in the solution.</p>"""
    event_type: NotRequired["capo_personalize.types.event_type.EventType"]
    """<p>The event type (for example, 'click' or 'like') that is used for training the model.</p>"""
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group providing the training data.</p>"""
    solution_config: NotRequired[
        "capo_personalize.types.solution_config.SolutionConfig"
    ]
    """<p>Describes the configuration properties for the solution.</p>"""
    training_hours: NotRequired["capo_personalize.types.training_hours.TrainingHours"]
    """<p>The time used to train the model. You are billed for the time it takes to train a model. This field is visible only after Amazon Personalize successfully trains a model.</p>"""
    training_mode: NotRequired["capo_personalize.types.training_mode.TrainingMode"]
    """<p>The scope of training to be performed when creating the solution version. A <code>FULL</code> training considers all of the data in your dataset group. An <code>UPDATE</code> processes only the data that has changed since the latest training. Only solution versions created with the User-Personalization recipe can use <code>UPDATE</code>. </p>"""
    tuned_hpo_params: NotRequired[
        "capo_personalize.types.tuned_hpo_params.TunedHPOParams"
    ]
    """<p>If hyperparameter optimization was performed, contains the hyperparameter values of the best performing model.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the solution version.</p> <p>A solution version can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING</p> </li> <li> <p>CREATE IN_PROGRESS</p> </li> <li> <p>ACTIVE</p> </li> <li> <p>CREATE FAILED</p> </li> <li> <p>CREATE STOPPING</p> </li> <li> <p>CREATE STOPPED</p> </li> </ul>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If training a solution version fails, the reason for the failure.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that this version of the solution was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the solution was last updated.</p>"""
    training_type: NotRequired["capo_personalize.types.training_type.TrainingType"]
    """<p>Whether the solution version was created automatically or manually.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SolutionVersion) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    out["performHPO"] = value.get("perform_hpo", False)
    out["performAutoML"] = value.get("perform_auto_ml", False)
    if "perform_incremental_update" in value:
        out["performIncrementalUpdate"] = value["perform_incremental_update"]
    if "recipe_arn" in value:
        out["recipeArn"] = value["recipe_arn"]
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "solution_config" in value:
        import capo_personalize.types.solution_config

        out["solutionConfig"] = (
            capo_personalize.types.solution_config.serialize_aws_json_1_1(
                value["solution_config"]
            )
        )
    if "training_hours" in value:
        out["trainingHours"] = (
            "NaN"
            if value["training_hours"] != value["training_hours"]
            else "Infinity"
            if value["training_hours"] == float("inf")
            else "-Infinity"
            if value["training_hours"] == float("-inf")
            else value["training_hours"]
        )
    if "training_mode" in value:
        import capo_personalize.types.training_mode

        out["trainingMode"] = (
            capo_personalize.types.training_mode.serialize_aws_json_1_1(
                value["training_mode"]
            )
        )
    if "tuned_hpo_params" in value:
        import capo_personalize.types.tuned_hpo_params

        out["tunedHPOParams"] = (
            capo_personalize.types.tuned_hpo_params.serialize_aws_json_1_1(
                value["tuned_hpo_params"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
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
    if "training_type" in value:
        import capo_personalize.types.training_type

        out["trainingType"] = (
            capo_personalize.types.training_type.serialize_aws_json_1_1(
                value["training_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SolutionVersion:
    out: SolutionVersion = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("solutionVersionArn") is not None:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    if data.get("performHPO") is not None:
        out["perform_hpo"] = data["performHPO"]
    else:
        out["perform_hpo"] = False
    if data.get("performAutoML") is not None:
        out["perform_auto_ml"] = data["performAutoML"]
    else:
        out["perform_auto_ml"] = False
    if data.get("performIncrementalUpdate") is not None:
        out["perform_incremental_update"] = data["performIncrementalUpdate"]
    if data.get("recipeArn") is not None:
        out["recipe_arn"] = data["recipeArn"]
    if data.get("eventType") is not None:
        out["event_type"] = data["eventType"]
    if data.get("datasetGroupArn") is not None:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if data.get("solutionConfig") is not None:
        import capo_personalize.types.solution_config

        out["solution_config"] = (
            capo_personalize.types.solution_config.deserialize_aws_json_1_1(
                data["solutionConfig"]
            )
        )
    if data.get("trainingHours") is not None:
        out["training_hours"] = float(data["trainingHours"])
    if data.get("trainingMode") is not None:
        import capo_personalize.types.training_mode

        out["training_mode"] = (
            capo_personalize.types.training_mode.deserialize_aws_json_1_1(
                data["trainingMode"]
            )
        )
    if data.get("tunedHPOParams") is not None:
        import capo_personalize.types.tuned_hpo_params

        out["tuned_hpo_params"] = (
            capo_personalize.types.tuned_hpo_params.deserialize_aws_json_1_1(
                data["tunedHPOParams"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
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
    if data.get("trainingType") is not None:
        import capo_personalize.types.training_type

        out["training_type"] = (
            capo_personalize.types.training_type.deserialize_aws_json_1_1(
                data["trainingType"]
            )
        )
    return out
