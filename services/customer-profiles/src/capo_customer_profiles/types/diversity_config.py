"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DiversityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.diversity_columns_list


class DiversityConfig(TypedDict, closed=True):
    diversity_columns: NotRequired[
        "capo_customer_profiles.types.diversity_columns_list.DiversityColumnsList"
    ]
    """<p>A list of up to two diversity columns. Each column defines a cap on the number or percentage of recommended items that share the same value for that column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiversityConfig) -> dict:
    out: dict = {}
    if "diversity_columns" in value:
        import capo_customer_profiles.types.diversity_columns_list

        out["DiversityColumns"] = (
            capo_customer_profiles.types.diversity_columns_list.serialize_json(
                value["diversity_columns"]
            )
        )
    return out


def deserialize_json(data: dict) -> DiversityConfig:
    out: DiversityConfig = {}  # type: ignore[typeddict-item]
    if data.get("DiversityColumns") is not None:
        import capo_customer_profiles.types.diversity_columns_list

        out["diversity_columns"] = (
            capo_customer_profiles.types.diversity_columns_list.deserialize_json(
                data["DiversityColumns"]
            )
        )
    return out
