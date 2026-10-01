"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentFailureContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_build_version_arn
    import capo_imagebuilder.types.non_empty_max_length_string
    import capo_imagebuilder.types.non_empty_string


class ComponentFailureContext(TypedDict, closed=True):
    component_arn: NotRequired[
        "capo_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the component build version that failed.</p>"""
    phase_name: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The name of the phase in the component document where the failure occurred, such as <code>build</code>, <code>validate</code>, or <code>test</code>.</p>"""
    step_name: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The name of the step in the component document that failed.</p>"""
    action: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The action that the failed step runs, for example <code>ExecuteBash</code>.</p>"""
    error_message: NotRequired[
        "capo_imagebuilder.types.non_empty_max_length_string.NonEmptyMaxLengthString"
    ]
    """<p>The error message from the step that failed. Image Builder truncates messages that are longer than 1024 characters. The component log in Amazon CloudWatch Logs contains the full output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentFailureContext) -> dict:
    out: dict = {}
    if "component_arn" in value:
        out["componentArn"] = value["component_arn"]
    if "phase_name" in value:
        out["phaseName"] = value["phase_name"]
    if "step_name" in value:
        out["stepName"] = value["step_name"]
    if "action" in value:
        out["action"] = value["action"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ComponentFailureContext:
    out: ComponentFailureContext = {}  # type: ignore[typeddict-item]
    if data.get("componentArn") is not None:
        out["component_arn"] = data["componentArn"]
    if data.get("phaseName") is not None:
        out["phase_name"] = data["phaseName"]
    if data.get("stepName") is not None:
        out["step_name"] = data["stepName"]
    if data.get("action") is not None:
        out["action"] = data["action"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
