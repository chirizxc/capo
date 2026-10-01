"""Generated from Smithy shape ``com.amazonaws.acm#DescribeAcmeEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint


class DescribeAcmeEndpointResponse(TypedDict, closed=True):
    acme_endpoint: NotRequired["capo_acm.types.acme_endpoint.AcmeEndpoint"]
    """<p>The ACME endpoint details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAcmeEndpointResponse) -> dict:
    out: dict = {}
    if "acme_endpoint" in value:
        import capo_acm.types.acme_endpoint

        out["AcmeEndpoint"] = capo_acm.types.acme_endpoint.serialize_aws_json_1_1(
            value["acme_endpoint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAcmeEndpointResponse:
    out: DescribeAcmeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpoint") is not None:
        import capo_acm.types.acme_endpoint

        out["acme_endpoint"] = capo_acm.types.acme_endpoint.deserialize_aws_json_1_1(
            data["AcmeEndpoint"]
        )
    return out
