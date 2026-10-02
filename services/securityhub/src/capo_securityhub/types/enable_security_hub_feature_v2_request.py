"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableSecurityHubFeatureV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.feature_name


class EnableSecurityHubFeatureV2Request(TypedDict, closed=True):
    feature_name: "capo_securityhub.types.feature_name.FeatureName"
    """<p>The name of the feature to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSecurityHubFeatureV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EnableSecurityHubFeatureV2Request:
    out: EnableSecurityHubFeatureV2Request = {}  # type: ignore[typeddict-item]
    return out
