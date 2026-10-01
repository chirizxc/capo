"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetInstrumentationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_configuration


class GetInstrumentationConfigurationResponse(TypedDict, closed=True):
    configuration: "capo_application_signals.types.instrumentation_configuration.InstrumentationConfiguration"
    """<p>The complete instrumentation configuration, including its location hash, capture settings, filters, expiration, and creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstrumentationConfigurationResponse) -> dict:
    out: dict = {}
    import capo_application_signals.types.instrumentation_configuration

    out["Configuration"] = (
        capo_application_signals.types.instrumentation_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetInstrumentationConfigurationResponse:
    out: GetInstrumentationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Configuration") is not None:
        import capo_application_signals.types.instrumentation_configuration

        out["configuration"] = (
            capo_application_signals.types.instrumentation_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "GetInstrumentationConfigurationResponse.configuration required"
        )
    return out
