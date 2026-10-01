"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListSharedDNSViewsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListSharedDNSViewsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to retrieve in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSharedDNSViewsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSharedDNSViewsInput:
    out: ListSharedDNSViewsInput = {}  # type: ignore[typeddict-item]
    return out
