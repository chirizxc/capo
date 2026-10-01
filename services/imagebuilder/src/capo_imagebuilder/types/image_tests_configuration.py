"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageTestsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_tests_timeout_minutes
    import capo_imagebuilder.types.nullable_boolean


class ImageTestsConfiguration(TypedDict, closed=True):
    image_tests_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether tests run after building the image. When enabled, tests run after the image build and before image distribution. Defaults to <code>true</code>.</p>"""
    timeout_minutes: NotRequired[
        "capo_imagebuilder.types.image_tests_timeout_minutes.ImageTestsTimeoutMinutes"
    ]
    """<p>The maximum time in minutes that tests are permitted to run. If you don't specify a value, Image Builder stores and returns 720.</p> <note> <p>The timeout property is not currently active. This value is ignored.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageTestsConfiguration) -> dict:
    out: dict = {}
    if "image_tests_enabled" in value:
        out["imageTestsEnabled"] = value["image_tests_enabled"]
    if "timeout_minutes" in value:
        out["timeoutMinutes"] = value["timeout_minutes"]
    return out


def deserialize_json(data: dict) -> ImageTestsConfiguration:
    out: ImageTestsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("imageTestsEnabled") is not None:
        out["image_tests_enabled"] = data["imageTestsEnabled"]
    if data.get("timeoutMinutes") is not None:
        out["timeout_minutes"] = data["timeoutMinutes"]
    return out
