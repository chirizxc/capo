"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DynamicInstrumentationAttributeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.dynamic_instrumentation_attribute_filter_group

DynamicInstrumentationAttributeFilters: TypeAlias = list[
    "capo_application_signals.types.dynamic_instrumentation_attribute_filter_group.DynamicInstrumentationAttributeFilterGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: DynamicInstrumentationAttributeFilters) -> list:
    import capo_application_signals.types.dynamic_instrumentation_attribute_filter_group

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.dynamic_instrumentation_attribute_filter_group.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DynamicInstrumentationAttributeFilters:
    import capo_application_signals.types.dynamic_instrumentation_attribute_filter_group

    out: DynamicInstrumentationAttributeFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_signals.types.dynamic_instrumentation_attribute_filter_group.deserialize_json(
                item
            )
        )
    return out
