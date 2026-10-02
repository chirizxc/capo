"""Generated from Smithy shape ``com.amazonaws.securityagent#FindingStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.finding_status

FindingStatusFilterList: TypeAlias = list[
    "capo_securityagent.types.finding_status.FindingStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatusFilterList) -> list:
    import capo_securityagent.types.finding_status

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.finding_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingStatusFilterList:
    import capo_securityagent.types.finding_status

    out: FindingStatusFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.finding_status.deserialize_json(item))
    return out
