"""Generated from Smithy shape ``com.amazonaws.quicksight#GoogleDriveParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.auth_type


class GoogleDriveParameters(TypedDict, closed=True):
    auth_type: NotRequired["capo_quicksight.types.auth_type.AuthType"]
    """<p>The authentication type for the Google Drive data source. Valid values include:</p> <ul> <li> <p> <code>SERVICE_ACCOUNT</code> – Server-to-server authentication using a Google service account key.</p> </li> <li> <p> <code>THREE_LEGGED_OAUTH</code> – Interactive OAuth that requires user consent.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoogleDriveParameters) -> dict:
    out: dict = {}
    if "auth_type" in value:
        import capo_quicksight.types.auth_type

        out["AuthType"] = capo_quicksight.types.auth_type.serialize_json(
            value["auth_type"]
        )
    return out


def deserialize_json(data: dict) -> GoogleDriveParameters:
    out: GoogleDriveParameters = {}  # type: ignore[typeddict-item]
    if data.get("AuthType") is not None:
        import capo_quicksight.types.auth_type

        out["auth_type"] = capo_quicksight.types.auth_type.deserialize_json(
            data["AuthType"]
        )
    return out
