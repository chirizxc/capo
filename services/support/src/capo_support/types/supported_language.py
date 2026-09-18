"""Generated from Smithy shape ``com.amazonaws.support#SupportedLanguage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.code
    import capo_support.types.display
    import capo_support.types.language


class SupportedLanguage(TypedDict, closed=True):
    code: NotRequired["capo_support.types.code.Code"]
    """<p> 2 digit ISO 639-1 code. e.g. <code>en</code> </p>"""
    language: NotRequired["capo_support.types.language.Language"]
    """<p> Full language description e.g. <code>ENGLISH</code> </p>"""
    display: NotRequired["capo_support.types.display.Display"]
    """<p> Language display value e.g. <code>ENGLISH</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedLanguage) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "language" in value:
        out["language"] = value["language"]
    if "display" in value:
        out["display"] = value["display"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedLanguage:
    out: SupportedLanguage = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("language") is not None:
        out["language"] = data["language"]
    if data.get("display") is not None:
        out["display"] = data["display"]
    return out
