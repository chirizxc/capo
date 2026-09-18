"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IssueLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class IssueLocation(TypedDict, closed=True):
    bot_locale: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale identifier where the issue was found.</p>"""
    intent_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The intent identifier where the issue was found, if applicable.</p>"""
    slot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The slot identifier where the issue was found, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueLocation) -> dict:
    out: dict = {}
    if "bot_locale" in value:
        out["botLocale"] = value["bot_locale"]
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "slot_id" in value:
        out["slotId"] = value["slot_id"]
    return out


def deserialize_json(data: dict) -> IssueLocation:
    out: IssueLocation = {}  # type: ignore[typeddict-item]
    if data.get("botLocale") is not None:
        out["bot_locale"] = data["botLocale"]
    if data.get("intentId") is not None:
        out["intent_id"] = data["intentId"]
    if data.get("slotId") is not None:
        out["slot_id"] = data["slotId"]
    return out
