"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Source``."""

from typing import Literal, TypeAlias, cast

"""Data source enum for context graph queries."""
Source: TypeAlias = Literal[
    "VPC_FLOW_LOG",
    "CLOUDTRAIL",
    "IAM_POLICY",
    "CODE_SEMANTICS",
    "TELEMETRY",
    "AZURE_VNET_FLOW_LOG",
    "ELB_ACCESS_LOG",
    "CLOUDFRONT_ACCESS_LOG",
    "S3_ACCESS_LOG",
    "WAF_ACCESS_LOG",
    "AWS_INTEGRATION",
    "CONFIG",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Source) -> str:
    return value


def deserialize_cbor(data: str) -> Source:
    return cast(Source, data)
