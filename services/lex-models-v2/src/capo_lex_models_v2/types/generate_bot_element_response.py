"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerateBotElementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.sample_utterances_list


class GenerateBotElementResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique bot Id for the bot which received the response.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The unique bot version for the bot which received the response.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The unique locale Id for the bot which received the response.</p>"""
    intent_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique intent Id for the bot which received the response.</p>"""
    sample_utterances: NotRequired[
        "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
    ]
    """<p>The sample utterances for the bot which received the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateBotElementResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "intent_id" in value:
        out["intentId"] = value["intent_id"]
    if "sample_utterances" in value:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sampleUtterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.serialize_json(
                value["sample_utterances"]
            )
        )
    return out


def deserialize_json(data: dict) -> GenerateBotElementResponse:
    out: GenerateBotElementResponse = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("intentId") is not None:
        out["intent_id"] = data["intentId"]
    if data.get("sampleUtterances") is not None:
        import capo_lex_models_v2.types.sample_utterances_list

        out["sample_utterances"] = (
            capo_lex_models_v2.types.sample_utterances_list.deserialize_json(
                data["sampleUtterances"]
            )
        )
    return out
