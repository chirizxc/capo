"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SearchableNumberType``."""

from typing import TypeAlias

"""The type of phone number to search for with ListAvailablePhoneNumbers. Currently only TEN_DLC is supported; additional number types (for example TOLL_FREE) will be added in future phases. Modeled as a dedicated enum rather than RequestableNumberType so this operation advertises only the values it actually supports. New values may be added over time (backward compatible)."""
SearchableNumberType: TypeAlias = str
