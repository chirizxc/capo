"""Generated from Smithy shape ``com.amazonaws.securityagent#PrivateConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.private_connection_summary

PrivateConnectionList: TypeAlias = list[
    "capo_securityagent.types.private_connection_summary.PrivateConnectionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionList) -> list:
    import capo_securityagent.types.private_connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.private_connection_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PrivateConnectionList:
    import capo_securityagent.types.private_connection_summary

    out: PrivateConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.private_connection_summary.deserialize_json(item)
        )
    return out
