"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ConsumableDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.issuance_detail
    import capo_partnercentral_benefits.types.monetary_value


class ConsumableDetails(TypedDict, closed=True):
    allocated_amount: NotRequired[
        "capo_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The total amount of the consumable benefit that has been allocated.</p>"""
    remaining_amount: NotRequired[
        "capo_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The remaining amount of the consumable benefit that is still available for use.</p>"""
    utilized_amount: NotRequired[
        "capo_partnercentral_benefits.types.monetary_value.MonetaryValue"
    ]
    """<p>The amount of the consumable benefit that has already been used.</p>"""
    issuance_details: NotRequired[
        "capo_partnercentral_benefits.types.issuance_detail.IssuanceDetail"
    ]
    """<p>Detailed information about how the consumable benefit was issued and distributed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConsumableDetails) -> dict:
    out: dict = {}
    if "allocated_amount" in value:
        import capo_partnercentral_benefits.types.monetary_value

        out["AllocatedAmount"] = (
            capo_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["allocated_amount"]
            )
        )
    if "remaining_amount" in value:
        import capo_partnercentral_benefits.types.monetary_value

        out["RemainingAmount"] = (
            capo_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["remaining_amount"]
            )
        )
    if "utilized_amount" in value:
        import capo_partnercentral_benefits.types.monetary_value

        out["UtilizedAmount"] = (
            capo_partnercentral_benefits.types.monetary_value.serialize_aws_json_1_0(
                value["utilized_amount"]
            )
        )
    if "issuance_details" in value:
        import capo_partnercentral_benefits.types.issuance_detail

        out["IssuanceDetails"] = (
            capo_partnercentral_benefits.types.issuance_detail.serialize_aws_json_1_0(
                value["issuance_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConsumableDetails:
    out: ConsumableDetails = {}  # type: ignore[typeddict-item]
    if data.get("AllocatedAmount") is not None:
        import capo_partnercentral_benefits.types.monetary_value

        out["allocated_amount"] = (
            capo_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["AllocatedAmount"]
            )
        )
    if data.get("RemainingAmount") is not None:
        import capo_partnercentral_benefits.types.monetary_value

        out["remaining_amount"] = (
            capo_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["RemainingAmount"]
            )
        )
    if data.get("UtilizedAmount") is not None:
        import capo_partnercentral_benefits.types.monetary_value

        out["utilized_amount"] = (
            capo_partnercentral_benefits.types.monetary_value.deserialize_aws_json_1_0(
                data["UtilizedAmount"]
            )
        )
    if data.get("IssuanceDetails") is not None:
        import capo_partnercentral_benefits.types.issuance_detail

        out["issuance_details"] = (
            capo_partnercentral_benefits.types.issuance_detail.deserialize_aws_json_1_0(
                data["IssuanceDetails"]
            )
        )
    return out
