"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetRelation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.topic_v2_data_set_relation_endpoint


class TopicV2DataSetRelation(TypedDict, closed=True):
    left: "capo_quicksight.types.topic_v2_data_set_relation_endpoint.TopicV2DataSetRelationEndpoint"
    """<p>The left endpoint of the data set relation.</p>"""
    right: "capo_quicksight.types.topic_v2_data_set_relation_endpoint.TopicV2DataSetRelationEndpoint"
    """<p>The right endpoint of the data set relation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetRelation) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_v2_data_set_relation_endpoint

    out["Left"] = (
        capo_quicksight.types.topic_v2_data_set_relation_endpoint.serialize_json(
            value["left"]
        )
    )
    import capo_quicksight.types.topic_v2_data_set_relation_endpoint

    out["Right"] = (
        capo_quicksight.types.topic_v2_data_set_relation_endpoint.serialize_json(
            value["right"]
        )
    )
    return out


def deserialize_json(data: dict) -> TopicV2DataSetRelation:
    out: TopicV2DataSetRelation = {}  # type: ignore[typeddict-item]
    if data.get("Left") is not None:
        import capo_quicksight.types.topic_v2_data_set_relation_endpoint

        out["left"] = (
            capo_quicksight.types.topic_v2_data_set_relation_endpoint.deserialize_json(
                data["Left"]
            )
        )
    else:
        raise DeserializationError("TopicV2DataSetRelation.left required")
    if data.get("Right") is not None:
        import capo_quicksight.types.topic_v2_data_set_relation_endpoint

        out["right"] = (
            capo_quicksight.types.topic_v2_data_set_relation_endpoint.deserialize_json(
                data["Right"]
            )
        )
    else:
        raise DeserializationError("TopicV2DataSetRelation.right required")
    return out
