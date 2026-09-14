"""Generated from Smithy shape ``com.amazonaws.personalize#Algorithm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.algorithm_image
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.default_hyper_parameter_ranges
    import capo_personalize.types.hyper_parameters
    import capo_personalize.types.name
    import capo_personalize.types.resource_config
    import capo_personalize.types.training_input_mode


class Algorithm(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the algorithm.</p>"""
    algorithm_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm.</p>"""
    algorithm_image: NotRequired[
        "capo_personalize.types.algorithm_image.AlgorithmImage"
    ]
    """<p>The URI of the Docker container for the algorithm image.</p>"""
    default_hyper_parameters: NotRequired[
        "capo_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>Specifies the default hyperparameters.</p>"""
    default_hyper_parameter_ranges: NotRequired[
        "capo_personalize.types.default_hyper_parameter_ranges.DefaultHyperParameterRanges"
    ]
    """<p>Specifies the default hyperparameters, their ranges, and whether they are tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).</p>"""
    default_resource_config: NotRequired[
        "capo_personalize.types.resource_config.ResourceConfig"
    ]
    """<p>Specifies the default maximum number of training jobs and parallel training jobs.</p>"""
    training_input_mode: NotRequired[
        "capo_personalize.types.training_input_mode.TrainingInputMode"
    ]
    """<p>The training input mode.</p>"""
    role_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role.</p>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the algorithm was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the algorithm was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Algorithm) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "algorithm_arn" in value:
        out["algorithmArn"] = value["algorithm_arn"]
    if "algorithm_image" in value:
        import capo_personalize.types.algorithm_image

        out["algorithmImage"] = (
            capo_personalize.types.algorithm_image.serialize_aws_json_1_1(
                value["algorithm_image"]
            )
        )
    if "default_hyper_parameters" in value:
        import capo_personalize.types.hyper_parameters

        out["defaultHyperParameters"] = (
            capo_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["default_hyper_parameters"]
            )
        )
    if "default_hyper_parameter_ranges" in value:
        import capo_personalize.types.default_hyper_parameter_ranges

        out["defaultHyperParameterRanges"] = (
            capo_personalize.types.default_hyper_parameter_ranges.serialize_aws_json_1_1(
                value["default_hyper_parameter_ranges"]
            )
        )
    if "default_resource_config" in value:
        import capo_personalize.types.resource_config

        out["defaultResourceConfig"] = (
            capo_personalize.types.resource_config.serialize_aws_json_1_1(
                value["default_resource_config"]
            )
        )
    if "training_input_mode" in value:
        out["trainingInputMode"] = value["training_input_mode"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> Algorithm:
    out: Algorithm = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("algorithmArn") is not None:
        out["algorithm_arn"] = data["algorithmArn"]
    if data.get("algorithmImage") is not None:
        import capo_personalize.types.algorithm_image

        out["algorithm_image"] = (
            capo_personalize.types.algorithm_image.deserialize_aws_json_1_1(
                data["algorithmImage"]
            )
        )
    if data.get("defaultHyperParameters") is not None:
        import capo_personalize.types.hyper_parameters

        out["default_hyper_parameters"] = (
            capo_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["defaultHyperParameters"]
            )
        )
    if data.get("defaultHyperParameterRanges") is not None:
        import capo_personalize.types.default_hyper_parameter_ranges

        out["default_hyper_parameter_ranges"] = (
            capo_personalize.types.default_hyper_parameter_ranges.deserialize_aws_json_1_1(
                data["defaultHyperParameterRanges"]
            )
        )
    if data.get("defaultResourceConfig") is not None:
        import capo_personalize.types.resource_config

        out["default_resource_config"] = (
            capo_personalize.types.resource_config.deserialize_aws_json_1_1(
                data["defaultResourceConfig"]
            )
        )
    if data.get("trainingInputMode") is not None:
        out["training_input_mode"] = data["trainingInputMode"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
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
    return out
