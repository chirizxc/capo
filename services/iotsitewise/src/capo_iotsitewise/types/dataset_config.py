"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.session_config


class DatasetConfig(TypedDict, closed=True):
    session: NotRequired["capo_iotsitewise.types.session_config.SessionConfig"]
    """<p>The session configuration for a session-type dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetConfig) -> dict:
    out: dict = {}
    if "session" in value:
        import capo_iotsitewise.types.session_config

        out["session"] = capo_iotsitewise.types.session_config.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> DatasetConfig:
    out: DatasetConfig = {}  # type: ignore[typeddict-item]
    if data.get("session") is not None:
        import capo_iotsitewise.types.session_config

        out["session"] = capo_iotsitewise.types.session_config.deserialize_json(
            data["session"]
        )
    return out
