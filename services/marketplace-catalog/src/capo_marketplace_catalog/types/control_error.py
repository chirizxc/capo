"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ControlError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.error_code
    import capo_marketplace_catalog.types.error_message
    import capo_marketplace_catalog.types.error_scope_list


class ControlError(TypedDict, closed=True):
    code: NotRequired["capo_marketplace_catalog.types.error_code.ErrorCode"]
    """<p>The error code that identifies the type of error.</p>"""
    message: NotRequired["capo_marketplace_catalog.types.error_message.ErrorMessage"]
    """<p>The message for the error.</p>"""
    scope: NotRequired["capo_marketplace_catalog.types.error_scope_list.ErrorScopeList"]
    """<p>The list of name-value pairs that identify the resource or attribute that the error applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "scope" in value:
        import capo_marketplace_catalog.types.error_scope_list

        out["Scope"] = capo_marketplace_catalog.types.error_scope_list.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> ControlError:
    out: ControlError = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Scope") is not None:
        import capo_marketplace_catalog.types.error_scope_list

        out["scope"] = capo_marketplace_catalog.types.error_scope_list.deserialize_json(
            data["Scope"]
        )
    return out
