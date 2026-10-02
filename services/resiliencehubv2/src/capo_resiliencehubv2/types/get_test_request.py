"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.test_id


class GetTestRequest(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test to retrieve.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTestRequest:
    out: GetTestRequest = {}  # type: ignore[typeddict-item]
    return out
