"""Generated from Smithy shape ``com.amazonaws.connect#ContentAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.recommender_config


class ContentAttributes(TypedDict, closed=True):
    recommender_config: NotRequired[
        "capo_connect.types.recommender_config.RecommenderConfig"
    ]
    """<p>Configuration for the recommender used to generate personalized recommendations for the notification content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContentAttributes) -> dict:
    out: dict = {}
    if "recommender_config" in value:
        import capo_connect.types.recommender_config

        out["RecommenderConfig"] = capo_connect.types.recommender_config.serialize_json(
            value["recommender_config"]
        )
    return out


def deserialize_json(data: dict) -> ContentAttributes:
    out: ContentAttributes = {}  # type: ignore[typeddict-item]
    if data.get("RecommenderConfig") is not None:
        import capo_connect.types.recommender_config

        out["recommender_config"] = (
            capo_connect.types.recommender_config.deserialize_json(
                data["RecommenderConfig"]
            )
        )
    return out
