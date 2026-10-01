"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_view_segments_list_element

BillingViewSegmentsList: TypeAlias = list[
    "capo_billing.types.billing_view_segments_list_element.BillingViewSegmentsListElement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewSegmentsList) -> list:
    import capo_billing.types.billing_view_segments_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.billing_view_segments_list_element.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewSegmentsList:
    import capo_billing.types.billing_view_segments_list_element

    out: BillingViewSegmentsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.billing_view_segments_list_element.deserialize_aws_json_1_0(
                item
            )
        )
    return out
