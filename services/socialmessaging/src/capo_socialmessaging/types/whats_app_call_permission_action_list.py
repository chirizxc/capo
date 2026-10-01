"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallPermissionActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_permission_action

WhatsAppCallPermissionActionList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_call_permission_action.WhatsAppCallPermissionAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallPermissionActionList) -> list:
    import capo_socialmessaging.types.whats_app_call_permission_action

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_call_permission_action.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppCallPermissionActionList:
    import capo_socialmessaging.types.whats_app_call_permission_action

    out: WhatsAppCallPermissionActionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_socialmessaging.types.whats_app_call_permission_action.deserialize_json(
                item
            )
        )
    return out
