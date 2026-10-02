"""Generated from Smithy shape ``com.amazonaws.devicefarm#JobReportMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.double
    import capo_device_farm.types.integer


class JobReportMetrics(TypedDict, closed=True):
    jobs_total: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The total number of jobs in the run.</p>"""
    jobs_passed: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of jobs that passed.</p>"""
    jobs_failed: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of jobs that failed.</p>"""
    jobs_skipped: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of jobs that were skipped.</p>"""
    jobs_errored: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of jobs that errored.</p>"""
    jobs_stopped: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of jobs that were stopped.</p>"""
    jobs_passed_percentage: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The percentage of jobs that passed.</p>"""
    total_job_execution_duration_seconds: NotRequired[
        "capo_device_farm.types.double.Double"
    ]
    """<p>The total execution duration of all jobs in the run, in seconds.</p>"""
    average_job_execution_duration_seconds: NotRequired[
        "capo_device_farm.types.double.Double"
    ]
    """<p>The average execution duration of jobs in the run, in seconds.</p>"""
    median_job_execution_duration_seconds: NotRequired[
        "capo_device_farm.types.double.Double"
    ]
    """<p>The median execution duration of jobs in the run, in seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobReportMetrics) -> dict:
    out: dict = {}
    if "jobs_total" in value:
        out["jobsTotal"] = value["jobs_total"]
    if "jobs_passed" in value:
        out["jobsPassed"] = value["jobs_passed"]
    if "jobs_failed" in value:
        out["jobsFailed"] = value["jobs_failed"]
    if "jobs_skipped" in value:
        out["jobsSkipped"] = value["jobs_skipped"]
    if "jobs_errored" in value:
        out["jobsErrored"] = value["jobs_errored"]
    if "jobs_stopped" in value:
        out["jobsStopped"] = value["jobs_stopped"]
    if "jobs_passed_percentage" in value:
        out["jobsPassedPercentage"] = (
            "NaN"
            if value["jobs_passed_percentage"] != value["jobs_passed_percentage"]
            else "Infinity"
            if value["jobs_passed_percentage"] == float("inf")
            else "-Infinity"
            if value["jobs_passed_percentage"] == float("-inf")
            else value["jobs_passed_percentage"]
        )
    if "total_job_execution_duration_seconds" in value:
        out["totalJobExecutionDurationSeconds"] = (
            "NaN"
            if value["total_job_execution_duration_seconds"]
            != value["total_job_execution_duration_seconds"]
            else "Infinity"
            if value["total_job_execution_duration_seconds"] == float("inf")
            else "-Infinity"
            if value["total_job_execution_duration_seconds"] == float("-inf")
            else value["total_job_execution_duration_seconds"]
        )
    if "average_job_execution_duration_seconds" in value:
        out["averageJobExecutionDurationSeconds"] = (
            "NaN"
            if value["average_job_execution_duration_seconds"]
            != value["average_job_execution_duration_seconds"]
            else "Infinity"
            if value["average_job_execution_duration_seconds"] == float("inf")
            else "-Infinity"
            if value["average_job_execution_duration_seconds"] == float("-inf")
            else value["average_job_execution_duration_seconds"]
        )
    if "median_job_execution_duration_seconds" in value:
        out["medianJobExecutionDurationSeconds"] = (
            "NaN"
            if value["median_job_execution_duration_seconds"]
            != value["median_job_execution_duration_seconds"]
            else "Infinity"
            if value["median_job_execution_duration_seconds"] == float("inf")
            else "-Infinity"
            if value["median_job_execution_duration_seconds"] == float("-inf")
            else value["median_job_execution_duration_seconds"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobReportMetrics:
    out: JobReportMetrics = {}  # type: ignore[typeddict-item]
    if data.get("jobsTotal") is not None:
        out["jobs_total"] = data["jobsTotal"]
    if data.get("jobsPassed") is not None:
        out["jobs_passed"] = data["jobsPassed"]
    if data.get("jobsFailed") is not None:
        out["jobs_failed"] = data["jobsFailed"]
    if data.get("jobsSkipped") is not None:
        out["jobs_skipped"] = data["jobsSkipped"]
    if data.get("jobsErrored") is not None:
        out["jobs_errored"] = data["jobsErrored"]
    if data.get("jobsStopped") is not None:
        out["jobs_stopped"] = data["jobsStopped"]
    if data.get("jobsPassedPercentage") is not None:
        out["jobs_passed_percentage"] = float(data["jobsPassedPercentage"])
    if data.get("totalJobExecutionDurationSeconds") is not None:
        out["total_job_execution_duration_seconds"] = float(
            data["totalJobExecutionDurationSeconds"]
        )
    if data.get("averageJobExecutionDurationSeconds") is not None:
        out["average_job_execution_duration_seconds"] = float(
            data["averageJobExecutionDurationSeconds"]
        )
    if data.get("medianJobExecutionDurationSeconds") is not None:
        out["median_job_execution_duration_seconds"] = float(
            data["medianJobExecutionDurationSeconds"]
        )
    return out
