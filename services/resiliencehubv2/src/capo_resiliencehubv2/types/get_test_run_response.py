"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetTestRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_run


class GetTestRunResponse(TypedDict, closed=True):
    test_run: "capo_resiliencehubv2.types.test_run.TestRun"
    """<p>The requested test run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestRunResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_run

    out["testRun"] = capo_resiliencehubv2.types.test_run.serialize_json(
        value["test_run"]
    )
    return out


def deserialize_json(data: dict) -> GetTestRunResponse:
    out: GetTestRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("testRun") is not None:
        import capo_resiliencehubv2.types.test_run

        out["test_run"] = capo_resiliencehubv2.types.test_run.deserialize_json(
            data["testRun"]
        )
    else:
        raise DeserializationError("GetTestRunResponse.test_run required")
    return out
