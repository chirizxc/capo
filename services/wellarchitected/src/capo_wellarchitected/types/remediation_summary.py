"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RemediationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.recommended_fix_steps


class RemediationSummary(TypedDict, closed=True):
    recommendation: "str"
    """<p>A short imperative statement of the recommended action.</p>"""
    steps: "capo_wellarchitected.types.recommended_fix_steps.RecommendedFixSteps"
    """<p>High-level steps to implement the fix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationSummary) -> dict:
    out: dict = {}
    out["recommendation"] = value["recommendation"]
    import capo_wellarchitected.types.recommended_fix_steps

    out["steps"] = capo_wellarchitected.types.recommended_fix_steps.serialize_json(
        value["steps"]
    )
    return out


def deserialize_json(data: dict) -> RemediationSummary:
    out: RemediationSummary = {}  # type: ignore[typeddict-item]
    if data.get("recommendation") is not None:
        out["recommendation"] = data["recommendation"]
    else:
        raise DeserializationError("RemediationSummary.recommendation required")
    if data.get("steps") is not None:
        import capo_wellarchitected.types.recommended_fix_steps

        out["steps"] = (
            capo_wellarchitected.types.recommended_fix_steps.deserialize_json(
                data["steps"]
            )
        )
    else:
        raise DeserializationError("RemediationSummary.steps required")
    return out
