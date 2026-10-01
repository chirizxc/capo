"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetTestRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.test_run_id


class GetTestRunRequest(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the test run to retrieve.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test run belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTestRunRequest:
    out: GetTestRunRequest = {}  # type: ignore[typeddict-item]
    return out
