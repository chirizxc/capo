"""Generated from Smithy shape ``com.amazonaws.billing#BillingFeatureFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_feature_filter_name
    import capo_billing.types.billing_feature_filter_values


class BillingFeatureFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_billing.types.billing_feature_filter_name.BillingFeatureFilterName"
    ]
    """<p>The filter name. Currently the only supported value is <code>PREFERENCE_KEY</code>.</p>"""
    value: NotRequired[
        "capo_billing.types.billing_feature_filter_values.BillingFeatureFilterValues"
    ]
    """<p>The filter values to match. For <code>PREFERENCE_KEY</code>, supply 1 to 10 preference key values to match.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingFeatureFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_billing.types.billing_feature_filter_name

        out["name"] = (
            capo_billing.types.billing_feature_filter_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "value" in value:
        import capo_billing.types.billing_feature_filter_values

        out["value"] = (
            capo_billing.types.billing_feature_filter_values.serialize_aws_json_1_0(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingFeatureFilter:
    out: BillingFeatureFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_billing.types.billing_feature_filter_name

        out["name"] = (
            capo_billing.types.billing_feature_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("value") is not None:
        import capo_billing.types.billing_feature_filter_values

        out["value"] = (
            capo_billing.types.billing_feature_filter_values.deserialize_aws_json_1_0(
                data["value"]
            )
        )
    return out
