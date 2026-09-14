"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.float
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.model_setup_time
    import capo_sagemaker.types.utilization_metric


class RecommendationMetrics(TypedDict, closed=True):
    cost_per_hour: NotRequired["capo_sagemaker.types.float.Float"]
    """<p>Defines the cost per hour for the instance. </p>"""
    cost_per_inference: NotRequired["capo_sagemaker.types.float.Float"]
    """<p>Defines the cost per inference for the instance .</p>"""
    max_invocations: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The expected maximum number of requests per minute for the instance.</p>"""
    model_latency: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The expected model latency at maximum invocation per minute for the instance.</p>"""
    cpu_utilization: NotRequired[
        "capo_sagemaker.types.utilization_metric.UtilizationMetric"
    ]
    """<p>The expected CPU utilization at maximum invocations per minute for the instance.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""
    memory_utilization: NotRequired[
        "capo_sagemaker.types.utilization_metric.UtilizationMetric"
    ]
    """<p>The expected memory utilization at maximum invocations per minute for the instance.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""
    model_setup_time: NotRequired[
        "capo_sagemaker.types.model_setup_time.ModelSetupTime"
    ]
    """<p>The time it takes to launch new compute resources for a serverless endpoint. The time can vary depending on the model size, how long it takes to download the model, and the start-up time of the container.</p> <p> <code>NaN</code> indicates that the value is not available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationMetrics) -> dict:
    out: dict = {}
    if "cost_per_hour" in value:
        out["CostPerHour"] = (
            "NaN"
            if value["cost_per_hour"] != value["cost_per_hour"]
            else "Infinity"
            if value["cost_per_hour"] == float("inf")
            else "-Infinity"
            if value["cost_per_hour"] == float("-inf")
            else value["cost_per_hour"]
        )
    if "cost_per_inference" in value:
        out["CostPerInference"] = (
            "NaN"
            if value["cost_per_inference"] != value["cost_per_inference"]
            else "Infinity"
            if value["cost_per_inference"] == float("inf")
            else "-Infinity"
            if value["cost_per_inference"] == float("-inf")
            else value["cost_per_inference"]
        )
    if "max_invocations" in value:
        out["MaxInvocations"] = value["max_invocations"]
    if "model_latency" in value:
        out["ModelLatency"] = value["model_latency"]
    if "cpu_utilization" in value:
        out["CpuUtilization"] = (
            "NaN"
            if value["cpu_utilization"] != value["cpu_utilization"]
            else "Infinity"
            if value["cpu_utilization"] == float("inf")
            else "-Infinity"
            if value["cpu_utilization"] == float("-inf")
            else value["cpu_utilization"]
        )
    if "memory_utilization" in value:
        out["MemoryUtilization"] = (
            "NaN"
            if value["memory_utilization"] != value["memory_utilization"]
            else "Infinity"
            if value["memory_utilization"] == float("inf")
            else "-Infinity"
            if value["memory_utilization"] == float("-inf")
            else value["memory_utilization"]
        )
    if "model_setup_time" in value:
        out["ModelSetupTime"] = value["model_setup_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationMetrics:
    out: RecommendationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("CostPerHour") is not None:
        out["cost_per_hour"] = float(data["CostPerHour"])
    if data.get("CostPerInference") is not None:
        out["cost_per_inference"] = float(data["CostPerInference"])
    if data.get("MaxInvocations") is not None:
        out["max_invocations"] = data["MaxInvocations"]
    if data.get("ModelLatency") is not None:
        out["model_latency"] = data["ModelLatency"]
    if data.get("CpuUtilization") is not None:
        out["cpu_utilization"] = float(data["CpuUtilization"])
    if data.get("MemoryUtilization") is not None:
        out["memory_utilization"] = float(data["MemoryUtilization"])
    if data.get("ModelSetupTime") is not None:
        out["model_setup_time"] = data["ModelSetupTime"]
    return out
