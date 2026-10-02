"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DisassociateStreamForSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class DisassociateStreamForSegmentsRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateStreamForSegmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateStreamForSegmentsRequest:
    out: DisassociateStreamForSegmentsRequest = {}  # type: ignore[typeddict-item]
    return out
