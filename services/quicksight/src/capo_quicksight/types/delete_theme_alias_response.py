"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteThemeAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.alias_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DeleteThemeAliasResponse(TypedDict, closed=True):
    alias_name: NotRequired["capo_quicksight.types.alias_name.AliasName"]
    """<p>The name for the theme alias.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme resource using the deleted alias.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    theme_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>An ID for the theme associated with the deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteThemeAliasResponse) -> dict:
    out: dict = {}
    if "alias_name" in value:
        out["AliasName"] = value["alias_name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    return out


def deserialize_json(data: dict) -> DeleteThemeAliasResponse:
    out: DeleteThemeAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("ThemeId") is not None:
        out["theme_id"] = data["ThemeId"]
    return out
