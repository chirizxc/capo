"""Generated from Smithy shape ``com.amazonaws.eks#NodeResourcesFitConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.scoring_strategy


class NodeResourcesFitConfig(TypedDict, closed=True):
    scoring_strategy: NotRequired["capo_eks.types.scoring_strategy.ScoringStrategy"]
    """<p>The scoring strategy used to rank nodes during scheduling.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeResourcesFitConfig) -> dict:
    out: dict = {}
    if "scoring_strategy" in value:
        import capo_eks.types.scoring_strategy

        out["scoringStrategy"] = capo_eks.types.scoring_strategy.serialize_json(
            value["scoring_strategy"]
        )
    return out


def deserialize_json(data: dict) -> NodeResourcesFitConfig:
    out: NodeResourcesFitConfig = {}  # type: ignore[typeddict-item]
    if data.get("scoringStrategy") is not None:
        import capo_eks.types.scoring_strategy

        out["scoring_strategy"] = capo_eks.types.scoring_strategy.deserialize_json(
            data["scoringStrategy"]
        )
    return out
