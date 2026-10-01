"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFixtureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.fixture_id


class GetFixtureRequest(TypedDict, closed=True):
    fixture_id: "capo_elementalinference.types.fixture_id.FixtureId"
    """<p>The ID of the fixture to retrieve, as returned by SearchFixtures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFixtureRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFixtureRequest:
    out: GetFixtureRequest = {}  # type: ignore[typeddict-item]
    return out
