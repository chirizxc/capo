"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.arn
    import capo_marketplace_catalog.types.assessment_result
    import capo_marketplace_catalog.types.assessment_target_summary
    import capo_marketplace_catalog.types.control_assessment_list
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.framework_summary
    import capo_marketplace_catalog.types.next_token
    import capo_marketplace_catalog.types.resource_id
    import capo_marketplace_catalog.types.versioned_framework_id


class DescribeAssessmentResponse(TypedDict, closed=True):
    assessment_arn: NotRequired["capo_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the assessment.</p>"""
    assessment_id: NotRequired["capo_marketplace_catalog.types.resource_id.ResourceId"]
    """<p>The unique ID of the assessment.</p>"""
    framework_id: NotRequired[
        "capo_marketplace_catalog.types.versioned_framework_id.VersionedFrameworkId"
    ]
    """<p>The identifier of the framework that was evaluated by this assessment, in the format <code>frameworkId@version</code> (for example, <code>AMISecurity@1.0</code>).</p>"""
    assessment_target_summary: NotRequired[
        "capo_marketplace_catalog.types.assessment_target_summary.AssessmentTargetSummary"
    ]
    """<p>Identifies the entity or change set that was assessed.</p>"""
    framework_summary: NotRequired[
        "capo_marketplace_catalog.types.framework_summary.FrameworkSummary"
    ]
    """<p>The framework-specific details of the assessed resource. The set member corresponds to the framework identified by <code>FrameworkId</code>.</p>"""
    assessment_result: NotRequired[
        "capo_marketplace_catalog.types.assessment_result.AssessmentResult"
    ]
    """<p>The overall result of the assessment.</p>"""
    created_at: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The date and time the assessment was created, in ISO 8601 format (<code>2018-02-27T13:45:22Z</code>).</p>"""
    expires_at: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The date and time the assessment expires, in ISO 8601 format (<code>2018-02-27T13:45:22Z</code>).</p>"""
    control_assessments: NotRequired[
        "capo_marketplace_catalog.types.control_assessment_list.ControlAssessmentList"
    ]
    """<p>An array of <code>ControlAssessment</code> objects, each containing the result of an individual control evaluated as part of the assessment.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment_arn" in value:
        out["AssessmentArn"] = value["assessment_arn"]
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    if "framework_id" in value:
        out["FrameworkId"] = value["framework_id"]
    if "assessment_target_summary" in value:
        import capo_marketplace_catalog.types.assessment_target_summary

        out["AssessmentTargetSummary"] = (
            capo_marketplace_catalog.types.assessment_target_summary.serialize_json(
                value["assessment_target_summary"]
            )
        )
    if "framework_summary" in value:
        import capo_marketplace_catalog.types.framework_summary

        out["FrameworkSummary"] = (
            capo_marketplace_catalog.types.framework_summary.serialize_json(
                value["framework_summary"]
            )
        )
    if "assessment_result" in value:
        import capo_marketplace_catalog.types.assessment_result

        out["AssessmentResult"] = (
            capo_marketplace_catalog.types.assessment_result.serialize_json(
                value["assessment_result"]
            )
        )
    if "created_at" in value:
        out["CreatedAt"] = value["created_at"]
    if "expires_at" in value:
        out["ExpiresAt"] = value["expires_at"]
    if "control_assessments" in value:
        import capo_marketplace_catalog.types.control_assessment_list

        out["ControlAssessments"] = (
            capo_marketplace_catalog.types.control_assessment_list.serialize_json(
                value["control_assessments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAssessmentResponse:
    out: DescribeAssessmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("AssessmentArn") is not None:
        out["assessment_arn"] = data["AssessmentArn"]
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    if data.get("FrameworkId") is not None:
        out["framework_id"] = data["FrameworkId"]
    if data.get("AssessmentTargetSummary") is not None:
        import capo_marketplace_catalog.types.assessment_target_summary

        out["assessment_target_summary"] = (
            capo_marketplace_catalog.types.assessment_target_summary.deserialize_json(
                data["AssessmentTargetSummary"]
            )
        )
    if data.get("FrameworkSummary") is not None:
        import capo_marketplace_catalog.types.framework_summary

        out["framework_summary"] = (
            capo_marketplace_catalog.types.framework_summary.deserialize_json(
                data["FrameworkSummary"]
            )
        )
    if data.get("AssessmentResult") is not None:
        import capo_marketplace_catalog.types.assessment_result

        out["assessment_result"] = (
            capo_marketplace_catalog.types.assessment_result.deserialize_json(
                data["AssessmentResult"]
            )
        )
    if data.get("CreatedAt") is not None:
        out["created_at"] = data["CreatedAt"]
    if data.get("ExpiresAt") is not None:
        out["expires_at"] = data["ExpiresAt"]
    if data.get("ControlAssessments") is not None:
        import capo_marketplace_catalog.types.control_assessment_list

        out["control_assessments"] = (
            capo_marketplace_catalog.types.control_assessment_list.deserialize_json(
                data["ControlAssessments"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
