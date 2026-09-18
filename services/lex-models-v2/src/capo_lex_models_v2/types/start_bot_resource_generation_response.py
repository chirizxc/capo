"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartBotResourceGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.generation_input
    import capo_lex_models_v2.types.generation_status
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.timestamp


class StartBotResourceGenerationResponse(TypedDict, closed=True):
    generation_input_prompt: NotRequired[
        "capo_lex_models_v2.types.generation_input.GenerationInput"
    ]
    """<p>The prompt that was used generate intents and slot types for the bot locale.</p>"""
    generation_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the generation request.</p>"""
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot for which the generation request was made.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot for which the generation request was made.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale of the bot for which the generation request was made.</p>"""
    generation_status: NotRequired[
        "capo_lex_models_v2.types.generation_status.GenerationStatus"
    ]
    """<p>The status of the generation request.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the generation request was made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartBotResourceGenerationResponse) -> dict:
    out: dict = {}
    if "generation_input_prompt" in value:
        out["generationInputPrompt"] = value["generation_input_prompt"]
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "generation_status" in value:
        import capo_lex_models_v2.types.generation_status

        out["generationStatus"] = (
            capo_lex_models_v2.types.generation_status.serialize_json(
                value["generation_status"]
            )
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    return out


def deserialize_json(data: dict) -> StartBotResourceGenerationResponse:
    out: StartBotResourceGenerationResponse = {}  # type: ignore[typeddict-item]
    if data.get("generationInputPrompt") is not None:
        out["generation_input_prompt"] = data["generationInputPrompt"]
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("generationStatus") is not None:
        import capo_lex_models_v2.types.generation_status

        out["generation_status"] = (
            capo_lex_models_v2.types.generation_status.deserialize_json(
                data["generationStatus"]
            )
        )
    if data.get("creationDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    return out
