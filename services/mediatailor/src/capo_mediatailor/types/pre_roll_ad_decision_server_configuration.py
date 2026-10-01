"""Generated from Smithy shape ``com.amazonaws.mediatailor#PreRollAdDecisionServerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.pre_roll_vast_response


class PreRollAdDecisionServerConfiguration(TypedDict, closed=True):
    vast_response: NotRequired[
        "capo_mediatailor.types.pre_roll_vast_response.PreRollVastResponse"
    ]
    """<p>The settings that control how MediaTailor processes VAST responses for live pre-roll ad breaks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreRollAdDecisionServerConfiguration) -> dict:
    out: dict = {}
    if "vast_response" in value:
        import capo_mediatailor.types.pre_roll_vast_response

        out["VastResponse"] = (
            capo_mediatailor.types.pre_roll_vast_response.serialize_json(
                value["vast_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> PreRollAdDecisionServerConfiguration:
    out: PreRollAdDecisionServerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("VastResponse") is not None:
        import capo_mediatailor.types.pre_roll_vast_response

        out["vast_response"] = (
            capo_mediatailor.types.pre_roll_vast_response.deserialize_json(
                data["VastResponse"]
            )
        )
    return out
