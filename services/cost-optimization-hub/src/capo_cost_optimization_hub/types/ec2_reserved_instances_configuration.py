"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2ReservedInstancesConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class Ec2ReservedInstancesConfiguration(TypedDict, closed=True):
    account_scope: NotRequired["str"]
    """<p>The account scope for which you want recommendations.</p>"""
    service: NotRequired["str"]
    """<p>The service for which you want recommendations.</p>"""
    term: NotRequired["str"]
    """<p>The reserved instances recommendation term in years.</p>"""
    payment_option: NotRequired["str"]
    """<p>The payment option for the commitment.</p>"""
    reserved_instances_region: NotRequired["str"]
    """<p>The Amazon Web Services Region of the commitment.</p>"""
    upfront_cost: NotRequired["str"]
    """<p>How much purchasing this instance costs you upfront.</p>"""
    monthly_recurring_cost: NotRequired["str"]
    """<p>How much purchasing these reserved instances costs you on a monthly basis.</p>"""
    normalized_units_to_purchase: NotRequired["str"]
    """<p>The number of normalized units that Amazon Web Services recommends that you purchase.</p>"""
    number_of_instances_to_purchase: NotRequired["str"]
    """<p>The number of instances that Amazon Web Services recommends that you purchase.</p>"""
    offering_class: NotRequired["str"]
    """<p>Indicates whether the recommendation is for standard or convertible reservations.</p>"""
    instance_family: NotRequired["str"]
    """<p>The instance family of the recommended reservation.</p>"""
    instance_type: NotRequired["str"]
    """<p>The type of instance that Amazon Web Services recommends.</p>"""
    current_generation: NotRequired["str"]
    """<p>Determines whether the recommendation is for a current generation instance.</p>"""
    platform: NotRequired["str"]
    """<p>The platform of the recommended reservation. The platform is the specific combination of operating system, license model, and software on an instance.</p>"""
    tenancy: NotRequired["str"]
    """<p>Determines whether the recommended reservation is dedicated or shared.</p>"""
    size_flex_eligible: NotRequired["bool"]
    """<p>Determines whether the recommendation is size flexible.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2ReservedInstancesConfiguration) -> dict:
    out: dict = {}
    if "account_scope" in value:
        out["accountScope"] = value["account_scope"]
    if "service" in value:
        out["service"] = value["service"]
    if "term" in value:
        out["term"] = value["term"]
    if "payment_option" in value:
        out["paymentOption"] = value["payment_option"]
    if "reserved_instances_region" in value:
        out["reservedInstancesRegion"] = value["reserved_instances_region"]
    if "upfront_cost" in value:
        out["upfrontCost"] = value["upfront_cost"]
    if "monthly_recurring_cost" in value:
        out["monthlyRecurringCost"] = value["monthly_recurring_cost"]
    if "normalized_units_to_purchase" in value:
        out["normalizedUnitsToPurchase"] = value["normalized_units_to_purchase"]
    if "number_of_instances_to_purchase" in value:
        out["numberOfInstancesToPurchase"] = value["number_of_instances_to_purchase"]
    if "offering_class" in value:
        out["offeringClass"] = value["offering_class"]
    if "instance_family" in value:
        out["instanceFamily"] = value["instance_family"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "current_generation" in value:
        out["currentGeneration"] = value["current_generation"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "tenancy" in value:
        out["tenancy"] = value["tenancy"]
    if "size_flex_eligible" in value:
        out["sizeFlexEligible"] = value["size_flex_eligible"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2ReservedInstancesConfiguration:
    out: Ec2ReservedInstancesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountScope") is not None:
        out["account_scope"] = data["accountScope"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("term") is not None:
        out["term"] = data["term"]
    if data.get("paymentOption") is not None:
        out["payment_option"] = data["paymentOption"]
    if data.get("reservedInstancesRegion") is not None:
        out["reserved_instances_region"] = data["reservedInstancesRegion"]
    if data.get("upfrontCost") is not None:
        out["upfront_cost"] = data["upfrontCost"]
    if data.get("monthlyRecurringCost") is not None:
        out["monthly_recurring_cost"] = data["monthlyRecurringCost"]
    if data.get("normalizedUnitsToPurchase") is not None:
        out["normalized_units_to_purchase"] = data["normalizedUnitsToPurchase"]
    if data.get("numberOfInstancesToPurchase") is not None:
        out["number_of_instances_to_purchase"] = data["numberOfInstancesToPurchase"]
    if data.get("offeringClass") is not None:
        out["offering_class"] = data["offeringClass"]
    if data.get("instanceFamily") is not None:
        out["instance_family"] = data["instanceFamily"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("currentGeneration") is not None:
        out["current_generation"] = data["currentGeneration"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("tenancy") is not None:
        out["tenancy"] = data["tenancy"]
    if data.get("sizeFlexEligible") is not None:
        out["size_flex_eligible"] = data["sizeFlexEligible"]
    return out
