"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListEnrichmentJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.job_type
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.workspace_name


class ListEnrichmentJobsRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the IoT SiteWise workspace to list enrichment jobs from.</p>"""
    dataset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>Filter jobs by dataset ID. Returns only jobs analyzing data from the specified dataset.</p>"""
    property_alias: NotRequired[
        "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
    ]
    """<p>Filter by property alias (human-readable sensor name). Specify either propertyAlias or timeSeriesId, but not both. Returns only jobs analyzing the specified property alias.</p>"""
    time_series_id: NotRequired["capo_iotsitewise.types.time_series_id.TimeSeriesId"]
    """<p>Filter by time series ID (system identifier). Specify either timeSeriesId or propertyAlias, but not both. Returns only jobs analyzing the specified time series.</p>"""
    status: NotRequired[
        "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
    ]
    """<p>Filter by job status. Returns only jobs in the specified status. Use RUNNING to find active jobs, or FAILED to identify jobs requiring attention.</p>"""
    job_type: NotRequired["capo_iotsitewise.types.job_type.JobType"]
    """<p>Filter by enrichment job type. Currently only EVENT_DETECTION is supported. Use this filter to future-proof queries when additional job types are added.</p>"""
    start_date: NotRequired["datetime.datetime"]
    """<p>The exclusive start of the date range for filtering jobs by creation time. Jobs created after this timestamp are included. Use ISO 8601 format (e.g., 2024-01-01T00:00:00Z).</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The inclusive end of the date range for filtering jobs by creation time. Jobs created on or before this timestamp are included. Use ISO 8601 format (e.g., 2024-01-31T23:59:59Z).</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>Maximum number of jobs to return per page. Defaults to 50 if not specified. Use smaller values for faster responses, larger values to reduce API calls.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>Pagination token from a previous ListEnrichmentJobs response. Include this token to retrieve the next page of results. Omit for the first request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnrichmentJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnrichmentJobsRequest:
    out: ListEnrichmentJobsRequest = {}  # type: ignore[typeddict-item]
    return out
