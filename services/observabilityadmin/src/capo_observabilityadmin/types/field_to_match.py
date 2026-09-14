"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#FieldToMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.single_header


class FieldToMatch(TypedDict, closed=True):
    single_header: NotRequired[
        "capo_observabilityadmin.types.single_header.SingleHeader"
    ]
    """<p> Redacts a specific header field by name from WAF logs. </p>"""
    uri_path: NotRequired["str"]
    """<p> Redacts the URI path from WAF logs. </p>"""
    query_string: NotRequired["str"]
    """<p> Redacts the entire query string from WAF logs. </p>"""
    method: NotRequired["str"]
    """<p> Redacts the HTTP method from WAF logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldToMatch) -> dict:
    out: dict = {}
    if "single_header" in value:
        import capo_observabilityadmin.types.single_header

        out["SingleHeader"] = (
            capo_observabilityadmin.types.single_header.serialize_json(
                value["single_header"]
            )
        )
    if "uri_path" in value:
        out["UriPath"] = value["uri_path"]
    if "query_string" in value:
        out["QueryString"] = value["query_string"]
    if "method" in value:
        out["Method"] = value["method"]
    return out


def deserialize_json(data: dict) -> FieldToMatch:
    out: FieldToMatch = {}  # type: ignore[typeddict-item]
    if data.get("SingleHeader") is not None:
        import capo_observabilityadmin.types.single_header

        out["single_header"] = (
            capo_observabilityadmin.types.single_header.deserialize_json(
                data["SingleHeader"]
            )
        )
    if data.get("UriPath") is not None:
        out["uri_path"] = data["UriPath"]
    if data.get("QueryString") is not None:
        out["query_string"] = data["QueryString"]
    if data.get("Method") is not None:
        out["method"] = data["Method"]
    return out
