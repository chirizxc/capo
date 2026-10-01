"""Generated from Smithy shape ``com.amazonaws.devopsagent#ApprovalArgumentPins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.approval_pin_key
    import capo_devops_agent.types.approval_pin_value

ApprovalArgumentPins: TypeAlias = dict[
    "capo_devops_agent.types.approval_pin_key.ApprovalPinKey",
    "capo_devops_agent.types.approval_pin_value.ApprovalPinValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ApprovalArgumentPins) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ApprovalArgumentPins:
    out: ApprovalArgumentPins = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
