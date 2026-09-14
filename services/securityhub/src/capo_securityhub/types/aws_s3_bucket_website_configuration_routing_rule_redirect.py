"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketWebsiteConfigurationRoutingRuleRedirect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsS3BucketWebsiteConfigurationRoutingRuleRedirect(TypedDict, closed=True):
    hostname: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The host name to use in the redirect request.</p>"""
    http_redirect_code: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The HTTP redirect code to use in the response.</p>"""
    protocol: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol to use to redirect the request. By default, uses the protocol from the original request.</p>"""
    replace_key_prefix_with: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The object key prefix to use in the redirect request.</p> <p>Cannot be provided if <code>ReplaceKeyWith</code> is present.</p>"""
    replace_key_with: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The specific object key to use in the redirect request.</p> <p>Cannot be provided if <code>ReplaceKeyPrefixWith</code> is present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketWebsiteConfigurationRoutingRuleRedirect) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["Hostname"] = value["hostname"]
    if "http_redirect_code" in value:
        out["HttpRedirectCode"] = value["http_redirect_code"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "replace_key_prefix_with" in value:
        out["ReplaceKeyPrefixWith"] = value["replace_key_prefix_with"]
    if "replace_key_with" in value:
        out["ReplaceKeyWith"] = value["replace_key_with"]
    return out


def deserialize_json(data: dict) -> AwsS3BucketWebsiteConfigurationRoutingRuleRedirect:
    out: AwsS3BucketWebsiteConfigurationRoutingRuleRedirect = {}  # type: ignore[typeddict-item]
    if data.get("Hostname") is not None:
        out["hostname"] = data["Hostname"]
    if data.get("HttpRedirectCode") is not None:
        out["http_redirect_code"] = data["HttpRedirectCode"]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("ReplaceKeyPrefixWith") is not None:
        out["replace_key_prefix_with"] = data["ReplaceKeyPrefixWith"]
    if data.get("ReplaceKeyWith") is not None:
        out["replace_key_with"] = data["ReplaceKeyWith"]
    return out
