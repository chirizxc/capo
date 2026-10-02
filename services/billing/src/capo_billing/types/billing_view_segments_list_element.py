"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewSegmentsListElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.billing_domain
    import capo_billing.types.billing_view_segment_time_range


class BillingViewSegmentsListElement(TypedDict, closed=True):
    domain: NotRequired["capo_billing.types.billing_domain.BillingDomain"]
    """<p>The billing domain for this segment. The following values are valid:</p> <ul> <li> <p> <code>PRO_FORMA</code> - Data shaped by Billing Conductor that doesn't reflect the final charges owed to Amazon Web Services.</p> </li> <li> <p> <code>BILLABLE</code> - Data that represents the final charges owed to Amazon Web Services.</p> </li> </ul>"""
    time_range: NotRequired[
        "capo_billing.types.billing_view_segment_time_range.BillingViewSegmentTimeRange"
    ]
    """<p> The time range during which this segment is effective. </p>"""
    billing_transfer_account_id: NotRequired["capo_billing.types.account_id.AccountId"]
    """<p> The billing transfer account ID. The response includes this field only when the caller is a billing transfer source account. The response omits this field for billing group billing views. </p>"""
    management_account_id: NotRequired["capo_billing.types.account_id.AccountId"]
    """<p> The management account ID of the organization. The response includes this field for organization member accounts. </p>"""
    billing_group_primary_account_id: NotRequired[
        "capo_billing.types.account_id.AccountId"
    ]
    """<p> The billing group primary account ID. The response includes this field for billing group members. Compare this value to your own account ID to determine whether you are the primary account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewSegmentsListElement) -> dict:
    out: dict = {}
    if "domain" in value:
        import capo_billing.types.billing_domain

        out["domain"] = capo_billing.types.billing_domain.serialize_aws_json_1_0(
            value["domain"]
        )
    if "time_range" in value:
        import capo_billing.types.billing_view_segment_time_range

        out["timeRange"] = (
            capo_billing.types.billing_view_segment_time_range.serialize_aws_json_1_0(
                value["time_range"]
            )
        )
    if "billing_transfer_account_id" in value:
        out["billingTransferAccountId"] = value["billing_transfer_account_id"]
    if "management_account_id" in value:
        out["managementAccountId"] = value["management_account_id"]
    if "billing_group_primary_account_id" in value:
        out["billingGroupPrimaryAccountId"] = value["billing_group_primary_account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewSegmentsListElement:
    out: BillingViewSegmentsListElement = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        import capo_billing.types.billing_domain

        out["domain"] = capo_billing.types.billing_domain.deserialize_aws_json_1_0(
            data["domain"]
        )
    if data.get("timeRange") is not None:
        import capo_billing.types.billing_view_segment_time_range

        out["time_range"] = (
            capo_billing.types.billing_view_segment_time_range.deserialize_aws_json_1_0(
                data["timeRange"]
            )
        )
    if data.get("billingTransferAccountId") is not None:
        out["billing_transfer_account_id"] = data["billingTransferAccountId"]
    if data.get("managementAccountId") is not None:
        out["management_account_id"] = data["managementAccountId"]
    if data.get("billingGroupPrimaryAccountId") is not None:
        out["billing_group_primary_account_id"] = data["billingGroupPrimaryAccountId"]
    return out
