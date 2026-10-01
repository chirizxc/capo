"""Generated from Smithy shape ``com.amazonaws.appconfig#ExperimentDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.experiment_definition_summary

ExperimentDefinitionList: TypeAlias = list[
    "capo_appconfig.types.experiment_definition_summary.ExperimentDefinitionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentDefinitionList) -> list:
    import capo_appconfig.types.experiment_definition_summary

    out: list = []
    for item in value:
        out.append(
            capo_appconfig.types.experiment_definition_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExperimentDefinitionList:
    import capo_appconfig.types.experiment_definition_summary

    out: ExperimentDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appconfig.types.experiment_definition_summary.deserialize_json(item)
        )
    return out
