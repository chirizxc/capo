"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultSliderControlOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.sheet_control_slider_type
    import capo_quicksight.types.slider_control_display_options


class DefaultSliderControlOptions(TypedDict, closed=True):
    display_options: NotRequired[
        "capo_quicksight.types.slider_control_display_options.SliderControlDisplayOptions"
    ]
    """<p>The display options of a control.</p>"""
    type: NotRequired[
        "capo_quicksight.types.sheet_control_slider_type.SheetControlSliderType"
    ]
    """<p>The type of the <code>DefaultSliderControlOptions</code>. Choose one of the following options:</p> <ul> <li> <p> <code>SINGLE_POINT</code>: Filter against(equals) a single data point.</p> </li> <li> <p> <code>RANGE</code>: Filter data that is in a specified range.</p> </li> </ul>"""
    maximum_value: "capo_quicksight.types.double.Double"
    """<p>The larger value that is displayed at the right of the slider.</p>"""
    minimum_value: "capo_quicksight.types.double.Double"
    """<p>The smaller value that is displayed at the left of the slider.</p>"""
    step_size: "capo_quicksight.types.double.Double"
    """<p>The number of increments that the slider bar is divided into.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSliderControlOptions) -> dict:
    out: dict = {}
    if "display_options" in value:
        import capo_quicksight.types.slider_control_display_options

        out["DisplayOptions"] = (
            capo_quicksight.types.slider_control_display_options.serialize_json(
                value["display_options"]
            )
        )
    if "type" in value:
        import capo_quicksight.types.sheet_control_slider_type

        out["Type"] = capo_quicksight.types.sheet_control_slider_type.serialize_json(
            value["type"]
        )
    out["MaximumValue"] = (
        "NaN"
        if value.get("maximum_value", 0) != value.get("maximum_value", 0)
        else "Infinity"
        if value.get("maximum_value", 0) == float("inf")
        else "-Infinity"
        if value.get("maximum_value", 0) == float("-inf")
        else value.get("maximum_value", 0)
    )
    out["MinimumValue"] = (
        "NaN"
        if value.get("minimum_value", 0) != value.get("minimum_value", 0)
        else "Infinity"
        if value.get("minimum_value", 0) == float("inf")
        else "-Infinity"
        if value.get("minimum_value", 0) == float("-inf")
        else value.get("minimum_value", 0)
    )
    out["StepSize"] = (
        "NaN"
        if value.get("step_size", 0) != value.get("step_size", 0)
        else "Infinity"
        if value.get("step_size", 0) == float("inf")
        else "-Infinity"
        if value.get("step_size", 0) == float("-inf")
        else value.get("step_size", 0)
    )
    return out


def deserialize_json(data: dict) -> DefaultSliderControlOptions:
    out: DefaultSliderControlOptions = {}  # type: ignore[typeddict-item]
    if data.get("DisplayOptions") is not None:
        import capo_quicksight.types.slider_control_display_options

        out["display_options"] = (
            capo_quicksight.types.slider_control_display_options.deserialize_json(
                data["DisplayOptions"]
            )
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.sheet_control_slider_type

        out["type"] = capo_quicksight.types.sheet_control_slider_type.deserialize_json(
            data["Type"]
        )
    if data.get("MaximumValue") is not None:
        out["maximum_value"] = float(data["MaximumValue"])
    else:
        out["maximum_value"] = 0
    if data.get("MinimumValue") is not None:
        out["minimum_value"] = float(data["MinimumValue"])
    else:
        out["minimum_value"] = 0
    if data.get("StepSize") is not None:
        out["step_size"] = float(data["StepSize"])
    else:
        out["step_size"] = 0
    return out
