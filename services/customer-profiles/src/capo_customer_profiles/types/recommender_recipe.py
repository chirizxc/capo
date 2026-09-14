"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderRecipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.recommender_recipe_name


class RecommenderRecipe(TypedDict, closed=True):
    name: NotRequired[
        "capo_customer_profiles.types.recommender_recipe_name.RecommenderRecipeName"
    ]
    """<p>The name of the recommender recipe.</p>"""
    description: NotRequired["str"]
    """<p>A description of the recommender recipe's purpose and functionality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderRecipe) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_customer_profiles.types.recommender_recipe_name

        out["name"] = (
            capo_customer_profiles.types.recommender_recipe_name.serialize_json(
                value["name"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> RecommenderRecipe:
    out: RecommenderRecipe = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_customer_profiles.types.recommender_recipe_name

        out["name"] = (
            capo_customer_profiles.types.recommender_recipe_name.deserialize_json(
                data["name"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
