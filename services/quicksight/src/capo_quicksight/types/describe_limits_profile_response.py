"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeLimitsProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.limits_profile


class DescribeLimitsProfileResponse(TypedDict, closed=True):
    profile: "capo_quicksight.types.limits_profile.LimitsProfile"
    """<p>The details of the requested limits profile, including its name, description, resource limits, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLimitsProfileResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.limits_profile

    out["profile"] = capo_quicksight.types.limits_profile.serialize_json(
        value["profile"]
    )
    return out


def deserialize_json(data: dict) -> DescribeLimitsProfileResponse:
    out: DescribeLimitsProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("profile") is not None:
        import capo_quicksight.types.limits_profile

        out["profile"] = capo_quicksight.types.limits_profile.deserialize_json(
            data["profile"]
        )
    else:
        raise DeserializationError("DescribeLimitsProfileResponse.profile required")
    return out
