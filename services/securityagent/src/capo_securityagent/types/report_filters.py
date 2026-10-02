"""Generated from Smithy shape ``com.amazonaws.securityagent#ReportFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.confidence_level_filter_list
    import capo_securityagent.types.finding_status_filter_list
    import capo_securityagent.types.report_filter_list
    import capo_securityagent.types.risk_level_filter_list
    import capo_securityagent.types.risk_type_filter_list
    import capo_securityagent.types.task_execution_status_filter_list


class ReportFilters(TypedDict, closed=True):
    risk_levels: NotRequired[
        "capo_securityagent.types.risk_level_filter_list.RiskLevelFilterList"
    ]
    """<p>The severity levels to include in the report.</p>"""
    confidence_levels: NotRequired[
        "capo_securityagent.types.confidence_level_filter_list.ConfidenceLevelFilterList"
    ]
    """<p>The confidence levels to include in the report.</p>"""
    statuses: NotRequired[
        "capo_securityagent.types.finding_status_filter_list.FindingStatusFilterList"
    ]
    """<p>The finding statuses to include in the report.</p>"""
    risk_types: NotRequired[
        "capo_securityagent.types.risk_type_filter_list.RiskTypeFilterList"
    ]
    """<p>The risk types to include in the report.</p>"""
    finding_types: NotRequired[
        "capo_securityagent.types.report_filter_list.ReportFilterList"
    ]
    """<p>The finding types to include in the report.</p>"""
    task_statuses: NotRequired[
        "capo_securityagent.types.task_execution_status_filter_list.TaskExecutionStatusFilterList"
    ]
    """<p>The task execution statuses to include in the report's task table.</p>"""
    annotation_notes: NotRequired["bool"]
    """<p>Whether to include reviewer annotation notes under each finding.</p>"""
    compliance_report: NotRequired["bool"]
    """<p>Whether to include the compliance-ready report additions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportFilters) -> dict:
    out: dict = {}
    if "risk_levels" in value:
        import capo_securityagent.types.risk_level_filter_list

        out["riskLevels"] = (
            capo_securityagent.types.risk_level_filter_list.serialize_json(
                value["risk_levels"]
            )
        )
    if "confidence_levels" in value:
        import capo_securityagent.types.confidence_level_filter_list

        out["confidenceLevels"] = (
            capo_securityagent.types.confidence_level_filter_list.serialize_json(
                value["confidence_levels"]
            )
        )
    if "statuses" in value:
        import capo_securityagent.types.finding_status_filter_list

        out["statuses"] = (
            capo_securityagent.types.finding_status_filter_list.serialize_json(
                value["statuses"]
            )
        )
    if "risk_types" in value:
        import capo_securityagent.types.risk_type_filter_list

        out["riskTypes"] = (
            capo_securityagent.types.risk_type_filter_list.serialize_json(
                value["risk_types"]
            )
        )
    if "finding_types" in value:
        import capo_securityagent.types.report_filter_list

        out["findingTypes"] = (
            capo_securityagent.types.report_filter_list.serialize_json(
                value["finding_types"]
            )
        )
    if "task_statuses" in value:
        import capo_securityagent.types.task_execution_status_filter_list

        out["taskStatuses"] = (
            capo_securityagent.types.task_execution_status_filter_list.serialize_json(
                value["task_statuses"]
            )
        )
    if "annotation_notes" in value:
        out["annotationNotes"] = value["annotation_notes"]
    if "compliance_report" in value:
        out["complianceReport"] = value["compliance_report"]
    return out


def deserialize_json(data: dict) -> ReportFilters:
    out: ReportFilters = {}  # type: ignore[typeddict-item]
    if data.get("riskLevels") is not None:
        import capo_securityagent.types.risk_level_filter_list

        out["risk_levels"] = (
            capo_securityagent.types.risk_level_filter_list.deserialize_json(
                data["riskLevels"]
            )
        )
    if data.get("confidenceLevels") is not None:
        import capo_securityagent.types.confidence_level_filter_list

        out["confidence_levels"] = (
            capo_securityagent.types.confidence_level_filter_list.deserialize_json(
                data["confidenceLevels"]
            )
        )
    if data.get("statuses") is not None:
        import capo_securityagent.types.finding_status_filter_list

        out["statuses"] = (
            capo_securityagent.types.finding_status_filter_list.deserialize_json(
                data["statuses"]
            )
        )
    if data.get("riskTypes") is not None:
        import capo_securityagent.types.risk_type_filter_list

        out["risk_types"] = (
            capo_securityagent.types.risk_type_filter_list.deserialize_json(
                data["riskTypes"]
            )
        )
    if data.get("findingTypes") is not None:
        import capo_securityagent.types.report_filter_list

        out["finding_types"] = (
            capo_securityagent.types.report_filter_list.deserialize_json(
                data["findingTypes"]
            )
        )
    if data.get("taskStatuses") is not None:
        import capo_securityagent.types.task_execution_status_filter_list

        out["task_statuses"] = (
            capo_securityagent.types.task_execution_status_filter_list.deserialize_json(
                data["taskStatuses"]
            )
        )
    if data.get("annotationNotes") is not None:
        out["annotation_notes"] = data["annotationNotes"]
    if data.get("complianceReport") is not None:
        out["compliance_report"] = data["complianceReport"]
    return out
