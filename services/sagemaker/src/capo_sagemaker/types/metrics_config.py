"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enable_detailed_observability
    import capo_sagemaker.types.enable_enhanced_metrics
    import capo_sagemaker.types.metric_publish_frequency_in_seconds


class MetricsConfig(TypedDict, closed=True):
    enable_enhanced_metrics: NotRequired[
        "capo_sagemaker.types.enable_enhanced_metrics.EnableEnhancedMetrics"
    ]
    """<p>Specifies whether to enable enhanced metrics for the endpoint. Enhanced metrics provide utilization and invocation data at instance and container granularity. Container granularity is supported for Inference Components. The default is <code>False</code>.</p>"""
    enable_detailed_observability: NotRequired[
        "capo_sagemaker.types.enable_detailed_observability.EnableDetailedObservability"
    ]
    """<p>Indicates whether detailed observability is enabled for the endpoint. When set to <code>True</code>, the following metrics are published at the configured frequency:</p> <ul> <li> <p>Container-level inference metrics scraped from the container's Prometheus endpoint (such as request latency, error counts, and throughput). Available metrics vary by framework.</p> </li> <li> <p>Per-GPU metrics (utilization, memory, and temperature) attributed to individual inference components.</p> </li> <li> <p>Per-instance host metrics (CPU, memory, and disk utilization).</p> </li> <li> <p>Inference component placement metrics (copy count per Availability Zone).</p> </li> </ul> <p>For first-party and Deep Learning Containers (DLC), the Prometheus endpoint path is determined automatically. For Bring-Your-Own-Container (BYOC) cases, you can optionally set <code>ContainerMetricsConfig</code> to specify a custom endpoint path. If not specified, the default path <code>/metrics</code> on port <code>8080</code> is used.</p> <p>When set to <code>False</code>, these additional metrics are not published. Standard invocation and utilization metrics controlled by <code>EnableEnhancedMetrics</code> are unaffected.</p> <p>The default value for new endpoint configurations is <code>True</code>. For existing endpoint configurations created before this feature, the value is <code>False</code> unless explicitly set.</p>"""
    metric_publish_frequency_in_seconds: NotRequired[
        "capo_sagemaker.types.metric_publish_frequency_in_seconds.MetricPublishFrequencyInSeconds"
    ]
    """<p>The interval, in seconds, at which metrics are published to Amazon CloudWatch. Defaults to <code>60</code>. Valid values: <code>10</code>, <code>30</code>, <code>60</code>, <code>120</code>, <code>180</code>, <code>240</code>, <code>300</code>.</p> <p>When <code>EnableEnhancedMetrics</code> is set to <code>False</code>, this interval applies to utilization metrics only. Invocation metrics continue to be published at the default 60-second interval. When <code>EnableEnhancedMetrics</code> is set to <code>True</code>, this interval applies to both utilization and invocation metrics.</p> <p>When <code>EnableDetailedObservability</code> is set to <code>True</code>, this interval applies to per-GPU metrics, per-instance host metrics, container metrics, and fleet-level inference component lifecycle and placement metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsConfig) -> dict:
    out: dict = {}
    if "enable_enhanced_metrics" in value:
        out["EnableEnhancedMetrics"] = value["enable_enhanced_metrics"]
    if "enable_detailed_observability" in value:
        out["EnableDetailedObservability"] = value["enable_detailed_observability"]
    if "metric_publish_frequency_in_seconds" in value:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["MetricPublishFrequencyInSeconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.serialize_aws_json_1_1(
                value["metric_publish_frequency_in_seconds"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricsConfig:
    out: MetricsConfig = {}  # type: ignore[typeddict-item]
    if data.get("EnableEnhancedMetrics") is not None:
        out["enable_enhanced_metrics"] = data["EnableEnhancedMetrics"]
    if data.get("EnableDetailedObservability") is not None:
        out["enable_detailed_observability"] = data["EnableDetailedObservability"]
    if data.get("MetricPublishFrequencyInSeconds") is not None:
        import capo_sagemaker.types.metric_publish_frequency_in_seconds

        out["metric_publish_frequency_in_seconds"] = (
            capo_sagemaker.types.metric_publish_frequency_in_seconds.deserialize_aws_json_1_1(
                data["MetricPublishFrequencyInSeconds"]
            )
        )
    return out
