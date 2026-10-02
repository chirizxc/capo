"""Generated from Smithy shape ``com.amazonaws.taxsettings#MonacoAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.business_number


class MonacoAdditionalInfo(TypedDict, closed=True):
    business_number: "capo_taxsettings.types.business_number.BusinessNumber"
    """<p>The business number for the company in Monaco. Can be up to 12 alphanumeric characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonacoAdditionalInfo) -> dict:
    out: dict = {}
    out["businessNumber"] = value["business_number"]
    return out


def deserialize_json(data: dict) -> MonacoAdditionalInfo:
    out: MonacoAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("businessNumber") is not None:
        out["business_number"] = data["businessNumber"]
    else:
        raise DeserializationError("MonacoAdditionalInfo.business_number required")
    return out
