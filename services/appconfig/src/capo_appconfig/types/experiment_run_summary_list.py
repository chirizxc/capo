"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentRunSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.experiment_run_summary

ExperimentRunSummaryList: TypeAlias = list[
    "capo_appconfig.types.experiment_run_summary.ExperimentRunSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentRunSummaryList) -> list:
    import capo_appconfig.types.experiment_run_summary

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.experiment_run_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentRunSummaryList:
    import capo_appconfig.types.experiment_run_summary

    out: ExperimentRunSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appconfig.types.experiment_run_summary.deserialize_json(item))
    return out
