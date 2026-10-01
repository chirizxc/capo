"""Generated from Smithy shape ``com.amazonaws.evs#Check``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_evs.types.check_result
    import capo_evs.types.check_type


class Check(TypedDict, closed=True):
    type: NotRequired["capo_evs.types.check_type.CheckType"]
    """<p>The check type. Amazon EVS performs the following checks:</p> <ul> <li> <p> <code>KEY_REUSE</code>: Verifies that the VCF license key is not used by another Amazon EVS environment.</p> </li> <li> <p> <code>KEY_COVERAGE</code>: Verifies that the VCF license key allocates sufficient vCPU cores for all deployed hosts.</p> </li> <li> <p> <code>REACHABILITY</code>: Verifies that the Amazon EVS control plane has a persistent connection to SDDC Manager.</p> </li> <li> <p> <code>HOST_COUNT</code>: Verifies that the environment meets the minimum host count.</p> </li> <li> <p> <code>VCENTER_REACHABILITY</code>: Verifies vCenter Server reachability through the vCenter connector.</p> </li> <li> <p> <code>VCENTER_VM_SYNC</code>: Verifies that the vCenter connector can synchronize VM inventory from vCenter Server.</p> </li> <li> <p> <code>VCENTER_VM_EVENT</code>: Verifies that the vCenter connector can receive VM lifecycle events from vCenter Server.</p> </li> <li> <p> <code>OPERATIONS_MANAGER_REACHABILITY</code>: Verifies Operations Manager reachability through the Operations Manager connector.</p> </li> <li> <p> <code>SDDC_MANAGER_REACHABILITY</code>: Verifies SDDC Manager reachability through the SDDC Manager connector.</p> </li> <li> <p> <code>SDDC_MANAGER_HOST_COUNT</code>: Verifies that the host count reported by SDDC Manager meets Amazon EVS minimum requirements.</p> </li> <li> <p> <code>SDDC_MANAGER_KEY_COVERAGE</code>: Verifies that the VCF license key configured in SDDC Manager covers all deployed hosts.</p> </li> <li> <p> <code>SDDC_MANAGER_KEY_REUSE</code>: Verifies that the VCF license key configured in SDDC Manager is not used by another Amazon EVS environment.</p> </li> <li> <p> <code>CONNECTOR_HEALTH</code>: Aggregate health across all connectors in the environment.</p> </li> </ul>"""
    id: NotRequired["str"]
    """<p>A unique ID for the check.</p>"""
    result: NotRequired["capo_evs.types.check_result.CheckResult"]
    """<p> The check result.</p>"""
    impaired_since: NotRequired["datetime.datetime"]
    """<p>The time when environment health began to be impaired.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Check) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_evs.types.check_type

        out["type"] = capo_evs.types.check_type.serialize_aws_json_1_0(value["type"])
    if "id" in value:
        out["id"] = value["id"]
    if "result" in value:
        import capo_evs.types.check_result

        out["result"] = capo_evs.types.check_result.serialize_aws_json_1_0(
            value["result"]
        )
    if "impaired_since" in value:
        import capo_evs.types._prelude.timestamp

        out["impairedSince"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["impaired_since"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Check:
    out: Check = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_evs.types.check_type

        out["type"] = capo_evs.types.check_type.deserialize_aws_json_1_0(data["type"])
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("result") is not None:
        import capo_evs.types.check_result

        out["result"] = capo_evs.types.check_result.deserialize_aws_json_1_0(
            data["result"]
        )
    if data.get("impairedSince") is not None:
        import capo_evs.types._prelude.timestamp

        out["impaired_since"] = (
            capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["impairedSince"]
            )
        )
    return out
