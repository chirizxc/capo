"""Generated from Smithy shape ``com.amazonaws.healthlake#ListDataTransformationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_job_name
    import capo_healthlake.types.data_transformation_next_token
    import capo_healthlake.types.date_time
    import capo_healthlake.types.max_results
    import capo_healthlake.types.transformation_job_status


class ListDataTransformationJobsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_healthlake.types.max_results.MaxResults"]
    """<p>The maximum number of jobs to return per page. If you don't specify a value, the service returns up to 100 results.</p>"""
    next_token: NotRequired[
        "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
    ]
    """<p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>"""
    job_status: NotRequired[
        "capo_healthlake.types.transformation_job_status.TransformationJobStatus"
    ]
    """<p>Filters the results to include only jobs with the specified status.</p>"""
    job_name: NotRequired[
        "capo_healthlake.types.data_transformation_job_name.DataTransformationJobName"
    ]
    """<p>Filters the results to include only jobs with the specified name.</p>"""
    submitted_after: NotRequired["capo_healthlake.types.date_time.DateTime"]
    """<p>Filters the results to include only jobs submitted at or after this timestamp.</p>"""
    submitted_before: NotRequired["capo_healthlake.types.date_time.DateTime"]
    """<p>Filters the results to include only jobs submitted at or before this timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataTransformationJobsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "job_status" in value:
        import capo_healthlake.types.transformation_job_status

        out["JobStatus"] = (
            capo_healthlake.types.transformation_job_status.serialize_aws_json_1_0(
                value["job_status"]
            )
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "submitted_after" in value:
        import capo_healthlake.types.date_time

        out["SubmittedAfter"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
            value["submitted_after"]
        )
    if "submitted_before" in value:
        import capo_healthlake.types.date_time

        out["SubmittedBefore"] = capo_healthlake.types.date_time.serialize_aws_json_1_0(
            value["submitted_before"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDataTransformationJobsRequest:
    out: ListDataTransformationJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("JobStatus") is not None:
        import capo_healthlake.types.transformation_job_status

        out["job_status"] = (
            capo_healthlake.types.transformation_job_status.deserialize_aws_json_1_0(
                data["JobStatus"]
            )
        )
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("SubmittedAfter") is not None:
        import capo_healthlake.types.date_time

        out["submitted_after"] = (
            capo_healthlake.types.date_time.deserialize_aws_json_1_0(
                data["SubmittedAfter"]
            )
        )
    if data.get("SubmittedBefore") is not None:
        import capo_healthlake.types.date_time

        out["submitted_before"] = (
            capo_healthlake.types.date_time.deserialize_aws_json_1_0(
                data["SubmittedBefore"]
            )
        )
    return out
