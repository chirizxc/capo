"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetDependencyInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class GetDependencyInsightsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: GetDependencyInsightsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDependencyInsightsRequest:
    out: GetDependencyInsightsRequest = {}  # type: ignore[typeddict-item]
    return out
