"""Generated from Smithy shape ``com.amazonaws.location#LteNetworkMeasurements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.earfcn
    import capo_location.types.eutran_cell_id
    import capo_location.types.pci
    import capo_location.types.rsrp
    import capo_location.types.rsrq


class LteNetworkMeasurements(TypedDict, closed=True):
    earfcn: "capo_location.types.earfcn.Earfcn"
    """<p>E-UTRA (Evolved Universal Terrestrial Radio Access) absolute radio frequency channel number (EARFCN).</p>"""
    cell_id: "capo_location.types.eutran_cell_id.EutranCellId"
    """<p>E-UTRAN Cell Identifier (ECI).</p>"""
    pci: "capo_location.types.pci.Pci"
    """<p>Physical Cell ID (PCI).</p>"""
    rsrp: NotRequired["capo_location.types.rsrp.Rsrp"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["capo_location.types.rsrq.Rsrq"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteNetworkMeasurements) -> dict:
    out: dict = {}
    out["Earfcn"] = value.get("earfcn", 0)
    out["CellId"] = value.get("cell_id", 0)
    out["Pci"] = value.get("pci", 0)
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = (
            "NaN"
            if value["rsrq"] != value["rsrq"]
            else "Infinity"
            if value["rsrq"] == float("inf")
            else "-Infinity"
            if value["rsrq"] == float("-inf")
            else value["rsrq"]
        )
    return out


def deserialize_json(data: dict) -> LteNetworkMeasurements:
    out: LteNetworkMeasurements = {}  # type: ignore[typeddict-item]
    if data.get("Earfcn") is not None:
        out["earfcn"] = data["Earfcn"]
    else:
        out["earfcn"] = 0
    if data.get("CellId") is not None:
        out["cell_id"] = data["CellId"]
    else:
        out["cell_id"] = 0
    if data.get("Pci") is not None:
        out["pci"] = data["Pci"]
    else:
        out["pci"] = 0
    if data.get("Rsrp") is not None:
        out["rsrp"] = data["Rsrp"]
    if data.get("Rsrq") is not None:
        out["rsrq"] = float(data["Rsrq"])
    return out
