"""Generated from Smithy shape ``com.amazonaws.quicksight#AppSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.app_id
    import capo_quicksight.types.app_name
    import capo_quicksight.types.app_visibility
    import capo_quicksight.types.timestamp


class AppSummary(TypedDict, closed=True):
    app_id: NotRequired["capo_quicksight.types.app_id.AppId"]
    """<p>The ID of the app.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the app.</p>"""
    name: NotRequired["capo_quicksight.types.app_name.AppName"]
    """<p>The display name of the app.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the app was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the app was last updated.</p>"""
    visibility: NotRequired["capo_quicksight.types.app_visibility.AppVisibility"]
    """<p>The sharing status of the app: <code>PUBLIC</code> if the app is shared publicly, or <code>PRIVATE</code> if it is private.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppSummary) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["AppId"] = value["app_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "visibility" in value:
        import capo_quicksight.types.app_visibility

        out["Visibility"] = capo_quicksight.types.app_visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> AppSummary:
    out: AppSummary = {}  # type: ignore[typeddict-item]
    if data.get("AppId") is not None:
        out["app_id"] = data["AppId"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("Visibility") is not None:
        import capo_quicksight.types.app_visibility

        out["visibility"] = capo_quicksight.types.app_visibility.deserialize_json(
            data["Visibility"]
        )
    return out
