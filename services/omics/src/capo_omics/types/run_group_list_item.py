"""Generated from Smithy shape ``com.amazonaws.omics#RunGroupListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_group_arn
    import capo_omics.types.run_group_id
    import capo_omics.types.run_group_name
    import capo_omics.types.run_group_timestamp


class RunGroupListItem(TypedDict, closed=True):
    arn: NotRequired["capo_omics.types.run_group_arn.RunGroupArn"]
    """<p>The group's ARN.</p>"""
    id: NotRequired["capo_omics.types.run_group_id.RunGroupId"]
    """<p>The group's ID.</p>"""
    name: NotRequired["capo_omics.types.run_group_name.RunGroupName"]
    """<p>The group's name.</p>"""
    max_cpus: NotRequired["int"]
    """<p>The group's maximum CPU count setting.</p>"""
    max_runs: NotRequired["int"]
    """<p>The group's maximum concurrent run setting.</p>"""
    max_duration: NotRequired["int"]
    """<p>The group's maximum duration setting in minutes.</p>"""
    creation_time: NotRequired["capo_omics.types.run_group_timestamp.RunGroupTimestamp"]
    """<p>When the group was created.</p>"""
    max_gpus: NotRequired["int"]
    """<p> The maximum GPUs that can be used by a run group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunGroupListItem) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "max_cpus" in value:
        out["maxCpus"] = value["max_cpus"]
    if "max_runs" in value:
        out["maxRuns"] = value["max_runs"]
    if "max_duration" in value:
        out["maxDuration"] = value["max_duration"]
    if "creation_time" in value:
        import capo_omics.types.run_group_timestamp

        out["creationTime"] = capo_omics.types.run_group_timestamp.serialize_json(
            value["creation_time"]
        )
    if "max_gpus" in value:
        out["maxGpus"] = value["max_gpus"]
    return out


def deserialize_json(data: dict) -> RunGroupListItem:
    out: RunGroupListItem = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("maxCpus") is not None:
        out["max_cpus"] = data["maxCpus"]
    if data.get("maxRuns") is not None:
        out["max_runs"] = data["maxRuns"]
    if data.get("maxDuration") is not None:
        out["max_duration"] = data["maxDuration"]
    if data.get("creationTime") is not None:
        import capo_omics.types.run_group_timestamp

        out["creation_time"] = capo_omics.types.run_group_timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("maxGpus") is not None:
        out["max_gpus"] = data["maxGpus"]
    return out
