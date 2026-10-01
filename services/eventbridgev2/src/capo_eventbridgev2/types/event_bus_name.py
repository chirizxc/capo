"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#EventBusName``."""

from typing import TypeAlias

"""Name of an event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '_'. The grammar matches the name segment of EventBusArn (event-busv2/<name>/<id>), so every valid name can be represented in the bus's ARN. The same type is used everywhere a bus name appears."""
EventBusName: TypeAlias = str
