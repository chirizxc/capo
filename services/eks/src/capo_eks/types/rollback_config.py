"""Generated from Smithy shape ``com.amazonaws.eks#RollbackConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_integer


class RollbackConfig(TypedDict, closed=True):
    timeout_minutes: NotRequired["capo_eks.types.boxed_integer.BoxedInteger"]
    """<p>The length of time in minutes to wait before cancelling the update. Timeout is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. This value can be between 120 (2 hours) and 10080 (7 days). Default: <code>720</code> (12 hours) if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackConfig) -> dict:
    out: dict = {}
    if "timeout_minutes" in value:
        out["timeoutMinutes"] = value["timeout_minutes"]
    return out


def deserialize_json(data: dict) -> RollbackConfig:
    out: RollbackConfig = {}  # type: ignore[typeddict-item]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    return out
