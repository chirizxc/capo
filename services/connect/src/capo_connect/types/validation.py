"""Generated from Smithy shape ``com.amazonaws.connect#Validation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.length_boundary
    import capo_connect.types.positive_and_negative_double
    import capo_connect.types.positive_double
    import capo_connect.types.validation_enum
    import capo_connect.types.value_boundary


class Validation(TypedDict, closed=True):
    min_length: "capo_connect.types.length_boundary.LengthBoundary"
    """<p>The minimum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT_LIST. Must be less than or equal to MaxLength.</p>"""
    max_length: "capo_connect.types.length_boundary.LengthBoundary"
    """<p>The maximum number of characters a text value can contain. Applies to TEXT value type and values within a TEXT_LIST. Must be greater than or equal to MinLength.</p>"""
    min_values: "capo_connect.types.value_boundary.ValueBoundary"
    """<p>The minimum number of values in a list. Must be an integer greater than or equal to 0 and less than or equal to MaxValues. Applies to all list types.</p>"""
    max_values: "capo_connect.types.value_boundary.ValueBoundary"
    """<p>The maximum number of values in a list. Must be an integer greater than or equal to 0 and greater than or equal to MinValues. Applies to all list types.</p>"""
    ignore_case: "capo_connect.types.boolean.Boolean"
    """<p>Boolean that defaults to false. Applies to text lists and text primary attributes. When true, enforces case-insensitive uniqueness for primary attributes and allows case-insensitive lookups.</p>"""
    minimum: "capo_connect.types.positive_and_negative_double.PositiveAndNegativeDouble"
    """<p>The smallest inclusive numeric value for NUMBER value type. Cannot be provided when ExclusiveMinimum is also provided. Must be less than or equal to Maximum and less than ExclusiveMaximum. Applies to NUMBER and values within NUMBER_LIST.</p>"""
    maximum: "capo_connect.types.positive_and_negative_double.PositiveAndNegativeDouble"
    """<p>The largest inclusive numeric value for NUMBER value type. Can be provided alongside ExclusiveMaximum where both operate independently. Must be greater than or equal to Minimum and greater than ExclusiveMinimum. Applies to NUMBER and values within NUMBER_LIST.</p>"""
    exclusive_minimum: (
        "capo_connect.types.positive_and_negative_double.PositiveAndNegativeDouble"
    )
    """<p>The smallest exclusive numeric value for NUMBER value type. Can be provided alongside Minimum where both operate independently. Must be less than ExclusiveMaximum and Maximum. Applies to NUMBER and values within NUMBER_LIST.</p>"""
    exclusive_maximum: (
        "capo_connect.types.positive_and_negative_double.PositiveAndNegativeDouble"
    )
    """<p>The largest exclusive numeric value for NUMBER value type. Can be provided alongside Maximum where both operate independently. Must be greater than ExclusiveMinimum and Minimum. Applies to NUMBER and values within NUMBER_LIST.</p>"""
    multiple_of: "capo_connect.types.positive_double.PositiveDouble"
    """<p>Specifies that numeric values must be multiples of this number. Must be greater than 0. The result of dividing a value by this multiple must result in an integer. Applies to NUMBER and values within NUMBER_LIST.</p>"""
    enum: NotRequired["capo_connect.types.validation_enum.ValidationEnum"]
    """<p>Defines enumeration constraints for attribute values. Can specify a list of allowed values and whether custom values are permitted beyond the enumerated list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Validation) -> dict:
    out: dict = {}
    out["MinLength"] = value.get("min_length", 0)
    out["MaxLength"] = value.get("max_length", 0)
    out["MinValues"] = value.get("min_values", 0)
    out["MaxValues"] = value.get("max_values", 0)
    out["IgnoreCase"] = value.get("ignore_case", False)
    out["Minimum"] = (
        "NaN"
        if value.get("minimum", 0) != value.get("minimum", 0)
        else "Infinity"
        if value.get("minimum", 0) == float("inf")
        else "-Infinity"
        if value.get("minimum", 0) == float("-inf")
        else value.get("minimum", 0)
    )
    out["Maximum"] = (
        "NaN"
        if value.get("maximum", 0) != value.get("maximum", 0)
        else "Infinity"
        if value.get("maximum", 0) == float("inf")
        else "-Infinity"
        if value.get("maximum", 0) == float("-inf")
        else value.get("maximum", 0)
    )
    out["ExclusiveMinimum"] = (
        "NaN"
        if value.get("exclusive_minimum", 0) != value.get("exclusive_minimum", 0)
        else "Infinity"
        if value.get("exclusive_minimum", 0) == float("inf")
        else "-Infinity"
        if value.get("exclusive_minimum", 0) == float("-inf")
        else value.get("exclusive_minimum", 0)
    )
    out["ExclusiveMaximum"] = (
        "NaN"
        if value.get("exclusive_maximum", 0) != value.get("exclusive_maximum", 0)
        else "Infinity"
        if value.get("exclusive_maximum", 0) == float("inf")
        else "-Infinity"
        if value.get("exclusive_maximum", 0) == float("-inf")
        else value.get("exclusive_maximum", 0)
    )
    out["MultipleOf"] = (
        "NaN"
        if value.get("multiple_of", 0) != value.get("multiple_of", 0)
        else "Infinity"
        if value.get("multiple_of", 0) == float("inf")
        else "-Infinity"
        if value.get("multiple_of", 0) == float("-inf")
        else value.get("multiple_of", 0)
    )
    if "enum" in value:
        import capo_connect.types.validation_enum

        out["Enum"] = capo_connect.types.validation_enum.serialize_json(value["enum"])
    return out


def deserialize_json(data: dict) -> Validation:
    out: Validation = {}  # type: ignore[typeddict-item]
    if data.get("MinLength") is not None:
        out["min_length"] = data["MinLength"]
    else:
        out["min_length"] = 0
    if data.get("MaxLength") is not None:
        out["max_length"] = data["MaxLength"]
    else:
        out["max_length"] = 0
    if data.get("MinValues") is not None:
        out["min_values"] = data["MinValues"]
    else:
        out["min_values"] = 0
    if data.get("MaxValues") is not None:
        out["max_values"] = data["MaxValues"]
    else:
        out["max_values"] = 0
    if data.get("IgnoreCase") is not None:
        out["ignore_case"] = data["IgnoreCase"]
    else:
        out["ignore_case"] = False
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    else:
        out["minimum"] = 0
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    else:
        out["maximum"] = 0
    if data.get("ExclusiveMinimum") is not None:
        out["exclusive_minimum"] = float(data["ExclusiveMinimum"])
    else:
        out["exclusive_minimum"] = 0
    if data.get("ExclusiveMaximum") is not None:
        out["exclusive_maximum"] = float(data["ExclusiveMaximum"])
    else:
        out["exclusive_maximum"] = 0
    if data.get("MultipleOf") is not None:
        out["multiple_of"] = float(data["MultipleOf"])
    else:
        out["multiple_of"] = 0
    if data.get("Enum") is not None:
        import capo_connect.types.validation_enum

        out["enum"] = capo_connect.types.validation_enum.deserialize_json(data["Enum"])
    return out
