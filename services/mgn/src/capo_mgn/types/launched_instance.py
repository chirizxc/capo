"""Generated from Smithy shape ``com.amazonaws.mgn#LaunchedInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.ec2_instance_id
    import capo_mgn.types.first_boot
    import capo_mgn.types.job_id
    import capo_mgn.types.last_known_check_status
    import capo_mgn.types.last_known_checks_list


class LaunchedInstance(TypedDict, closed=True):
    ec2_instance_id: NotRequired["capo_mgn.types.ec2_instance_id.EC2InstanceID"]
    """<p>Launched instance EC2 ID.</p>"""
    job_id: NotRequired["capo_mgn.types.job_id.JobID"]
    """<p>Launched instance Job ID.</p>"""
    first_boot: NotRequired["capo_mgn.types.first_boot.FirstBoot"]
    """<p>Launched instance first boot.</p>"""
    last_known_checks: NotRequired[
        "capo_mgn.types.last_known_checks_list.LastKnownChecksList"
    ]
    """<p>Launched instance last known checks.</p>"""
    last_known_fsx_checks_status: NotRequired[
        "capo_mgn.types.last_known_check_status.LastKnownCheckStatus"
    ]
    """<p>Launched instance last known FSx checks status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchedInstance) -> dict:
    out: dict = {}
    if "ec2_instance_id" in value:
        out["ec2InstanceID"] = value["ec2_instance_id"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "first_boot" in value:
        out["firstBoot"] = value["first_boot"]
    if "last_known_checks" in value:
        import capo_mgn.types.last_known_checks_list

        out["lastKnownChecks"] = capo_mgn.types.last_known_checks_list.serialize_json(
            value["last_known_checks"]
        )
    if "last_known_fsx_checks_status" in value:
        out["lastKnownFsxChecksStatus"] = value["last_known_fsx_checks_status"]
    return out


def deserialize_json(data: dict) -> LaunchedInstance:
    out: LaunchedInstance = {}  # type: ignore[typeddict-item]
    if data.get("ec2InstanceID") is not None:
        out["ec2_instance_id"] = data["ec2InstanceID"]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    if data.get("firstBoot") is not None:
        out["first_boot"] = data["firstBoot"]
    if data.get("lastKnownChecks") is not None:
        import capo_mgn.types.last_known_checks_list

        out["last_known_checks"] = (
            capo_mgn.types.last_known_checks_list.deserialize_json(
                data["lastKnownChecks"]
            )
        )
    if data.get("lastKnownFsxChecksStatus") is not None:
        out["last_known_fsx_checks_status"] = data["lastKnownFsxChecksStatus"]
    return out
