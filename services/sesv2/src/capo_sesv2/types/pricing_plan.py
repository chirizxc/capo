"""Generated from Smithy shape ``com.amazonaws.sesv2#PricingPlan``."""

from typing import Literal, TypeAlias, cast

"""<p>Identifies an Amazon SES pricing plan. See <code>PutAccountPricingAttributesRequest$Plan</code> for the list of supported values and their meanings.</p>"""
PricingPlan: TypeAlias = Literal[
    "NONE",
    "ESSENTIALS",
    "PRO",
    "ENTERPRISE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlan) -> str:
    return value


def deserialize_json(data: str) -> PricingPlan:
    return cast(PricingPlan, data)
