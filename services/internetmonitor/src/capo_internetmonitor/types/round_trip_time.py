"""Generated from Smithy shape ``com.amazonaws.internetmonitor#RoundTripTime``."""

from typing_extensions import NotRequired, TypedDict


class RoundTripTime(TypedDict, closed=True):
    p50: NotRequired["float"]
    """<p>RTT at the 50th percentile (p50).</p>"""
    p90: NotRequired["float"]
    """<p>RTT at the 90th percentile (p90). </p>"""
    p95: NotRequired["float"]
    """<p>RTT at the 95th percentile (p95). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoundTripTime) -> dict:
    out: dict = {}
    if "p50" in value:
        out["P50"] = (
            "NaN"
            if value["p50"] != value["p50"]
            else "Infinity"
            if value["p50"] == float("inf")
            else "-Infinity"
            if value["p50"] == float("-inf")
            else value["p50"]
        )
    if "p90" in value:
        out["P90"] = (
            "NaN"
            if value["p90"] != value["p90"]
            else "Infinity"
            if value["p90"] == float("inf")
            else "-Infinity"
            if value["p90"] == float("-inf")
            else value["p90"]
        )
    if "p95" in value:
        out["P95"] = (
            "NaN"
            if value["p95"] != value["p95"]
            else "Infinity"
            if value["p95"] == float("inf")
            else "-Infinity"
            if value["p95"] == float("-inf")
            else value["p95"]
        )
    return out


def deserialize_json(data: dict) -> RoundTripTime:
    out: RoundTripTime = {}  # type: ignore[typeddict-item]
    if data.get("P50") is not None:
        out["p50"] = float(data["P50"])
    if data.get("P90") is not None:
        out["p90"] = float(data["P90"])
    if data.get("P95") is not None:
        out["p95"] = float(data["P95"])
    return out
