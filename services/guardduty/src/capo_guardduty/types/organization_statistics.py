"""Generated from Smithy shape ``com.amazonaws.guardduty#OrganizationStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.organization_feature_statistics_results


class OrganizationStatistics(TypedDict, closed=True):
    total_accounts_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of accounts in your Amazon Web Services organization.</p>"""
    member_accounts_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of accounts in your Amazon Web Services organization that are associated with GuardDuty.</p>"""
    active_accounts_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of active accounts in your Amazon Web Services organization that are associated with GuardDuty.</p>"""
    enabled_accounts_count: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of accounts that have enabled GuardDuty.</p>"""
    count_by_feature: NotRequired[
        "capo_guardduty.types.organization_feature_statistics_results.OrganizationFeatureStatisticsResults"
    ]
    """<p>Retrieves the coverage statistics for each feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationStatistics) -> dict:
    out: dict = {}
    if "total_accounts_count" in value:
        out["totalAccountsCount"] = value["total_accounts_count"]
    if "member_accounts_count" in value:
        out["memberAccountsCount"] = value["member_accounts_count"]
    if "active_accounts_count" in value:
        out["activeAccountsCount"] = value["active_accounts_count"]
    if "enabled_accounts_count" in value:
        out["enabledAccountsCount"] = value["enabled_accounts_count"]
    if "count_by_feature" in value:
        import capo_guardduty.types.organization_feature_statistics_results

        out["countByFeature"] = (
            capo_guardduty.types.organization_feature_statistics_results.serialize_json(
                value["count_by_feature"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrganizationStatistics:
    out: OrganizationStatistics = {}  # type: ignore[typeddict-item]
    if data.get("totalAccountsCount") is not None:
        out["total_accounts_count"] = data["totalAccountsCount"]
    if data.get("memberAccountsCount") is not None:
        out["member_accounts_count"] = data["memberAccountsCount"]
    if data.get("activeAccountsCount") is not None:
        out["active_accounts_count"] = data["activeAccountsCount"]
    if data.get("enabledAccountsCount") is not None:
        out["enabled_accounts_count"] = data["enabledAccountsCount"]
    if data.get("countByFeature") is not None:
        import capo_guardduty.types.organization_feature_statistics_results

        out["count_by_feature"] = (
            capo_guardduty.types.organization_feature_statistics_results.deserialize_json(
                data["countByFeature"]
            )
        )
    return out
