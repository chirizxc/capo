"""Generated from Smithy shape ``com.amazonaws.eks#DurationParameterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.duration_constraints
    import capo_eks.types.string


class DurationParameterConfig(TypedDict, closed=True):
    default_value: NotRequired["capo_eks.types.string.String"]
    """<p>The default value for the duration parameter.</p>"""
    constraints: NotRequired["capo_eks.types.duration_constraints.DurationConstraints"]
    """<p>The constraints for the duration parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DurationParameterConfig) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "constraints" in value:
        import capo_eks.types.duration_constraints

        out["constraints"] = capo_eks.types.duration_constraints.serialize_json(
            value["constraints"]
        )
    return out


def deserialize_json(data: dict) -> DurationParameterConfig:
    out: DurationParameterConfig = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("constraints") is not None:
        import capo_eks.types.duration_constraints

        out["constraints"] = capo_eks.types.duration_constraints.deserialize_json(
            data["constraints"]
        )
    return out
