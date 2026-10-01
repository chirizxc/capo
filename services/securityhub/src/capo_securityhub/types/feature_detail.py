"""Generated from Smithy shape ``com.amazonaws.securityhub#FeatureDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.feature_status
    import capo_securityhub.types.timestamp


class FeatureDetail(TypedDict, closed=True):
    feature_status: NotRequired["capo_securityhub.types.feature_status.FeatureStatus"]
    """<p>The current enablement status of the feature. Valid values: <code>ENABLED</code> | <code>DISABLED</code>.</p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The date and time when the feature status was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FeatureDetail) -> dict:
    out: dict = {}
    if "feature_status" in value:
        import capo_securityhub.types.feature_status

        out["FeatureStatus"] = capo_securityhub.types.feature_status.serialize_json(
            value["feature_status"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> FeatureDetail:
    out: FeatureDetail = {}  # type: ignore[typeddict-item]
    if data.get("FeatureStatus") is not None:
        import capo_securityhub.types.feature_status

        out["feature_status"] = capo_securityhub.types.feature_status.deserialize_json(
            data["FeatureStatus"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
