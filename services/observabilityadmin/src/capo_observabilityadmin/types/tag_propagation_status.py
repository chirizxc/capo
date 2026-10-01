"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagPropagationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The health status of tag propagation for a centralization rule. This status is independent of the overall <code>RuleHealth</code> for log delivery.</p>"""
TagPropagationStatus: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationStatus) -> str:
    return value


def deserialize_json(data: str) -> TagPropagationStatus:
    return cast(TagPropagationStatus, data)
