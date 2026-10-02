"""Generated from Smithy shape ``com.amazonaws.elementalinference#ClippingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.data_source_configuration
    import capo_elementalinference.types.resource_description


class ClippingConfig(TypedDict, closed=True):
    callback_metadata: NotRequired[
        "capo_elementalinference.types.resource_description.ResourceDescription"
    ]
    """<p>A string that you want Elemental Inference to always include in the event clipping metadata for this output. The string might identify the sports event in the source media, for example. </p>"""
    data_source_configuration: NotRequired[
        "capo_elementalinference.types.data_source_configuration.DataSourceConfiguration"
    ]
    """<p>The data source to map onto this clipping output. This parameter is optional. When you include this parameter, Elemental Inference reads the event data for the fixture that you specify, and includes that data in the event clipping metadata for this output. </p> <p>If you omit this parameter, Elemental Inference doesn't map a data source onto this output. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClippingConfig) -> dict:
    out: dict = {}
    if "callback_metadata" in value:
        out["callbackMetadata"] = value["callback_metadata"]
    if "data_source_configuration" in value:
        import capo_elementalinference.types.data_source_configuration

        out["dataSourceConfiguration"] = (
            capo_elementalinference.types.data_source_configuration.serialize_json(
                value["data_source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClippingConfig:
    out: ClippingConfig = {}  # type: ignore[typeddict-item]
    if data.get("callbackMetadata") is not None:
        out["callback_metadata"] = data["callbackMetadata"]
    if data.get("dataSourceConfiguration") is not None:
        import capo_elementalinference.types.data_source_configuration

        out["data_source_configuration"] = (
            capo_elementalinference.types.data_source_configuration.deserialize_json(
                data["dataSourceConfiguration"]
            )
        )
    return out
