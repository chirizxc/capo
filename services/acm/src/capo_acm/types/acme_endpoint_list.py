"""Generated from Smithy shape ``com.amazonaws.acm#AcmeEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_summary

AcmeEndpointList: TypeAlias = list[
    "capo_acm.types.acme_endpoint_summary.AcmeEndpointSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcmeEndpointList) -> list:
    import capo_acm.types.acme_endpoint_summary

    out: list = []
    for item in value:
        out.append(capo_acm.types.acme_endpoint_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AcmeEndpointList:
    import capo_acm.types.acme_endpoint_summary

    out: AcmeEndpointList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_acm.types.acme_endpoint_summary.deserialize_aws_json_1_1(item))
    return out
