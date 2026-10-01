"""Generated from Smithy shape ``com.amazonaws.outposts#GetPrivateConnectivityConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.outpost_id


class GetPrivateConnectivityConfigInput(TypedDict, closed=True):
    outpost_id: "capo_outposts.types.outpost_id.OutpostId"
    """<p>The ID or ARN of the Outpost.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrivateConnectivityConfigInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPrivateConnectivityConfigInput:
    out: GetPrivateConnectivityConfigInput = {}  # type: ignore[typeddict-item]
    return out
