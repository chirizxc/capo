"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunEvents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.experiment_run_event_list
    import capo_appconfig.types.next_token


class ExperimentRunEvents(TypedDict, closed=True):
    items: NotRequired[
        "capo_appconfig.types.experiment_run_event_list.ExperimentRunEventList"
    ]
    """<p>The list of experiment run events.</p>"""
    next_token: NotRequired["capo_appconfig.types.next_token.NextToken"]
    """<p>A token to use for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunEvents) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_appconfig.types.experiment_run_event_list

        out["Items"] = capo_appconfig.types.experiment_run_event_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExperimentRunEvents:
    out: ExperimentRunEvents = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_appconfig.types.experiment_run_event_list

        out["items"] = capo_appconfig.types.experiment_run_event_list.deserialize_json(
            data["Items"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
