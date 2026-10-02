"""Generated from Smithy shape ``com.amazonaws.eks#NodeResourcesFitVersionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.scoring_strategy_config


class NodeResourcesFitVersionConfig(TypedDict, closed=True):
    scoring_strategy: NotRequired[
        "capo_eks.types.scoring_strategy_config.ScoringStrategyConfig"
    ]
    """<p>The scoring strategy configuration with default value and constraints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeResourcesFitVersionConfig) -> dict:
    out: dict = {}
    if "scoring_strategy" in value:
        import capo_eks.types.scoring_strategy_config

        out["scoringStrategy"] = capo_eks.types.scoring_strategy_config.serialize_json(
            value["scoring_strategy"]
        )
    return out


def deserialize_json(data: dict) -> NodeResourcesFitVersionConfig:
    out: NodeResourcesFitVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("scoringStrategy") is not None:
        import capo_eks.types.scoring_strategy_config

        out["scoring_strategy"] = (
            capo_eks.types.scoring_strategy_config.deserialize_json(
                data["scoringStrategy"]
            )
        )
    return out
