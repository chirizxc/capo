"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.experiment_run_event

ExperimentRunEventList: TypeAlias = list[
    "capo_appconfig.types.experiment_run_event.ExperimentRunEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunEventList) -> list:
    import capo_appconfig.types.experiment_run_event

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.experiment_run_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentRunEventList:
    import capo_appconfig.types.experiment_run_event

    out: ExperimentRunEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appconfig.types.experiment_run_event.deserialize_json(item))
    return out
