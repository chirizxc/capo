"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetTestTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.test_template


class GetTestTemplateResponse(TypedDict, closed=True):
    test_template: "capo_resiliencehubv2.types.test_template.TestTemplate"
    """<p>The requested test template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestTemplateResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.test_template

    out["testTemplate"] = capo_resiliencehubv2.types.test_template.serialize_json(
        value["test_template"]
    )
    return out


def deserialize_json(data: dict) -> GetTestTemplateResponse:
    out: GetTestTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("testTemplate") is not None:
        import capo_resiliencehubv2.types.test_template

        out["test_template"] = (
            capo_resiliencehubv2.types.test_template.deserialize_json(
                data["testTemplate"]
            )
        )
    else:
        raise DeserializationError("GetTestTemplateResponse.test_template required")
    return out
