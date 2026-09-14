"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#CustomColors``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__string_min1_max16


class CustomColors(TypedDict, closed=True):
    accent_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>Represents the accent color.</p>"""
    background_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>Represents the background color.</p>"""
    error_validation_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>The errorValidationColor.</p>"""
    header_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>Represents the header color.</p>"""
    navigation_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>Represents the navigation color.</p>"""
    text_color: NotRequired[
        "capo_apigatewayv2.types.__string_min1_max16.__stringMin1Max16"
    ]
    """<p>Represents the text color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomColors) -> dict:
    out: dict = {}
    if "accent_color" in value:
        out["accentColor"] = value["accent_color"]
    if "background_color" in value:
        out["backgroundColor"] = value["background_color"]
    if "error_validation_color" in value:
        out["errorValidationColor"] = value["error_validation_color"]
    if "header_color" in value:
        out["headerColor"] = value["header_color"]
    if "navigation_color" in value:
        out["navigationColor"] = value["navigation_color"]
    if "text_color" in value:
        out["textColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> CustomColors:
    out: CustomColors = {}  # type: ignore[typeddict-item]
    if data.get("accentColor") is not None:
        out["accent_color"] = data["accentColor"]
    if data.get("backgroundColor") is not None:
        out["background_color"] = data["backgroundColor"]
    if data.get("errorValidationColor") is not None:
        out["error_validation_color"] = data["errorValidationColor"]
    if data.get("headerColor") is not None:
        out["header_color"] = data["headerColor"]
    if data.get("navigationColor") is not None:
        out["navigation_color"] = data["navigationColor"]
    if data.get("textColor") is not None:
        out["text_color"] = data["textColor"]
    return out
