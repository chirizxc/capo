"""Generated from Smithy shape ``com.amazonaws.macie2#Cell``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long
    import capo_macie2.types.__string


class Cell(TypedDict, closed=True):
    cell_reference: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The location of the cell, as an absolute cell reference, that contains the sensitive data, for example Sheet2!C5 for cell C5 on Sheet2 in a Microsoft Excel workbook. This value is null for CSV and TSV files.</p>"""
    column: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The column number of the column that contains the sensitive data. For a Microsoft Excel workbook, this value correlates to the alphabetical character(s) for a column identifier, for example: 1 for column A, 2 for column B, and so on.</p>"""
    column_name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the column that contains the sensitive data, if available.</p>"""
    row: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The row number of the row that contains the sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cell) -> dict:
    out: dict = {}
    if "cell_reference" in value:
        out["cellReference"] = value["cell_reference"]
    if "column" in value:
        out["column"] = value["column"]
    if "column_name" in value:
        out["columnName"] = value["column_name"]
    if "row" in value:
        out["row"] = value["row"]
    return out


def deserialize_json(data: dict) -> Cell:
    out: Cell = {}  # type: ignore[typeddict-item]
    if data.get("cellReference") is not None:
        out["cell_reference"] = data["cellReference"]
    if data.get("column") is not None:
        out["column"] = data["column"]
    if data.get("columnName") is not None:
        out["column_name"] = data["columnName"]
    if data.get("row") is not None:
        out["row"] = data["row"]
    return out
