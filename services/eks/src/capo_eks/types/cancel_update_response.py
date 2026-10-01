"""Generated from Smithy shape ``com.amazonaws.eks#CancelUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.update


class CancelUpdateResponse(TypedDict, closed=True):
    update: NotRequired["capo_eks.types.update.Update"]
    """<p>The full description of the specified update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelUpdateResponse) -> dict:
    out: dict = {}
    if "update" in value:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.serialize_json(value["update"])
    return out


def deserialize_json(data: dict) -> CancelUpdateResponse:
    out: CancelUpdateResponse = {}  # type: ignore[typeddict-item]
    if data.get("update") is not None:
        import capo_eks.types.update

        out["update"] = capo_eks.types.update.deserialize_json(data["update"])
    return out
