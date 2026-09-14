"""Generated from Smithy shape ``com.amazonaws.guardduty#ProcessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.lineage
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class ProcessDetails(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the process.</p>"""
    executable_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The absolute path of the process executable file.</p>"""
    executable_sha256: NotRequired["capo_guardduty.types.string.String"]
    """<p>The <code>SHA256</code> hash of the process executable.</p>"""
    namespace_pid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The ID of the child process.</p>"""
    pwd: NotRequired["capo_guardduty.types.string.String"]
    """<p>The present working directory of the process.</p>"""
    pid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The ID of the process.</p>"""
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The time when the process started. This is in UTC format.</p>"""
    uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID assigned to the process by GuardDuty.</p>"""
    parent_uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.</p>"""
    user: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user that executed the process.</p>"""
    user_id: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The unique ID of the user that executed the process.</p>"""
    euid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The effective user ID of the user that executed the process.</p>"""
    lineage: NotRequired["capo_guardduty.types.lineage.Lineage"]
    """<p>Information about the process's lineage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "executable_path" in value:
        out["executablePath"] = value["executable_path"]
    if "executable_sha256" in value:
        out["executableSha256"] = value["executable_sha256"]
    if "namespace_pid" in value:
        out["namespacePid"] = value["namespace_pid"]
    if "pwd" in value:
        out["pwd"] = value["pwd"]
    if "pid" in value:
        out["pid"] = value["pid"]
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "parent_uuid" in value:
        out["parentUuid"] = value["parent_uuid"]
    if "user" in value:
        out["user"] = value["user"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "euid" in value:
        out["euid"] = value["euid"]
    if "lineage" in value:
        import capo_guardduty.types.lineage

        out["lineage"] = capo_guardduty.types.lineage.serialize_json(value["lineage"])
    return out


def deserialize_json(data: dict) -> ProcessDetails:
    out: ProcessDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("executablePath") is not None:
        out["executable_path"] = data["executablePath"]
    if data.get("executableSha256") is not None:
        out["executable_sha256"] = data["executableSha256"]
    if data.get("namespacePid") is not None:
        out["namespace_pid"] = data["namespacePid"]
    if data.get("pwd") is not None:
        out["pwd"] = data["pwd"]
    if data.get("pid") is not None:
        out["pid"] = data["pid"]
    if data.get("startTime") is not None:
        import capo_guardduty.types.timestamp

        out["start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    if data.get("parentUuid") is not None:
        out["parent_uuid"] = data["parentUuid"]
    if data.get("user") is not None:
        out["user"] = data["user"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("euid") is not None:
        out["euid"] = data["euid"]
    if data.get("lineage") is not None:
        import capo_guardduty.types.lineage

        out["lineage"] = capo_guardduty.types.lineage.deserialize_json(data["lineage"])
    return out
