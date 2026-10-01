"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_version_arn_or_build_version_arn


class GetComponentRequest(TypedDict, closed=True):
    component_build_version_arn: "capo_imagebuilder.types.component_version_arn_or_build_version_arn.ComponentVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the component that you want to get. You can specify a build version ARN, or a component version ARN. The version can use the <code>x</code> wildcard in trailing positions, for example <code>1.0.x</code> or <code>1.x.x</code>. Version ARNs resolve to the latest available matching component build version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentRequest:
    out: GetComponentRequest = {}  # type: ignore[typeddict-item]
    return out
