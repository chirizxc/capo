"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountPricingAttributesResponse``."""

from typing_extensions import TypedDict


class PutAccountPricingAttributesResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountPricingAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutAccountPricingAttributesResponse:
    out: PutAccountPricingAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
