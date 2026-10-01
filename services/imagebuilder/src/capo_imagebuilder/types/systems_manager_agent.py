"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SystemsManagerAgent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.nullable_boolean


class SystemsManagerAgent(TypedDict, closed=True):
    uninstall_after_build: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether the Systems Manager agent is removed from your final build image before Image Builder creates the new AMI. If <code>true</code>, the agent is removed. If <code>false</code>, the agent is kept, so that it's included in the AMI. If you don't set this property, Image Builder removes the agent only if Image Builder installed the agent during the build. An agent that was pre-installed on the base image is kept.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemsManagerAgent) -> dict:
    out: dict = {}
    if "uninstall_after_build" in value:
        out["uninstallAfterBuild"] = value["uninstall_after_build"]
    return out


def deserialize_json(data: dict) -> SystemsManagerAgent:
    out: SystemsManagerAgent = {}  # type: ignore[typeddict-item]
    if data.get("uninstallAfterBuild") is not None:
        out["uninstall_after_build"] = data["uninstallAfterBuild"]
    return out
