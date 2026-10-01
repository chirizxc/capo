"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferTargetAgreementIntentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list


class OfferTargetAgreementIntentFilter(TypedDict, closed=True):
    value_list: NotRequired[
        "capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list.OfferTargetAgreementIntentFilterValueList"
    ]
    """<p>Allows filtering on the <code>TargetAgreementIntent</code> of an offer with list input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferTargetAgreementIntentFilter) -> dict:
    out: dict = {}
    if "value_list" in value:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list

        out["ValueList"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list.serialize_json(
                value["value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferTargetAgreementIntentFilter:
    out: OfferTargetAgreementIntentFilter = {}  # type: ignore[typeddict-item]
    if data.get("ValueList") is not None:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list

        out["value_list"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_filter_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    return out
