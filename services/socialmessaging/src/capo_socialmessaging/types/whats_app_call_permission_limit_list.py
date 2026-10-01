"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallPermissionLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_permission_limit

WhatsAppCallPermissionLimitList: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_call_permission_limit.WhatsAppCallPermissionLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallPermissionLimitList) -> list:
    import capo_socialmessaging.types.whats_app_call_permission_limit

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_call_permission_limit.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppCallPermissionLimitList:
    import capo_socialmessaging.types.whats_app_call_permission_limit

    out: WhatsAppCallPermissionLimitList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_socialmessaging.types.whats_app_call_permission_limit.deserialize_json(
                item
            )
        )
    return out
