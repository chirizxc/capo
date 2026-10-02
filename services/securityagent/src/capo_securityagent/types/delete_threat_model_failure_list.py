"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteThreatModelFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.delete_threat_model_failure

DeleteThreatModelFailureList: TypeAlias = list[
    "capo_securityagent.types.delete_threat_model_failure.DeleteThreatModelFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThreatModelFailureList) -> list:
    import capo_securityagent.types.delete_threat_model_failure

    out: list = []
    for item in value:
        out.append(
            capo_securityagent.types.delete_threat_model_failure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteThreatModelFailureList:
    import capo_securityagent.types.delete_threat_model_failure

    out: DeleteThreatModelFailureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_securityagent.types.delete_threat_model_failure.deserialize_json(item)
        )
    return out
