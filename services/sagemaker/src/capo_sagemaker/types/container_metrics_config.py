"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerMetricsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.metrics_endpoint_list


class ContainerMetricsConfig(TypedDict, closed=True):
    metrics_endpoints: NotRequired[
        "capo_sagemaker.types.metrics_endpoint_list.MetricsEndpointList"
    ]
    """<p>A list of metrics endpoints to scrape from the container. Each endpoint specifies the path where the container exposes Prometheus-formatted metrics and the frequency at which to publish them. You can specify a maximum of 1 endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMetricsConfig) -> dict:
    out: dict = {}
    if "metrics_endpoints" in value:
        import capo_sagemaker.types.metrics_endpoint_list

        out["MetricsEndpoints"] = (
            capo_sagemaker.types.metrics_endpoint_list.serialize_aws_json_1_1(
                value["metrics_endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerMetricsConfig:
    out: ContainerMetricsConfig = {}  # type: ignore[typeddict-item]
    if data.get("MetricsEndpoints") is not None:
        import capo_sagemaker.types.metrics_endpoint_list

        out["metrics_endpoints"] = (
            capo_sagemaker.types.metrics_endpoint_list.deserialize_aws_json_1_1(
                data["MetricsEndpoints"]
            )
        )
    return out
