"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommendationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.metadata_columns_list


class RecommendationMetadata(TypedDict, closed=True):
    columns: NotRequired[
        "capo_customer_profiles.types.metadata_columns_list.MetadataColumnsList"
    ]
    """<p>A list of metadata column names from your Items dataset to include in the recommendation response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationMetadata) -> dict:
    out: dict = {}
    if "columns" in value:
        import capo_customer_profiles.types.metadata_columns_list

        out["Columns"] = (
            capo_customer_profiles.types.metadata_columns_list.serialize_json(
                value["columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationMetadata:
    out: RecommendationMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Columns") is not None:
        import capo_customer_profiles.types.metadata_columns_list

        out["columns"] = (
            capo_customer_profiles.types.metadata_columns_list.deserialize_json(
                data["Columns"]
            )
        )
    return out
