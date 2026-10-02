"""Generated from Smithy shape ``com.amazonaws.acm#CreateAcmeEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_arn


class CreateAcmeEndpointResponse(TypedDict, closed=True):
    acme_endpoint_arn: NotRequired["capo_acm.types.acme_endpoint_arn.AcmeEndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the created ACME endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAcmeEndpointResponse) -> dict:
    out: dict = {}
    if "acme_endpoint_arn" in value:
        out["AcmeEndpointArn"] = value["acme_endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAcmeEndpointResponse:
    out: CreateAcmeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpointArn") is not None:
        out["acme_endpoint_arn"] = data["AcmeEndpointArn"]
    return out
