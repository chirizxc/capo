"""Generated from Smithy shape ``com.amazonaws.vpclattice#CidrResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.cidr_range_list


class CidrResource(TypedDict, closed=True):
    cidr_ranges: NotRequired["capo_vpc_lattice.types.cidr_range_list.CidrRangeList"]
    """<p>The CIDR ranges of the network segment, for example, <code>10.0.0.0/16</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CidrResource) -> dict:
    out: dict = {}
    if "cidr_ranges" in value:
        import capo_vpc_lattice.types.cidr_range_list

        out["cidrRanges"] = capo_vpc_lattice.types.cidr_range_list.serialize_json(
            value["cidr_ranges"]
        )
    return out


def deserialize_json(data: dict) -> CidrResource:
    out: CidrResource = {}  # type: ignore[typeddict-item]
    if data.get("cidrRanges") is not None:
        import capo_vpc_lattice.types.cidr_range_list

        out["cidr_ranges"] = capo_vpc_lattice.types.cidr_range_list.deserialize_json(
            data["cidrRanges"]
        )
    return out
