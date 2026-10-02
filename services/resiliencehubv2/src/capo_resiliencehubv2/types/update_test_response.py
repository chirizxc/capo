"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test


class UpdateTestResponse(TypedDict, closed=True):
    test: "capo_resiliencehubv2.types.test.Test"
    """<p>The updated test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTestResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test

    out["test"] = capo_resiliencehubv2.types.test.serialize_json(value["test"])
    return out


def deserialize_json(data: dict) -> UpdateTestResponse:
    out: UpdateTestResponse = {}  # type: ignore[typeddict-item]
    if data.get("test") is not None:
        import capo_resiliencehubv2.types.test

        out["test"] = capo_resiliencehubv2.types.test.deserialize_json(data["test"])
    else:
        raise DeserializationError("UpdateTestResponse.test required")
    return out
