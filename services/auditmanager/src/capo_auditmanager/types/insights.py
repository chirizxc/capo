"""Generated from Smithy shape ``com.amazonaws.auditmanager#Insights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.nullable_integer
    import capo_auditmanager.types.timestamp


class Insights(TypedDict, closed=True):
    active_assessments_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of active assessments in Audit Manager. </p>"""
    noncompliant_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of compliance check evidence that Audit Manager classified as non-compliant on the <code>lastUpdated</code> date. This includes evidence that was collected from Security Hub CSPM with a <i>Fail</i> ruling, or collected from Config with a <i>Non-compliant</i> ruling. </p>"""
    compliant_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of compliance check evidence that Audit Manager classified as compliant on the <code>lastUpdated</code> date. This includes evidence that was collected from Security Hub CSPM with a <i>Pass</i> ruling, or collected from Config with a <i>Compliant</i> ruling. </p>"""
    inconclusive_evidence_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of evidence without a compliance check ruling. Evidence is inconclusive when the associated control uses Security Hub CSPM or Config as a data source but you didn't enable those services. This is also the case when a control uses a data source that doesn’t support compliance checks (for example: manual evidence, API calls, or CloudTrail). </p> <note> <p>If evidence has a compliance check status of <i>not applicable</i>, it's classed as <i>inconclusive</i> in <code>Insights</code> data.</p> </note>"""
    assessment_controls_count_by_noncompliant_evidence: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of assessment controls that collected non-compliant evidence on the <code>lastUpdated</code> date. </p>"""
    total_assessment_controls_count: NotRequired[
        "capo_auditmanager.types.nullable_integer.NullableInteger"
    ]
    """<p>The total number of controls across all active assessments. </p>"""
    last_updated: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p>The time when the cross-assessment insights were last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Insights) -> dict:
    out: dict = {}
    if "active_assessments_count" in value:
        out["activeAssessmentsCount"] = value["active_assessments_count"]
    if "noncompliant_evidence_count" in value:
        out["noncompliantEvidenceCount"] = value["noncompliant_evidence_count"]
    if "compliant_evidence_count" in value:
        out["compliantEvidenceCount"] = value["compliant_evidence_count"]
    if "inconclusive_evidence_count" in value:
        out["inconclusiveEvidenceCount"] = value["inconclusive_evidence_count"]
    if "assessment_controls_count_by_noncompliant_evidence" in value:
        out["assessmentControlsCountByNoncompliantEvidence"] = value[
            "assessment_controls_count_by_noncompliant_evidence"
        ]
    if "total_assessment_controls_count" in value:
        out["totalAssessmentControlsCount"] = value["total_assessment_controls_count"]
    if "last_updated" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdated"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> Insights:
    out: Insights = {}  # type: ignore[typeddict-item]
    if data.get("activeAssessmentsCount") is not None:
        out["active_assessments_count"] = data["activeAssessmentsCount"]
    if data.get("noncompliantEvidenceCount") is not None:
        out["noncompliant_evidence_count"] = data["noncompliantEvidenceCount"]
    if data.get("compliantEvidenceCount") is not None:
        out["compliant_evidence_count"] = data["compliantEvidenceCount"]
    if data.get("inconclusiveEvidenceCount") is not None:
        out["inconclusive_evidence_count"] = data["inconclusiveEvidenceCount"]
    if data.get("assessmentControlsCountByNoncompliantEvidence") is not None:
        out["assessment_controls_count_by_noncompliant_evidence"] = data[
            "assessmentControlsCountByNoncompliantEvidence"
        ]
    if data.get("totalAssessmentControlsCount") is not None:
        out["total_assessment_controls_count"] = data["totalAssessmentControlsCount"]
    if data.get("lastUpdated") is not None:
        import capo_auditmanager.types.timestamp

        out["last_updated"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out
