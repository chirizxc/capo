"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.test_id


class TestSummary(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The unique identifier of the test.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template the test was created from.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    total_test_runs: "int"
    """<p>The total number of runs of the test.</p>"""
    successful_test_runs: "int"
    """<p>The number of successful runs of the test.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp when the test was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSummary) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["testTemplateArn"] = value["test_template_arn"]
    out["serviceArn"] = value["service_arn"]
    out["totalTestRuns"] = value["total_test_runs"]
    out["successfulTestRuns"] = value["successful_test_runs"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["creationTime"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> TestSummary:
    out: TestSummary = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        raise DeserializationError("TestSummary.test_id required")
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        raise DeserializationError("TestSummary.test_template_arn required")
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("TestSummary.service_arn required")
    if data.get("totalTestRuns") is not None:
        out["total_test_runs"] = data["totalTestRuns"]
    else:
        raise DeserializationError("TestSummary.total_test_runs required")
    if data.get("successfulTestRuns") is not None:
        out["successful_test_runs"] = data["successfulTestRuns"]
    else:
        raise DeserializationError("TestSummary.successful_test_runs required")
    if data.get("creationTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["creation_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("TestSummary.creation_time required")
    return out
