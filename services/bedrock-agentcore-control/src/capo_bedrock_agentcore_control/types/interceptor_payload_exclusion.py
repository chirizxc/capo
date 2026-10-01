"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorPayloadExclusion``."""

from typing import Literal, TypeAlias, cast

InterceptorPayloadExclusion: TypeAlias = Literal["RESPONSE_BODY",]


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorPayloadExclusion) -> str:
    return value


def deserialize_json(data: str) -> InterceptorPayloadExclusion:
    return cast(InterceptorPayloadExclusion, data)
