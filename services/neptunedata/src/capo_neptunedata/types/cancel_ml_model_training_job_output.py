"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelMLModelTrainingJobOutput``."""

from typing_extensions import NotRequired, TypedDict


class CancelMLModelTrainingJobOutput(TypedDict, closed=True):
    status: NotRequired["str"]
    """<p>The status of the cancellation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMLModelTrainingJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelMLModelTrainingJobOutput:
    out: CancelMLModelTrainingJobOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
