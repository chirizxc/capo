"""Generated from Smithy shape ``com.amazonaws.securityagent#Step``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.step_name
    import capo_securityagent.types.step_status


class Step(TypedDict, closed=True):
    name: NotRequired["capo_securityagent.types.step_name.StepName"]
    """<p>The name of the step. Valid values include PREFLIGHT, STATIC_ANALYSIS, PENTEST, and FINALIZING.</p>"""
    status: NotRequired["capo_securityagent.types.step_status.StepStatus"]
    """<p>The current status of the step.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the step was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the step was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_securityagent.types.step_name

        out["name"] = capo_securityagent.types.step_name.serialize_json(value["name"])
    if "status" in value:
        import capo_securityagent.types.step_status

        out["status"] = capo_securityagent.types.step_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_securityagent._protocol.serialize

        out["createdAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent._protocol.serialize

        out["updatedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_securityagent.types.step_name

        out["name"] = capo_securityagent.types.step_name.deserialize_json(data["name"])
    if data.get("status") is not None:
        import capo_securityagent.types.step_status

        out["status"] = capo_securityagent.types.step_status.deserialize_json(
            data["status"]
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out
