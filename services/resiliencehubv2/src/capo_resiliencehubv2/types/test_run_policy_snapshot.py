"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TestRunPolicySnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.data_recovery_targets
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.multi_az_targets
    import capo_resiliencehubv2.types.multi_region_targets


class TestRunPolicySnapshot(TypedDict, closed=True):
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The ARN of the policy.</p>"""
    name: NotRequired["capo_resiliencehubv2.types.entity_name.EntityName"]
    """<p>The name of the policy.</p>"""
    availability_slo: NotRequired[
        "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO targets.</p>"""
    multi_az: NotRequired["capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"]
    """<p>The multi-AZ resilience targets.</p>"""
    multi_region: NotRequired[
        "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The multi-Region resilience targets.</p>"""
    data_recovery: NotRequired[
        "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
    ]
    """<p>The data recovery targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestRunPolicySnapshot) -> dict:
    out: dict = {}
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "availability_slo" in value:
        import capo_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            capo_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az" in value:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multiAz"] = capo_resiliencehubv2.types.multi_az_targets.serialize_json(
            value["multi_az"]
        )
    if "multi_region" in value:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multiRegion"] = (
            capo_resiliencehubv2.types.multi_region_targets.serialize_json(
                value["multi_region"]
            )
        )
    if "data_recovery" in value:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["dataRecovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.serialize_json(
                value["data_recovery"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestRunPolicySnapshot:
    out: TestRunPolicySnapshot = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("availabilitySlo") is not None:
        import capo_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            capo_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if data.get("multiAz") is not None:
        import capo_resiliencehubv2.types.multi_az_targets

        out["multi_az"] = capo_resiliencehubv2.types.multi_az_targets.deserialize_json(
            data["multiAz"]
        )
    if data.get("multiRegion") is not None:
        import capo_resiliencehubv2.types.multi_region_targets

        out["multi_region"] = (
            capo_resiliencehubv2.types.multi_region_targets.deserialize_json(
                data["multiRegion"]
            )
        )
    if data.get("dataRecovery") is not None:
        import capo_resiliencehubv2.types.data_recovery_targets

        out["data_recovery"] = (
            capo_resiliencehubv2.types.data_recovery_targets.deserialize_json(
                data["dataRecovery"]
            )
        )
    return out
