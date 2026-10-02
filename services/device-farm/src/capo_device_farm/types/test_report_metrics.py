"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestReportMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.double
    import capo_device_farm.types.integer


class TestReportMetrics(TypedDict, closed=True):
    tests_total: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The total number of tests in the job.</p>"""
    tests_passed: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of tests that passed.</p>"""
    tests_failed: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of tests that failed.</p>"""
    tests_skipped: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of tests that were skipped.</p>"""
    tests_errored: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of tests that errored.</p>"""
    tests_other: NotRequired["capo_device_farm.types.integer.Integer"]
    """<p>The number of tests with other result types.</p>"""
    tests_passed_percentage: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The percentage of tests that passed.</p>"""
    total_test_execution_duration_seconds: NotRequired[
        "capo_device_farm.types.double.Double"
    ]
    """<p>The total execution duration of all tests in the job, in seconds.</p>"""
    median_test_execution_duration_seconds: NotRequired[
        "capo_device_farm.types.double.Double"
    ]
    """<p>The median execution duration of tests in the job, in seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestReportMetrics) -> dict:
    out: dict = {}
    if "tests_total" in value:
        out["testsTotal"] = value["tests_total"]
    if "tests_passed" in value:
        out["testsPassed"] = value["tests_passed"]
    if "tests_failed" in value:
        out["testsFailed"] = value["tests_failed"]
    if "tests_skipped" in value:
        out["testsSkipped"] = value["tests_skipped"]
    if "tests_errored" in value:
        out["testsErrored"] = value["tests_errored"]
    if "tests_other" in value:
        out["testsOther"] = value["tests_other"]
    if "tests_passed_percentage" in value:
        out["testsPassedPercentage"] = (
            "NaN"
            if value["tests_passed_percentage"] != value["tests_passed_percentage"]
            else "Infinity"
            if value["tests_passed_percentage"] == float("inf")
            else "-Infinity"
            if value["tests_passed_percentage"] == float("-inf")
            else value["tests_passed_percentage"]
        )
    if "total_test_execution_duration_seconds" in value:
        out["totalTestExecutionDurationSeconds"] = (
            "NaN"
            if value["total_test_execution_duration_seconds"]
            != value["total_test_execution_duration_seconds"]
            else "Infinity"
            if value["total_test_execution_duration_seconds"] == float("inf")
            else "-Infinity"
            if value["total_test_execution_duration_seconds"] == float("-inf")
            else value["total_test_execution_duration_seconds"]
        )
    if "median_test_execution_duration_seconds" in value:
        out["medianTestExecutionDurationSeconds"] = (
            "NaN"
            if value["median_test_execution_duration_seconds"]
            != value["median_test_execution_duration_seconds"]
            else "Infinity"
            if value["median_test_execution_duration_seconds"] == float("inf")
            else "-Infinity"
            if value["median_test_execution_duration_seconds"] == float("-inf")
            else value["median_test_execution_duration_seconds"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TestReportMetrics:
    out: TestReportMetrics = {}  # type: ignore[typeddict-item]
    if data.get("testsTotal") is not None:
        out["tests_total"] = data["testsTotal"]
    if data.get("testsPassed") is not None:
        out["tests_passed"] = data["testsPassed"]
    if data.get("testsFailed") is not None:
        out["tests_failed"] = data["testsFailed"]
    if data.get("testsSkipped") is not None:
        out["tests_skipped"] = data["testsSkipped"]
    if data.get("testsErrored") is not None:
        out["tests_errored"] = data["testsErrored"]
    if data.get("testsOther") is not None:
        out["tests_other"] = data["testsOther"]
    if data.get("testsPassedPercentage") is not None:
        out["tests_passed_percentage"] = float(data["testsPassedPercentage"])
    if data.get("totalTestExecutionDurationSeconds") is not None:
        out["total_test_execution_duration_seconds"] = float(
            data["totalTestExecutionDurationSeconds"]
        )
    if data.get("medianTestExecutionDurationSeconds") is not None:
        out["median_test_execution_duration_seconds"] = float(
            data["medianTestExecutionDurationSeconds"]
        )
    return out
