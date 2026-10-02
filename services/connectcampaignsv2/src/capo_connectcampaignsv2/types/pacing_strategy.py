"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PacingStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.abandonment_rate_pacing_config


class _PacingStrategy_abandonmentRate(TypedDict, closed=True):
    abandonmentRate: "capo_connectcampaignsv2.types.abandonment_rate_pacing_config.AbandonmentRatePacingConfig"


PacingStrategy: TypeAlias = _PacingStrategy_abandonmentRate


# --- restJson1 ser/de ---
def serialize_json(value: PacingStrategy) -> dict:
    if "abandonmentRate" in value:
        import capo_connectcampaignsv2.types.abandonment_rate_pacing_config

        return {
            "abandonmentRate": capo_connectcampaignsv2.types.abandonment_rate_pacing_config.serialize_json(
                value["abandonmentRate"]
            )
        }
    else:
        raise SerializationError("PacingStrategy: no variant present")


def deserialize_json(data: dict) -> PacingStrategy:
    if data.get("abandonmentRate") is not None:
        import capo_connectcampaignsv2.types.abandonment_rate_pacing_config

        return {
            "abandonmentRate": capo_connectcampaignsv2.types.abandonment_rate_pacing_config.deserialize_json(
                data["abandonmentRate"]
            )
        }
    else:
        raise DeserializationError("PacingStrategy: no recognized variant key")
