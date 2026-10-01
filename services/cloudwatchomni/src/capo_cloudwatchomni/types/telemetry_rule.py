"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#TelemetryRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_condition
    import capo_cloudwatchomni.types.alert_evaluation
    import capo_cloudwatchomni.types.alert_rule_query
    import capo_cloudwatchomni.types.no_data


class TelemetryRule(TypedDict, closed=True):
    query: NotRequired["capo_cloudwatchomni.types.alert_rule_query.AlertRuleQuery"]
    """The query expression to evaluate."""
    condition: NotRequired["capo_cloudwatchomni.types.alert_condition.AlertCondition"]
    """The condition that determines when the alert fires."""
    evaluation: NotRequired[
        "capo_cloudwatchomni.types.alert_evaluation.AlertEvaluation"
    ]
    """The evaluation cadence and durations."""
    no_data: NotRequired["capo_cloudwatchomni.types.no_data.NoData"]
    """How the alert behaves when a query produces no data."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TelemetryRule) -> dict:
    out: dict = {}
    if "query" in value:
        import capo_cloudwatchomni.types.alert_rule_query

        out["query"] = capo_cloudwatchomni.types.alert_rule_query.serialize_cbor(
            value["query"]
        )
    if "condition" in value:
        import capo_cloudwatchomni.types.alert_condition

        out["condition"] = capo_cloudwatchomni.types.alert_condition.serialize_cbor(
            value["condition"]
        )
    if "evaluation" in value:
        import capo_cloudwatchomni.types.alert_evaluation

        out["evaluation"] = capo_cloudwatchomni.types.alert_evaluation.serialize_cbor(
            value["evaluation"]
        )
    if "no_data" in value:
        import capo_cloudwatchomni.types.no_data

        out["noData"] = capo_cloudwatchomni.types.no_data.serialize_cbor(
            value["no_data"]
        )
    return out


def deserialize_cbor(data: dict) -> TelemetryRule:
    out: TelemetryRule = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        import capo_cloudwatchomni.types.alert_rule_query

        out["query"] = capo_cloudwatchomni.types.alert_rule_query.deserialize_cbor(
            data["query"]
        )
    if data.get("condition") is not None:
        import capo_cloudwatchomni.types.alert_condition

        out["condition"] = capo_cloudwatchomni.types.alert_condition.deserialize_cbor(
            data["condition"]
        )
    if data.get("evaluation") is not None:
        import capo_cloudwatchomni.types.alert_evaluation

        out["evaluation"] = capo_cloudwatchomni.types.alert_evaluation.deserialize_cbor(
            data["evaluation"]
        )
    if data.get("noData") is not None:
        import capo_cloudwatchomni.types.no_data

        out["no_data"] = capo_cloudwatchomni.types.no_data.deserialize_cbor(
            data["noData"]
        )
    return out
