"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.date_time_iso8601
    import capo_marketplace_catalog.types.offer_buyer_accounts_list
    import capo_marketplace_catalog.types.offer_created_by_source_string
    import capo_marketplace_catalog.types.offer_name_string
    import capo_marketplace_catalog.types.offer_product_id_string
    import capo_marketplace_catalog.types.offer_resale_authorization_id_string
    import capo_marketplace_catalog.types.offer_set_id_string
    import capo_marketplace_catalog.types.offer_state_string
    import capo_marketplace_catalog.types.offer_target_agreement_id_string
    import capo_marketplace_catalog.types.offer_target_agreement_intent_string
    import capo_marketplace_catalog.types.offer_targeting_list


class OfferSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_marketplace_catalog.types.offer_name_string.OfferNameString"
    ]
    """<p>The name of the offer.</p>"""
    product_id: NotRequired[
        "capo_marketplace_catalog.types.offer_product_id_string.OfferProductIdString"
    ]
    """<p>The product ID of the offer.</p>"""
    resale_authorization_id: NotRequired[
        "capo_marketplace_catalog.types.offer_resale_authorization_id_string.OfferResaleAuthorizationIdString"
    ]
    """<p>The ResaleAuthorizationId of the offer.</p>"""
    release_date: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The release date of the offer.</p>"""
    availability_end_date: NotRequired[
        "capo_marketplace_catalog.types.date_time_iso8601.DateTimeISO8601"
    ]
    """<p>The availability end date of the offer.</p>"""
    buyer_accounts: NotRequired[
        "capo_marketplace_catalog.types.offer_buyer_accounts_list.OfferBuyerAccountsList"
    ]
    """<p>The buyer accounts in the offer.</p>"""
    state: NotRequired[
        "capo_marketplace_catalog.types.offer_state_string.OfferStateString"
    ]
    """<p>The status of the offer.</p>"""
    targeting: NotRequired[
        "capo_marketplace_catalog.types.offer_targeting_list.OfferTargetingList"
    ]
    """<p>The targeting in the offer.</p>"""
    offer_set_id: NotRequired[
        "capo_marketplace_catalog.types.offer_set_id_string.OfferSetIdString"
    ]
    """<p>The offer set ID of the offer.</p>"""
    target_agreement_id: NotRequired[
        "capo_marketplace_catalog.types.offer_target_agreement_id_string.OfferTargetAgreementIdString"
    ]
    """<p>The target agreement ID of the offer.</p>"""
    target_agreement_intent: NotRequired[
        "capo_marketplace_catalog.types.offer_target_agreement_intent_string.OfferTargetAgreementIntentString"
    ]
    """<p>The target agreement intent of the offer.</p>"""
    created_by_source: NotRequired[
        "capo_marketplace_catalog.types.offer_created_by_source_string.OfferCreatedBySourceString"
    ]
    """<p>The creation source of the offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "resale_authorization_id" in value:
        out["ResaleAuthorizationId"] = value["resale_authorization_id"]
    if "release_date" in value:
        out["ReleaseDate"] = value["release_date"]
    if "availability_end_date" in value:
        out["AvailabilityEndDate"] = value["availability_end_date"]
    if "buyer_accounts" in value:
        import capo_marketplace_catalog.types.offer_buyer_accounts_list

        out["BuyerAccounts"] = (
            capo_marketplace_catalog.types.offer_buyer_accounts_list.serialize_json(
                value["buyer_accounts"]
            )
        )
    if "state" in value:
        import capo_marketplace_catalog.types.offer_state_string

        out["State"] = capo_marketplace_catalog.types.offer_state_string.serialize_json(
            value["state"]
        )
    if "targeting" in value:
        import capo_marketplace_catalog.types.offer_targeting_list

        out["Targeting"] = (
            capo_marketplace_catalog.types.offer_targeting_list.serialize_json(
                value["targeting"]
            )
        )
    if "offer_set_id" in value:
        out["OfferSetId"] = value["offer_set_id"]
    if "target_agreement_id" in value:
        out["TargetAgreementId"] = value["target_agreement_id"]
    if "target_agreement_intent" in value:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_string

        out["TargetAgreementIntent"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_string.serialize_json(
                value["target_agreement_intent"]
            )
        )
    if "created_by_source" in value:
        import capo_marketplace_catalog.types.offer_created_by_source_string

        out["CreatedBySource"] = (
            capo_marketplace_catalog.types.offer_created_by_source_string.serialize_json(
                value["created_by_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferSummary:
    out: OfferSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ResaleAuthorizationId") is not None:
        out["resale_authorization_id"] = data["ResaleAuthorizationId"]
    if data.get("ReleaseDate") is not None:
        out["release_date"] = data["ReleaseDate"]
    if data.get("AvailabilityEndDate") is not None:
        out["availability_end_date"] = data["AvailabilityEndDate"]
    if data.get("BuyerAccounts") is not None:
        import capo_marketplace_catalog.types.offer_buyer_accounts_list

        out["buyer_accounts"] = (
            capo_marketplace_catalog.types.offer_buyer_accounts_list.deserialize_json(
                data["BuyerAccounts"]
            )
        )
    if data.get("State") is not None:
        import capo_marketplace_catalog.types.offer_state_string

        out["state"] = (
            capo_marketplace_catalog.types.offer_state_string.deserialize_json(
                data["State"]
            )
        )
    if data.get("Targeting") is not None:
        import capo_marketplace_catalog.types.offer_targeting_list

        out["targeting"] = (
            capo_marketplace_catalog.types.offer_targeting_list.deserialize_json(
                data["Targeting"]
            )
        )
    if data.get("OfferSetId") is not None:
        out["offer_set_id"] = data["OfferSetId"]
    if data.get("TargetAgreementId") is not None:
        out["target_agreement_id"] = data["TargetAgreementId"]
    if data.get("TargetAgreementIntent") is not None:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_string

        out["target_agreement_intent"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_string.deserialize_json(
                data["TargetAgreementIntent"]
            )
        )
    if data.get("CreatedBySource") is not None:
        import capo_marketplace_catalog.types.offer_created_by_source_string

        out["created_by_source"] = (
            capo_marketplace_catalog.types.offer_created_by_source_string.deserialize_json(
                data["CreatedBySource"]
            )
        )
    return out
