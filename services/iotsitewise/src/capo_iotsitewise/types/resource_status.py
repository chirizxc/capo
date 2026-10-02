"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ResourceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_error
    import capo_iotsitewise.types.resource_state


class ResourceStatus(TypedDict, closed=True):
    error: NotRequired["capo_iotsitewise.types.resource_error.ResourceError"]
    """<p>Contains associated error information, if any.</p>"""
    state: NotRequired["capo_iotsitewise.types.resource_state.ResourceState"]
    """<p>The current status of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> dict:
    out: dict = {}
    if "error" in value:
        import capo_iotsitewise.types.resource_error

        out["error"] = capo_iotsitewise.types.resource_error.serialize_json(
            value["error"]
        )
    if "state" in value:
        import capo_iotsitewise.types.resource_state

        out["state"] = capo_iotsitewise.types.resource_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ResourceStatus:
    out: ResourceStatus = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        import capo_iotsitewise.types.resource_error

        out["error"] = capo_iotsitewise.types.resource_error.deserialize_json(
            data["error"]
        )
    if data.get("state") is not None:
        import capo_iotsitewise.types.resource_state

        out["state"] = capo_iotsitewise.types.resource_state.deserialize_json(
            data["state"]
        )
    return out
