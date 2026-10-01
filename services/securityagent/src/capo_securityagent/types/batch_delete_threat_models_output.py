"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchDeleteThreatModelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.delete_threat_model_failure_list
    import capo_securityagent.types.threat_model_id_list


class BatchDeleteThreatModelsOutput(TypedDict, closed=True):
    deleted: NotRequired[
        "capo_securityagent.types.threat_model_id_list.ThreatModelIdList"
    ]
    """<p>The list of threat model identifiers that were successfully deleted.</p>"""
    failed: NotRequired[
        "capo_securityagent.types.delete_threat_model_failure_list.DeleteThreatModelFailureList"
    ]
    """<p>The list of threat models that failed to delete, including the reason for each failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteThreatModelsOutput) -> dict:
    out: dict = {}
    if "deleted" in value:
        import capo_securityagent.types.threat_model_id_list

        out["deleted"] = capo_securityagent.types.threat_model_id_list.serialize_json(
            value["deleted"]
        )
    if "failed" in value:
        import capo_securityagent.types.delete_threat_model_failure_list

        out["failed"] = (
            capo_securityagent.types.delete_threat_model_failure_list.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteThreatModelsOutput:
    out: BatchDeleteThreatModelsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deleted") is not None:
        import capo_securityagent.types.threat_model_id_list

        out["deleted"] = capo_securityagent.types.threat_model_id_list.deserialize_json(
            data["deleted"]
        )
    if data.get("failed") is not None:
        import capo_securityagent.types.delete_threat_model_failure_list

        out["failed"] = (
            capo_securityagent.types.delete_threat_model_failure_list.deserialize_json(
                data["failed"]
            )
        )
    return out
