"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PostFulfillmentStatusSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conditional_specification
    import capo_lex_models_v2.types.dialog_state
    import capo_lex_models_v2.types.response_specification


class PostFulfillmentStatusSpecification(TypedDict, closed=True):
    success_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    failure_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    timeout_response: NotRequired[
        "capo_lex_models_v2.types.response_specification.ResponseSpecification"
    ]
    success_next_step: NotRequired["capo_lex_models_v2.types.dialog_state.DialogState"]
    """<p>Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.</p>"""
    success_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.</p>"""
    failure_next_step: NotRequired["capo_lex_models_v2.types.dialog_state.DialogState"]
    """<p>Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the <code>State</code> field of the <code>Intent</code> object set to <code>Failed</code>.</p>"""
    failure_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the <code>State</code> field of the <code>Intent</code> object set to <code>Failed</code>.</p>"""
    timeout_next_step: NotRequired["capo_lex_models_v2.types.dialog_state.DialogState"]
    """<p>Specifies the next step that the bot runs when the fulfillment code hook times out.</p>"""
    timeout_conditional: NotRequired[
        "capo_lex_models_v2.types.conditional_specification.ConditionalSpecification"
    ]
    """<p>A list of conditional branches to evaluate if the fulfillment code hook times out.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostFulfillmentStatusSpecification) -> dict:
    out: dict = {}
    if "success_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["successResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["success_response"]
            )
        )
    if "failure_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["failureResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["failure_response"]
            )
        )
    if "timeout_response" in value:
        import capo_lex_models_v2.types.response_specification

        out["timeoutResponse"] = (
            capo_lex_models_v2.types.response_specification.serialize_json(
                value["timeout_response"]
            )
        )
    if "success_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["successNextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
            value["success_next_step"]
        )
    if "success_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["successConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["success_conditional"]
            )
        )
    if "failure_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["failureNextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
            value["failure_next_step"]
        )
    if "failure_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["failureConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["failure_conditional"]
            )
        )
    if "timeout_next_step" in value:
        import capo_lex_models_v2.types.dialog_state

        out["timeoutNextStep"] = capo_lex_models_v2.types.dialog_state.serialize_json(
            value["timeout_next_step"]
        )
    if "timeout_conditional" in value:
        import capo_lex_models_v2.types.conditional_specification

        out["timeoutConditional"] = (
            capo_lex_models_v2.types.conditional_specification.serialize_json(
                value["timeout_conditional"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostFulfillmentStatusSpecification:
    out: PostFulfillmentStatusSpecification = {}  # type: ignore[typeddict-item]
    if data.get("successResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["success_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["successResponse"]
            )
        )
    if data.get("failureResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["failure_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["failureResponse"]
            )
        )
    if data.get("timeoutResponse") is not None:
        import capo_lex_models_v2.types.response_specification

        out["timeout_response"] = (
            capo_lex_models_v2.types.response_specification.deserialize_json(
                data["timeoutResponse"]
            )
        )
    if data.get("successNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["success_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["successNextStep"]
            )
        )
    if data.get("successConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["success_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["successConditional"]
            )
        )
    if data.get("failureNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["failure_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["failureNextStep"]
            )
        )
    if data.get("failureConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["failure_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["failureConditional"]
            )
        )
    if data.get("timeoutNextStep") is not None:
        import capo_lex_models_v2.types.dialog_state

        out["timeout_next_step"] = (
            capo_lex_models_v2.types.dialog_state.deserialize_json(
                data["timeoutNextStep"]
            )
        )
    if data.get("timeoutConditional") is not None:
        import capo_lex_models_v2.types.conditional_specification

        out["timeout_conditional"] = (
            capo_lex_models_v2.types.conditional_specification.deserialize_json(
                data["timeoutConditional"]
            )
        )
    return out
