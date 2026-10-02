"""Generated from Smithy shape ``com.amazonaws.applicationsignals#InstrumentationConfigurationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.instrumentation_configuration_status_report

InstrumentationConfigurationStatusList: TypeAlias = list[
    "capo_application_signals.types.instrumentation_configuration_status_report.InstrumentationConfigurationStatusReport"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstrumentationConfigurationStatusList) -> list:
    import capo_application_signals.types.instrumentation_configuration_status_report

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.instrumentation_configuration_status_report.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstrumentationConfigurationStatusList:
    import capo_application_signals.types.instrumentation_configuration_status_report

    out: InstrumentationConfigurationStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.instrumentation_configuration_status_report.deserialize_json(
                item
            )
        )
    return out
