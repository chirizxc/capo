"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#DisplayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.resolution


class DisplayConfiguration(TypedDict, closed=True):
    resolution: NotRequired["capo_gameliftstreams.types.resolution.Resolution"]
    """<p>The resolution to apply to the stream session's virtual monitor. When specified, this value overrides the default resolution of 1920 × 1080.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisplayConfiguration) -> dict:
    out: dict = {}
    if "resolution" in value:
        import capo_gameliftstreams.types.resolution

        out["Resolution"] = capo_gameliftstreams.types.resolution.serialize_json(
            value["resolution"]
        )
    return out


def deserialize_json(data: dict) -> DisplayConfiguration:
    out: DisplayConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Resolution") is not None:
        import capo_gameliftstreams.types.resolution

        out["resolution"] = capo_gameliftstreams.types.resolution.deserialize_json(
            data["Resolution"]
        )
    return out
