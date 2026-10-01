"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributionFailureContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_max_length_string
    import capo_imagebuilder.types.region_failure_list


class DistributionFailureContext(TypedDict, closed=True):
    error_message: NotRequired[
        "capo_imagebuilder.types.non_empty_max_length_string.NonEmptyMaxLengthString"
    ]
    """<p>The error message for the distribution failure.</p>"""
    region_failures: NotRequired[
        "capo_imagebuilder.types.region_failure_list.RegionFailureList"
    ]
    """<p>The details about the failure for each Region where the image didn't finish distribution or configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributionFailureContext) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "region_failures" in value:
        import capo_imagebuilder.types.region_failure_list

        out["regionFailures"] = (
            capo_imagebuilder.types.region_failure_list.serialize_json(
                value["region_failures"]
            )
        )
    return out


def deserialize_json(data: dict) -> DistributionFailureContext:
    out: DistributionFailureContext = {}  # type: ignore[typeddict-item]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("regionFailures") is not None:
        import capo_imagebuilder.types.region_failure_list

        out["region_failures"] = (
            capo_imagebuilder.types.region_failure_list.deserialize_json(
                data["regionFailures"]
            )
        )
    return out
