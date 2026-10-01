"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryPlanStepArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.strict_drsarn

RecoveryPlanStepArnList: TypeAlias = list["capo_drs.types.strict_drsarn.StrictDRSARN"]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPlanStepArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecoveryPlanStepArnList:
    return [item for item in data if item is not None]
