"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetStreamForSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class GetStreamForSegmentsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamForSegmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStreamForSegmentsRequest:
    out: GetStreamForSegmentsRequest = {}  # type: ignore[typeddict-item]
    return out
