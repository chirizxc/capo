"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableSecurityHubFeatureV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.feature_name


class DisableSecurityHubFeatureV2Request(TypedDict, closed=True):
    feature_name: "capo_securityhub.types.feature_name.FeatureName"
    """<p>The name of the feature to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableSecurityHubFeatureV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableSecurityHubFeatureV2Request:
    out: DisableSecurityHubFeatureV2Request = {}  # type: ignore[typeddict-item]
    return out
