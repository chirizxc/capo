"""Generated from Smithy shape ``com.amazonaws.connect#LanguageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.language_locale


class LanguageConfiguration(TypedDict, closed=True):
    language_locale: NotRequired["capo_connect.types.language_locale.LanguageLocale"]
    """<p>The language locale setting for conversational analytics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LanguageConfiguration) -> dict:
    out: dict = {}
    if "language_locale" in value:
        out["LanguageLocale"] = value["language_locale"]
    return out


def deserialize_json(data: dict) -> LanguageConfiguration:
    out: LanguageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("LanguageLocale") is not None:
        out["language_locale"] = data["LanguageLocale"]
    return out
