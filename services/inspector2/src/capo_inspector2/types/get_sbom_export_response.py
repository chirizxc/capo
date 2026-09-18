"""Generated from Smithy shape ``com.amazonaws.inspector2#GetSbomExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.destination
    import capo_inspector2.types.external_report_status
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.report_id
    import capo_inspector2.types.reporting_error_code
    import capo_inspector2.types.resource_filter_criteria
    import capo_inspector2.types.sbom_report_format


class GetSbomExportResponse(TypedDict, closed=True):
    report_id: NotRequired["capo_inspector2.types.report_id.ReportId"]
    """<p>The report ID of the software bill of materials (SBOM) report.</p>"""
    format: NotRequired["capo_inspector2.types.sbom_report_format.SbomReportFormat"]
    """<p>The format of the software bill of materials (SBOM) report.</p>"""
    status: NotRequired[
        "capo_inspector2.types.external_report_status.ExternalReportStatus"
    ]
    """<p>The status of the software bill of materials (SBOM) report.</p>"""
    error_code: NotRequired[
        "capo_inspector2.types.reporting_error_code.ReportingErrorCode"
    ]
    """<p>An error code.</p>"""
    error_message: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>An error message.</p>"""
    s3_destination: NotRequired["capo_inspector2.types.destination.Destination"]
    """<p>Contains details of the Amazon S3 bucket and KMS key used to export findings</p>"""
    filter_criteria: NotRequired[
        "capo_inspector2.types.resource_filter_criteria.ResourceFilterCriteria"
    ]
    """<p>Contains details about the resource filter criteria used for the software bill of materials (SBOM) report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSbomExportResponse) -> dict:
    out: dict = {}
    if "report_id" in value:
        out["reportId"] = value["report_id"]
    if "format" in value:
        out["format"] = value["format"]
    if "status" in value:
        out["status"] = value["status"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "s3_destination" in value:
        import capo_inspector2.types.destination

        out["s3Destination"] = capo_inspector2.types.destination.serialize_json(
            value["s3_destination"]
        )
    if "filter_criteria" in value:
        import capo_inspector2.types.resource_filter_criteria

        out["filterCriteria"] = (
            capo_inspector2.types.resource_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSbomExportResponse:
    out: GetSbomExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    if data.get("format") is not None:
        out["format"] = data["format"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("s3Destination") is not None:
        import capo_inspector2.types.destination

        out["s3_destination"] = capo_inspector2.types.destination.deserialize_json(
            data["s3Destination"]
        )
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.resource_filter_criteria

        out["filter_criteria"] = (
            capo_inspector2.types.resource_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    return out
