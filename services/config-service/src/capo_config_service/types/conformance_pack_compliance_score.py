"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceScore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_score
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.last_updated_time


class ConformancePackComplianceScore(TypedDict, closed=True):
    score: NotRequired["capo_config_service.types.compliance_score.ComplianceScore"]
    """<p>Compliance score for the conformance pack. Conformance packs with no evaluation results will have a compliance score of <code>INSUFFICIENT_DATA</code>.</p>"""
    conformance_pack_name: NotRequired[
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    ]
    """<p>The name of the conformance pack.</p>"""
    last_updated_time: NotRequired[
        "capo_config_service.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>The time that the conformance pack compliance score was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceScore) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "conformance_pack_name" in value:
        out["ConformancePackName"] = value["conformance_pack_name"]
    if "last_updated_time" in value:
        import capo_config_service.types.last_updated_time

        out["LastUpdatedTime"] = (
            capo_config_service.types.last_updated_time.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackComplianceScore:
    out: ConformancePackComplianceScore = {}  # type: ignore[typeddict-item]
    if data.get("Score") is not None:
        out["score"] = data["Score"]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    if data.get("LastUpdatedTime") is not None:
        import capo_config_service.types.last_updated_time

        out["last_updated_time"] = (
            capo_config_service.types.last_updated_time.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    return out
