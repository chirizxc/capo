"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionCustomErrorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.integer
    import capo_lightsail.types.long
    import capo_lightsail.types.string


class DistributionCustomErrorResponse(TypedDict, closed=True):
    error_code: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The HTTP error code from the origin that triggers the custom error response (for example, <code>403</code> or <code>404</code>).</p>"""
    response_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The HTTP status code that the distribution returns to the viewer for the custom error response.</p>"""
    response_page_path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path to the custom error page that the distribution returns to the viewer (for example, <code>/404.html</code>). The path must begin with a forward slash (<code>/</code>) and reference an object that is available from the origin.</p>"""
    error_caching_min_ttl: NotRequired["capo_lightsail.types.long.long"]
    """<p>The minimum time, in seconds, that the distribution caches the custom error response before requesting the object again from the origin. If you don't specify a value, the default is <code>10</code> seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionCustomErrorResponse) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "response_code" in value:
        out["responseCode"] = value["response_code"]
    if "response_page_path" in value:
        out["responsePagePath"] = value["response_page_path"]
    if "error_caching_min_ttl" in value:
        out["errorCachingMinTTL"] = value["error_caching_min_ttl"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributionCustomErrorResponse:
    out: DistributionCustomErrorResponse = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("responseCode") is not None:
        out["response_code"] = data["responseCode"]
    if data.get("responsePagePath") is not None:
        out["response_page_path"] = data["responsePagePath"]
    if data.get("errorCachingMinTTL") is not None:
        out["error_caching_min_ttl"] = data["errorCachingMinTTL"]
    return out
