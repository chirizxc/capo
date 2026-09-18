"""Generated from Smithy shape ``com.amazonaws.securityhub#ImportFindingsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ImportFindingsError(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the finding that could not be updated.</p>"""
    error_code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The code of the error returned by the <code>BatchImportFindings</code> operation.</p>"""
    error_message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The message of the error returned by the <code>BatchImportFindings</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportFindingsError) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ImportFindingsError:
    out: ImportFindingsError = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
