"""Generated from Smithy shape ``com.amazonaws.acm#ListAcmeEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.acme_endpoint_list


class ListAcmeEndpointsResponse(TypedDict, closed=True):
    acme_endpoints: NotRequired["capo_acm.types.acme_endpoint_list.AcmeEndpointList"]
    """<p>The list of ACME endpoints.</p>"""
    next_token: NotRequired["str"]
    """<p>A token for pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcmeEndpointsResponse) -> dict:
    out: dict = {}
    if "acme_endpoints" in value:
        import capo_acm.types.acme_endpoint_list

        out["AcmeEndpoints"] = capo_acm.types.acme_endpoint_list.serialize_aws_json_1_1(
            value["acme_endpoints"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcmeEndpointsResponse:
    out: ListAcmeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("AcmeEndpoints") is not None:
        import capo_acm.types.acme_endpoint_list

        out["acme_endpoints"] = (
            capo_acm.types.acme_endpoint_list.deserialize_aws_json_1_1(
                data["AcmeEndpoints"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
