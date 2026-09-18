"""Generated from Smithy shape ``com.amazonaws.guardduty#LineageObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class LineageObject(TypedDict, closed=True):
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The time when the process started. This is in UTC format.</p>"""
    namespace_pid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The process ID of the child process.</p>"""
    user_id: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The user ID of the user that executed the process.</p>"""
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the process.</p>"""
    pid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The ID of the process.</p>"""
    uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID assigned to the process by GuardDuty.</p>"""
    executable_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The absolute path of the process executable file.</p>"""
    euid: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The effective user ID that was used to execute the process.</p>"""
    parent_uuid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID of the parent process. This ID is assigned to the parent process by GuardDuty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageObject) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "namespace_pid" in value:
        out["namespacePid"] = value["namespace_pid"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "pid" in value:
        out["pid"] = value["pid"]
    if "uuid" in value:
        out["uuid"] = value["uuid"]
    if "executable_path" in value:
        out["executablePath"] = value["executable_path"]
    if "euid" in value:
        out["euid"] = value["euid"]
    if "parent_uuid" in value:
        out["parentUuid"] = value["parent_uuid"]
    return out


def deserialize_json(data: dict) -> LineageObject:
    out: LineageObject = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_guardduty.types.timestamp

        out["start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("namespacePid") is not None:
        out["namespace_pid"] = data["namespacePid"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("pid") is not None:
        out["pid"] = data["pid"]
    if data.get("uuid") is not None:
        out["uuid"] = data["uuid"]
    if data.get("executablePath") is not None:
        out["executable_path"] = data["executablePath"]
    if data.get("euid") is not None:
        out["euid"] = data["euid"]
    if data.get("parentUuid") is not None:
        out["parent_uuid"] = data["parentUuid"]
    return out
