"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIntermediateTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier


class GetIntermediateTableInput(TypedDict, closed=True):
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table to retrieve.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntermediateTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIntermediateTableInput:
    out: GetIntermediateTableInput = {}  # type: ignore[typeddict-item]
    return out
