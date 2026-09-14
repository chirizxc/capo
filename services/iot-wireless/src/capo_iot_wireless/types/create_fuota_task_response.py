"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateFuotaTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.fuota_task_arn
    import capo_iot_wireless.types.fuota_task_id


class CreateFuotaTaskResponse(TypedDict, closed=True):
    arn: NotRequired["capo_iot_wireless.types.fuota_task_arn.FuotaTaskArn"]
    id: NotRequired["capo_iot_wireless.types.fuota_task_id.FuotaTaskId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateFuotaTaskResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateFuotaTaskResponse:
    out: CreateFuotaTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out
