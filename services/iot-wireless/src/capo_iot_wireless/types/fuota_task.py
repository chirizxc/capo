"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_arn
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.fuota_task_name


class FuotaTask(TypedDict, closed=True):
    id: NotRequired["capo_iot_wireless.types.fuota_task_id.FuotaTaskId"]
    arn: NotRequired["capo_iot_wireless.types.fuota_task_arn.FuotaTaskArn"]
    name: NotRequired["capo_iot_wireless.types.fuota_task_name.FuotaTaskName"]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTask) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> FuotaTask:
    out: FuotaTask = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
