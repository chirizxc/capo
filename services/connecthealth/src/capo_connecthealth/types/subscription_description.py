"""Generated from Smithy shape ``com.amazonaws.connecthealth#SubscriptionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.domain_id
    import capo_connecthealth.types.subscription_arn
    import capo_connecthealth.types.subscription_id
    import capo_connecthealth.types.subscription_status


class SubscriptionDescription(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p/>"""
    subscription_id: "capo_connecthealth.types.subscription_id.SubscriptionId"
    """<p/>"""
    arn: "capo_connecthealth.types.subscription_arn.SubscriptionArn"
    """<p/>"""
    status: "capo_connecthealth.types.subscription_status.SubscriptionStatus"
    """<p/>"""
    created_at: "datetime.datetime"
    """<p/>"""
    last_updated_at: "datetime.datetime"
    """<p/>"""
    activated_at: NotRequired["datetime.datetime"]
    """<p/>"""
    deactivated_at: NotRequired["datetime.datetime"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionDescription) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["subscriptionId"] = value["subscription_id"]
    out["arn"] = value["arn"]
    import capo_connecthealth.types.subscription_status

    out["status"] = capo_connecthealth.types.subscription_status.serialize_json(
        value["status"]
    )
    import capo_connecthealth.types._prelude.timestamp

    out["createdAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_connecthealth.types._prelude.timestamp

    out["lastUpdatedAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "activated_at" in value:
        import capo_connecthealth.types._prelude.timestamp

        out["activatedAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
            value["activated_at"]
        )
    if "deactivated_at" in value:
        import capo_connecthealth.types._prelude.timestamp

        out["deactivatedAt"] = (
            capo_connecthealth.types._prelude.timestamp.serialize_json(
                value["deactivated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscriptionDescription:
    out: SubscriptionDescription = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("SubscriptionDescription.domain_id required")
    if data.get("subscriptionId") is not None:
        out["subscription_id"] = data["subscriptionId"]
    else:
        raise DeserializationError("SubscriptionDescription.subscription_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("SubscriptionDescription.arn required")
    if data.get("status") is not None:
        import capo_connecthealth.types.subscription_status

        out["status"] = capo_connecthealth.types.subscription_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SubscriptionDescription.status required")
    if data.get("createdAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SubscriptionDescription.created_at required")
    if data.get("lastUpdatedAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("SubscriptionDescription.last_updated_at required")
    if data.get("activatedAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["activated_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["activatedAt"]
            )
        )
    if data.get("deactivatedAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["deactivated_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["deactivatedAt"]
            )
        )
    return out
