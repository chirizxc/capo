"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricsEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metric_publish_frequency_in_seconds
    import capo_sagemaker.types.metrics_endpoint_path


class MetricsEndpoint(TypedDict, closed=True):
    metrics_endpoint_path: NotRequired[
        "capo_sagemaker.types.metrics_endpoint_path.MetricsEndpointPath"
    ]
    """<p>The path to the metrics endpoint exposed by the container. For example, <code>/metrics</code> or <code>/server/metrics</code>. The path must start with <code>/</code> and can contain alphanumeric characters, forward slashes, underscores, hyphens, and periods. Maximum length is 256 characters. If not specified, defaults to <code>/metrics</code>.</p>"""
    metric_publish_frequency_in_seconds: NotRequired[
        "capo_sagemaker.types.metric_publish_frequency_in_seconds.MetricPublishFrequencyInSeconds"
    ]
    """<p>The interval, in seconds, at which container metrics scraped from the endpoint are published to Amazon CloudWatch. Valid values: <code>10</code>, <code>30</code>, <code>60</code>, <code>120</code>, <code>180</code>, <code>240</code>, <code>300</code>. Defaults to <code>60</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsEndpoint) -> dict:
    out: dict = {}
    if "metrics_endpoint_path" in value:
        out["MetricsEndpointPath"] = value["metrics_endpoint_path"]
    if "metric_publish_frequency_in_seconds" in value:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["MetricPublishFrequencyInSeconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.serialize_aws_json_1_1(
                value["metric_publish_frequency_in_seconds"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricsEndpoint:
    out: MetricsEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("MetricsEndpointPath") is not None:
        out["metrics_endpoint_path"] = data["MetricsEndpointPath"]
    if data.get("MetricPublishFrequencyInSeconds") is not None:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["metric_publish_frequency_in_seconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.deserialize_aws_json_1_1(
                data["MetricPublishFrequencyInSeconds"]
            )
        )
    return out
