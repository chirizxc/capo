"""Generated from Smithy shape ``com.amazonaws.connect#RecommenderContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.recommender_context_key
    import capo_connect.types.recommender_context_value

RecommenderContext: TypeAlias = dict[
    "capo_connect.types.recommender_context_key.RecommenderContextKey",
    "capo_connect.types.recommender_context_value.RecommenderContextValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecommenderContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RecommenderContext:
    out: RecommenderContext = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
