"""Generated from Smithy shape ``com.amazonaws.partnercentralrevenuemeasurement#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_revenue_measurement.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "capo_partnercentral_revenue_measurement.types.validation_exception_field.ValidationExceptionField"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidationExceptionFieldList) -> list:
    import capo_partnercentral_revenue_measurement.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_revenue_measurement.types.validation_exception_field.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ValidationExceptionFieldList:
    import capo_partnercentral_revenue_measurement.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_revenue_measurement.types.validation_exception_field.deserialize_cbor(
                item
            )
        )
    return out
