"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateFeedRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.update_output_list


class UpdateFeedRequest(TypedDict, closed=True):
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>Required. You can specify the existing name (to leave it unchanged) or a new name. </p>"""
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed to update.</p>"""
    outputs: "capo_elementalinference.types.update_output_list.UpdateOutputList"
    """<p>Required. You can specify the existing array of outputs (to leave outputs unchanged) or you can specify a new array. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFeedRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_elementalinference.types.update_output_list

    out["outputs"] = capo_elementalinference.types.update_output_list.serialize_json(
        value["outputs"]
    )
    return out


def deserialize_json(data: dict) -> UpdateFeedRequest:
    out: UpdateFeedRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFeedRequest.name required")
    if data.get("outputs") is not None:
        import capo_elementalinference.types.update_output_list

        out["outputs"] = (
            capo_elementalinference.types.update_output_list.deserialize_json(
                data["outputs"]
            )
        )
    else:
        raise DeserializationError("UpdateFeedRequest.outputs required")
    return out
