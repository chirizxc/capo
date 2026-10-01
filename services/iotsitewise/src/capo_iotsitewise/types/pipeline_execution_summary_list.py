"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineExecutionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.pipeline_execution_summary

PipelineExecutionSummaryList: TypeAlias = list[
    "capo_iotsitewise.types.pipeline_execution_summary.PipelineExecutionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionSummaryList) -> list:
    import capo_iotsitewise.types.pipeline_execution_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.pipeline_execution_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PipelineExecutionSummaryList:
    import capo_iotsitewise.types.pipeline_execution_summary

    out: PipelineExecutionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iotsitewise.types.pipeline_execution_summary.deserialize_json(item)
        )
    return out
