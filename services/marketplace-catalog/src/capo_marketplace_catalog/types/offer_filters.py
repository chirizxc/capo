"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_availability_end_date_filter
    import capo_marketplace_catalog.types.offer_buyer_accounts_filter
    import capo_marketplace_catalog.types.offer_created_by_source_filter
    import capo_marketplace_catalog.types.offer_entity_id_filter
    import capo_marketplace_catalog.types.offer_last_modified_date_filter
    import capo_marketplace_catalog.types.offer_name_filter
    import capo_marketplace_catalog.types.offer_product_id_filter
    import capo_marketplace_catalog.types.offer_release_date_filter
    import capo_marketplace_catalog.types.offer_resale_authorization_id_filter
    import capo_marketplace_catalog.types.offer_set_id_filter
    import capo_marketplace_catalog.types.offer_state_filter
    import capo_marketplace_catalog.types.offer_target_agreement_id_filter
    import capo_marketplace_catalog.types.offer_target_agreement_intent_filter
    import capo_marketplace_catalog.types.offer_targeting_filter


class OfferFilters(TypedDict, closed=True):
    entity_id: NotRequired[
        "capo_marketplace_catalog.types.offer_entity_id_filter.OfferEntityIdFilter"
    ]
    """<p>Allows filtering on <code>EntityId</code> of an offer.</p>"""
    name: NotRequired[
        "capo_marketplace_catalog.types.offer_name_filter.OfferNameFilter"
    ]
    """<p>Allows filtering on the <code>Name</code> of an offer.</p>"""
    product_id: NotRequired[
        "capo_marketplace_catalog.types.offer_product_id_filter.OfferProductIdFilter"
    ]
    """<p>Allows filtering on the <code>ProductId</code> of an offer.</p>"""
    resale_authorization_id: NotRequired[
        "capo_marketplace_catalog.types.offer_resale_authorization_id_filter.OfferResaleAuthorizationIdFilter"
    ]
    """<p>Allows filtering on the <code>ResaleAuthorizationId</code> of an offer.</p> <note> <p>Not all offers have a <code>ResaleAuthorizationId</code>. The response will only include offers for which you have permissions.</p> </note>"""
    release_date: NotRequired[
        "capo_marketplace_catalog.types.offer_release_date_filter.OfferReleaseDateFilter"
    ]
    """<p>Allows filtering on the <code>ReleaseDate</code> of an offer.</p>"""
    availability_end_date: NotRequired[
        "capo_marketplace_catalog.types.offer_availability_end_date_filter.OfferAvailabilityEndDateFilter"
    ]
    """<p>Allows filtering on the <code>AvailabilityEndDate</code> of an offer.</p>"""
    buyer_accounts: NotRequired[
        "capo_marketplace_catalog.types.offer_buyer_accounts_filter.OfferBuyerAccountsFilter"
    ]
    """<p>Allows filtering on the <code>BuyerAccounts</code> of an offer.</p>"""
    state: NotRequired[
        "capo_marketplace_catalog.types.offer_state_filter.OfferStateFilter"
    ]
    """<p>Allows filtering on the <code>State</code> of an offer.</p>"""
    targeting: NotRequired[
        "capo_marketplace_catalog.types.offer_targeting_filter.OfferTargetingFilter"
    ]
    """<p>Allows filtering on the <code>Targeting</code> of an offer.</p>"""
    last_modified_date: NotRequired[
        "capo_marketplace_catalog.types.offer_last_modified_date_filter.OfferLastModifiedDateFilter"
    ]
    """<p>Allows filtering on the <code>LastModifiedDate</code> of an offer.</p>"""
    offer_set_id: NotRequired[
        "capo_marketplace_catalog.types.offer_set_id_filter.OfferSetIdFilter"
    ]
    """<p>Allows filtering on the <code>OfferSetId</code> of an offer.</p>"""
    target_agreement_id: NotRequired[
        "capo_marketplace_catalog.types.offer_target_agreement_id_filter.OfferTargetAgreementIdFilter"
    ]
    """<p>Allows filtering on the <code>TargetAgreementId</code> of an offer.</p>"""
    target_agreement_intent: NotRequired[
        "capo_marketplace_catalog.types.offer_target_agreement_intent_filter.OfferTargetAgreementIntentFilter"
    ]
    """<p>Allows filtering on the <code>TargetAgreementIntent</code> of an offer.</p>"""
    created_by_source: NotRequired[
        "capo_marketplace_catalog.types.offer_created_by_source_filter.OfferCreatedBySourceFilter"
    ]
    """<p>Allows filtering on the <code>CreatedBySource</code> of an offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OfferFilters) -> dict:
    out: dict = {}
    if "entity_id" in value:
        import capo_marketplace_catalog.types.offer_entity_id_filter

        out["EntityId"] = (
            capo_marketplace_catalog.types.offer_entity_id_filter.serialize_json(
                value["entity_id"]
            )
        )
    if "name" in value:
        import capo_marketplace_catalog.types.offer_name_filter

        out["Name"] = capo_marketplace_catalog.types.offer_name_filter.serialize_json(
            value["name"]
        )
    if "product_id" in value:
        import capo_marketplace_catalog.types.offer_product_id_filter

        out["ProductId"] = (
            capo_marketplace_catalog.types.offer_product_id_filter.serialize_json(
                value["product_id"]
            )
        )
    if "resale_authorization_id" in value:
        import capo_marketplace_catalog.types.offer_resale_authorization_id_filter

        out["ResaleAuthorizationId"] = (
            capo_marketplace_catalog.types.offer_resale_authorization_id_filter.serialize_json(
                value["resale_authorization_id"]
            )
        )
    if "release_date" in value:
        import capo_marketplace_catalog.types.offer_release_date_filter

        out["ReleaseDate"] = (
            capo_marketplace_catalog.types.offer_release_date_filter.serialize_json(
                value["release_date"]
            )
        )
    if "availability_end_date" in value:
        import capo_marketplace_catalog.types.offer_availability_end_date_filter

        out["AvailabilityEndDate"] = (
            capo_marketplace_catalog.types.offer_availability_end_date_filter.serialize_json(
                value["availability_end_date"]
            )
        )
    if "buyer_accounts" in value:
        import capo_marketplace_catalog.types.offer_buyer_accounts_filter

        out["BuyerAccounts"] = (
            capo_marketplace_catalog.types.offer_buyer_accounts_filter.serialize_json(
                value["buyer_accounts"]
            )
        )
    if "state" in value:
        import capo_marketplace_catalog.types.offer_state_filter

        out["State"] = capo_marketplace_catalog.types.offer_state_filter.serialize_json(
            value["state"]
        )
    if "targeting" in value:
        import capo_marketplace_catalog.types.offer_targeting_filter

        out["Targeting"] = (
            capo_marketplace_catalog.types.offer_targeting_filter.serialize_json(
                value["targeting"]
            )
        )
    if "last_modified_date" in value:
        import capo_marketplace_catalog.types.offer_last_modified_date_filter

        out["LastModifiedDate"] = (
            capo_marketplace_catalog.types.offer_last_modified_date_filter.serialize_json(
                value["last_modified_date"]
            )
        )
    if "offer_set_id" in value:
        import capo_marketplace_catalog.types.offer_set_id_filter

        out["OfferSetId"] = (
            capo_marketplace_catalog.types.offer_set_id_filter.serialize_json(
                value["offer_set_id"]
            )
        )
    if "target_agreement_id" in value:
        import capo_marketplace_catalog.types.offer_target_agreement_id_filter

        out["TargetAgreementId"] = (
            capo_marketplace_catalog.types.offer_target_agreement_id_filter.serialize_json(
                value["target_agreement_id"]
            )
        )
    if "target_agreement_intent" in value:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_filter

        out["TargetAgreementIntent"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_filter.serialize_json(
                value["target_agreement_intent"]
            )
        )
    if "created_by_source" in value:
        import capo_marketplace_catalog.types.offer_created_by_source_filter

        out["CreatedBySource"] = (
            capo_marketplace_catalog.types.offer_created_by_source_filter.serialize_json(
                value["created_by_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> OfferFilters:
    out: OfferFilters = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        import capo_marketplace_catalog.types.offer_entity_id_filter

        out["entity_id"] = (
            capo_marketplace_catalog.types.offer_entity_id_filter.deserialize_json(
                data["EntityId"]
            )
        )
    if data.get("Name") is not None:
        import capo_marketplace_catalog.types.offer_name_filter

        out["name"] = capo_marketplace_catalog.types.offer_name_filter.deserialize_json(
            data["Name"]
        )
    if data.get("ProductId") is not None:
        import capo_marketplace_catalog.types.offer_product_id_filter

        out["product_id"] = (
            capo_marketplace_catalog.types.offer_product_id_filter.deserialize_json(
                data["ProductId"]
            )
        )
    if data.get("ResaleAuthorizationId") is not None:
        import capo_marketplace_catalog.types.offer_resale_authorization_id_filter

        out["resale_authorization_id"] = (
            capo_marketplace_catalog.types.offer_resale_authorization_id_filter.deserialize_json(
                data["ResaleAuthorizationId"]
            )
        )
    if data.get("ReleaseDate") is not None:
        import capo_marketplace_catalog.types.offer_release_date_filter

        out["release_date"] = (
            capo_marketplace_catalog.types.offer_release_date_filter.deserialize_json(
                data["ReleaseDate"]
            )
        )
    if data.get("AvailabilityEndDate") is not None:
        import capo_marketplace_catalog.types.offer_availability_end_date_filter

        out["availability_end_date"] = (
            capo_marketplace_catalog.types.offer_availability_end_date_filter.deserialize_json(
                data["AvailabilityEndDate"]
            )
        )
    if data.get("BuyerAccounts") is not None:
        import capo_marketplace_catalog.types.offer_buyer_accounts_filter

        out["buyer_accounts"] = (
            capo_marketplace_catalog.types.offer_buyer_accounts_filter.deserialize_json(
                data["BuyerAccounts"]
            )
        )
    if data.get("State") is not None:
        import capo_marketplace_catalog.types.offer_state_filter

        out["state"] = (
            capo_marketplace_catalog.types.offer_state_filter.deserialize_json(
                data["State"]
            )
        )
    if data.get("Targeting") is not None:
        import capo_marketplace_catalog.types.offer_targeting_filter

        out["targeting"] = (
            capo_marketplace_catalog.types.offer_targeting_filter.deserialize_json(
                data["Targeting"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_marketplace_catalog.types.offer_last_modified_date_filter

        out["last_modified_date"] = (
            capo_marketplace_catalog.types.offer_last_modified_date_filter.deserialize_json(
                data["LastModifiedDate"]
            )
        )
    if data.get("OfferSetId") is not None:
        import capo_marketplace_catalog.types.offer_set_id_filter

        out["offer_set_id"] = (
            capo_marketplace_catalog.types.offer_set_id_filter.deserialize_json(
                data["OfferSetId"]
            )
        )
    if data.get("TargetAgreementId") is not None:
        import capo_marketplace_catalog.types.offer_target_agreement_id_filter

        out["target_agreement_id"] = (
            capo_marketplace_catalog.types.offer_target_agreement_id_filter.deserialize_json(
                data["TargetAgreementId"]
            )
        )
    if data.get("TargetAgreementIntent") is not None:
        import capo_marketplace_catalog.types.offer_target_agreement_intent_filter

        out["target_agreement_intent"] = (
            capo_marketplace_catalog.types.offer_target_agreement_intent_filter.deserialize_json(
                data["TargetAgreementIntent"]
            )
        )
    if data.get("CreatedBySource") is not None:
        import capo_marketplace_catalog.types.offer_created_by_source_filter

        out["created_by_source"] = (
            capo_marketplace_catalog.types.offer_created_by_source_filter.deserialize_json(
                data["CreatedBySource"]
            )
        )
    return out
