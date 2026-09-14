"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.index_state


class CreateIndexOutput(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The ARN of the new local index for the Region. You can reference this ARN in IAM permission policies to authorize the following operations: <a>DeleteIndex</a> | <a>GetIndex</a> | <a>UpdateIndexType</a> | <a>CreateView</a> </p>"""
    state: NotRequired["capo_resource_explorer_2.types.index_state.IndexState"]
    """<p>Indicates the current state of the index. You can check for changes to the state for asynchronous operations by calling the <a>GetIndex</a> operation.</p> <note> <p>The state can remain in the <code>CREATING</code> or <code>UPDATING</code> state for several hours as Resource Explorer discovers the information about your resources and populates the index.</p> </note>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and timestamp when the index was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "state" in value:
        out["State"] = value["state"]
    if "created_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["CreatedAt"] = capo_resource_explorer_2._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateIndexOutput:
    out: CreateIndexOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    return out
