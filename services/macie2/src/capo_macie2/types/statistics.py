"""Generated from Smithy shape ``com.amazonaws.macie2#Statistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__double


class Statistics(TypedDict, closed=True):
    approximate_number_of_objects_to_process: NotRequired[
        "capo_macie2.types.__double.__double"
    ]
    """<p>The approximate number of objects that the job has yet to process during its current run.</p>"""
    number_of_runs: NotRequired["capo_macie2.types.__double.__double"]
    """<p>The number of times that the job has run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Statistics) -> dict:
    out: dict = {}
    if "approximate_number_of_objects_to_process" in value:
        out["approximateNumberOfObjectsToProcess"] = (
            "NaN"
            if value["approximate_number_of_objects_to_process"]
            != value["approximate_number_of_objects_to_process"]
            else "Infinity"
            if value["approximate_number_of_objects_to_process"] == float("inf")
            else "-Infinity"
            if value["approximate_number_of_objects_to_process"] == float("-inf")
            else value["approximate_number_of_objects_to_process"]
        )
    if "number_of_runs" in value:
        out["numberOfRuns"] = (
            "NaN"
            if value["number_of_runs"] != value["number_of_runs"]
            else "Infinity"
            if value["number_of_runs"] == float("inf")
            else "-Infinity"
            if value["number_of_runs"] == float("-inf")
            else value["number_of_runs"]
        )
    return out


def deserialize_json(data: dict) -> Statistics:
    out: Statistics = {}  # type: ignore[typeddict-item]
    if data.get("approximateNumberOfObjectsToProcess") is not None:
        out["approximate_number_of_objects_to_process"] = float(
            data["approximateNumberOfObjectsToProcess"]
        )
    if data.get("numberOfRuns") is not None:
        out["number_of_runs"] = float(data["numberOfRuns"])
    return out
