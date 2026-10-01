"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeleteTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_status


class DeleteTaskResponse(TypedDict, closed=True):
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTaskResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteTaskResponse:
    out: DeleteTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteTaskResponse.status required")
    return out
