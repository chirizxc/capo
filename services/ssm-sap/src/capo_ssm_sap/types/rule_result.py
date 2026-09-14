"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.rule_result_id
    import capo_ssm_sap.types.rule_result_metadata
    import capo_ssm_sap.types.rule_result_status


class RuleResult(TypedDict, closed=True):
    id: NotRequired["capo_ssm_sap.types.rule_result_id.RuleResultId"]
    """<p>The unique identifier of the rule result.</p>"""
    description: NotRequired["str"]
    """<p>A description of what the rule validates.</p>"""
    status: NotRequired["capo_ssm_sap.types.rule_result_status.RuleResultStatus"]
    """<p>The status of the rule result.</p>"""
    message: NotRequired["str"]
    """<p>A message providing details about the rule result.</p>"""
    metadata: NotRequired["capo_ssm_sap.types.rule_result_metadata.RuleResultMetadata"]
    """<p>Additional metadata associated with the rule result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleResult) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_ssm_sap.types.rule_result_status

        out["Status"] = capo_ssm_sap.types.rule_result_status.serialize_json(
            value["status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "metadata" in value:
        import capo_ssm_sap.types.rule_result_metadata

        out["Metadata"] = capo_ssm_sap.types.rule_result_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> RuleResult:
    out: RuleResult = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_ssm_sap.types.rule_result_status

        out["status"] = capo_ssm_sap.types.rule_result_status.deserialize_json(
            data["Status"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Metadata") is not None:
        import capo_ssm_sap.types.rule_result_metadata

        out["metadata"] = capo_ssm_sap.types.rule_result_metadata.deserialize_json(
            data["Metadata"]
        )
    return out
