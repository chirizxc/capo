"""Generated from Smithy shape ``com.amazonaws.devopsagent#TriggerEvent``."""

from typing import Literal, TypeAlias, cast

"""<p>Webhook events that can auto-trigger a capability. PULL_REQUEST_* events apply to RELEASE_READINESS_REVIEW; WORKFLOW_* events apply to RELEASE_SHEPHERDING.</p>"""
TriggerEvent: TypeAlias = Literal[
    "PULL_REQUEST_READY_FOR_REVIEW",
    "PULL_REQUEST_DRAFT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerEvent) -> str:
    return value


def deserialize_json(data: str) -> TriggerEvent:
    return cast(TriggerEvent, data)
