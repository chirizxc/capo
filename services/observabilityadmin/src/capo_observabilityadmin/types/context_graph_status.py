"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ContextGraphStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of context graph centralization for a centralization rule. This status is independent of the overall <code>RuleHealth</code> for log delivery. Returns <code>Provisioning</code> while the context graph is being set up, <code>Healthy</code> once it is active, or <code>Unhealthy</code> if provisioning failed.</p>"""
ContextGraphStatus: TypeAlias = Literal[
    "Healthy",
    "Unhealthy",
    "Provisioning",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextGraphStatus) -> str:
    return value


def deserialize_json(data: str) -> ContextGraphStatus:
    return cast(ContextGraphStatus, data)
