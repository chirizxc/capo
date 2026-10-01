"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricsEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.metrics_endpoint

MetricsEndpointList: TypeAlias = list[
    "capo_sagemaker.types.metrics_endpoint.MetricsEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsEndpointList) -> list:
    import capo_sagemaker.types.metrics_endpoint

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.metrics_endpoint.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricsEndpointList:
    import capo_sagemaker.types.metrics_endpoint

    out: MetricsEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_sagemaker.types.metrics_endpoint.deserialize_aws_json_1_1(item))
    return out
