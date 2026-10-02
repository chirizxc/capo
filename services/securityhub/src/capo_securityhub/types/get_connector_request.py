"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class GetConnectorRequest(TypedDict, closed=True):
    connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the connector to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectorRequest:
    out: GetConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
