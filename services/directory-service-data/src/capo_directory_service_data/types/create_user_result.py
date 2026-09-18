"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#CreateUserResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_id
    import capo_directory_service_data.types.sid
    import capo_directory_service_data.types.user_name


class CreateUserResult(TypedDict, closed=True):
    directory_id: NotRequired[
        "capo_directory_service_data.types.directory_id.DirectoryId"
    ]
    """<p> The identifier (ID) of the directory where the address block is added. </p>"""
    sid: NotRequired["capo_directory_service_data.types.sid.SID"]
    """<p> The unique security identifier (SID) of the user. </p>"""
    sam_account_name: NotRequired[
        "capo_directory_service_data.types.user_name.UserName"
    ]
    """<p> The name of the user. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "sid" in value:
        out["SID"] = value["sid"]
    if "sam_account_name" in value:
        out["SAMAccountName"] = value["sam_account_name"]
    return out


def deserialize_json(data: dict) -> CreateUserResult:
    out: CreateUserResult = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("SAMAccountName") is not None:
        out["sam_account_name"] = data["SAMAccountName"]
    return out
