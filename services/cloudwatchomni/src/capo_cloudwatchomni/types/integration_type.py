"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IntegrationType``."""

from typing import Literal, TypeAlias, cast

"""The type of external system that an integration connects to, such as a source of configuration data, a messaging destination, or a model provider."""
IntegrationType: TypeAlias = Literal[
    "AWS_CONFIG_SLREC",
    "SLACK",
    "EXTERNAL_AGENT",
    "AWS_INTEGRATION",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegrationType) -> str:
    return value


def deserialize_cbor(data: str) -> IntegrationType:
    return cast(IntegrationType, data)
