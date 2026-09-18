"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInitiation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.recovery_instance_data_replication_initiation_steps


class RecoveryInstanceDataReplicationInitiation(TypedDict, closed=True):
    start_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of the current attempt to initiate data replication.</p>"""
    steps: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_initiation_steps.RecoveryInstanceDataReplicationInitiationSteps"
    ]
    """<p>The steps of the current attempt to initiate data replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInitiation) -> dict:
    out: dict = {}
    if "start_date_time" in value:
        out["startDateTime"] = value["start_date_time"]
    if "steps" in value:
        import capo_drs.types.recovery_instance_data_replication_initiation_steps

        out["steps"] = (
            capo_drs.types.recovery_instance_data_replication_initiation_steps.serialize_json(
                value["steps"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationInitiation:
    out: RecoveryInstanceDataReplicationInitiation = {}  # type: ignore[typeddict-item]
    if data.get("startDateTime") is not None:
        out["start_date_time"] = data["startDateTime"]
    if data.get("steps") is not None:
        import capo_drs.types.recovery_instance_data_replication_initiation_steps

        out["steps"] = (
            capo_drs.types.recovery_instance_data_replication_initiation_steps.deserialize_json(
                data["steps"]
            )
        )
    return out
