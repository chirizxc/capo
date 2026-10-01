"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DeletePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.resource_status


class DeletePipelineResponse(TypedDict, closed=True):
    status: "capo_iotsitewise.types.resource_status.ResourceStatus"
    """<p>The current lifecycle status of the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipelineResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.resource_status

    out["status"] = capo_iotsitewise.types.resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeletePipelineResponse:
    out: DeletePipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_iotsitewise.types.resource_status

        out["status"] = capo_iotsitewise.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeletePipelineResponse.status required")
    return out
