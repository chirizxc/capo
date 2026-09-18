"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#StopProductSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.identity_provider


class StopProductSubscriptionRequest(TypedDict, closed=True):
    username: NotRequired["str"]
    """<p>The user name from the identity provider for the user.</p>"""
    identity_provider: NotRequired[
        "capo_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    ]
    """<p>An object that specifies details for the identity provider.</p>"""
    product: NotRequired["str"]
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    product_user_arn: NotRequired[
        "capo_license_manager_user_subscriptions.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the product user.</p>"""
    domain: NotRequired["str"]
    """<p>The domain name of the Active Directory that contains the user for whom to stop the product subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopProductSubscriptionRequest) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "identity_provider" in value:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["IdentityProvider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    if "product" in value:
        out["Product"] = value["product"]
    if "product_user_arn" in value:
        out["ProductUserArn"] = value["product_user_arn"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> StopProductSubscriptionRequest:
    out: StopProductSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("IdentityProvider") is not None:
        import capo_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            capo_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    if data.get("Product") is not None:
        out["product"] = data["Product"]
    if data.get("ProductUserArn") is not None:
        out["product_user_arn"] = data["ProductUserArn"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    return out
