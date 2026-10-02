"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetTestTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service_owned_arn


class GetTestTemplateRequest(TypedDict, closed=True):
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTestTemplateRequest:
    out: GetTestTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
