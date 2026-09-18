"""Generated from Smithy shape ``com.amazonaws.quicksight#PercentVisibleRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.percent_number

PercentVisibleRange = TypedDict(
    "PercentVisibleRange",
    {
        "from": NotRequired["capo_quicksight.types.percent_number.PercentNumber"],
        "to": NotRequired["capo_quicksight.types.percent_number.PercentNumber"],
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: PercentVisibleRange) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = (
            "NaN"
            if value["from"] != value["from"]
            else "Infinity"
            if value["from"] == float("inf")
            else "-Infinity"
            if value["from"] == float("-inf")
            else value["from"]
        )
    if "to" in value:
        out["To"] = (
            "NaN"
            if value["to"] != value["to"]
            else "Infinity"
            if value["to"] == float("inf")
            else "-Infinity"
            if value["to"] == float("-inf")
            else value["to"]
        )
    return out


def deserialize_json(data: dict) -> PercentVisibleRange:
    out: PercentVisibleRange = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = float(data["From"])
    if data.get("To") is not None:
        out["to"] = float(data["To"])
    return out
