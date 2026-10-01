"""Generated from Smithy shape ``com.amazonaws.evs#CheckType``."""

from typing import Literal, TypeAlias, cast

CheckType: TypeAlias = Literal[
    "KEY_REUSE",
    "KEY_COVERAGE",
    "REACHABILITY",
    "HOST_COUNT",
    "VCENTER_REACHABILITY",
    "VCENTER_VM_SYNC",
    "VCENTER_VM_EVENT",
    "OPERATIONS_MANAGER_REACHABILITY",
    "SDDC_MANAGER_REACHABILITY",
    "SDDC_MANAGER_HOST_COUNT",
    "SDDC_MANAGER_KEY_COVERAGE",
    "SDDC_MANAGER_KEY_REUSE",
    "CONNECTOR_HEALTH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CheckType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CheckType:
    return cast(CheckType, data)
