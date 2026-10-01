"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationsWithoutServiceEnv``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_configuration_without_service_env

InstrumentationConfigurationsWithoutServiceEnv: TypeAlias = list[
    "capo_application_signals.types.instrumentation_configuration_without_service_env.InstrumentationConfigurationWithoutServiceEnv"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationConfigurationsWithoutServiceEnv) -> list:
    import capo_application_signals.types.instrumentation_configuration_without_service_env

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.instrumentation_configuration_without_service_env.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstrumentationConfigurationsWithoutServiceEnv:
    import capo_application_signals.types.instrumentation_configuration_without_service_env

    out: InstrumentationConfigurationsWithoutServiceEnv = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.instrumentation_configuration_without_service_env.deserialize_json(
                item
            )
        )
    return out
