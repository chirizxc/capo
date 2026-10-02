"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#StateReason``."""

from typing import TypeAlias

"""Human-readable explanation of why an event bus is in its current State. Omitted when the bus is in a normal operational state (ACTIVE). It stands in for the error response an asynchronous failure cannot return, so it applies only to resources with an asynchronous lifecycle: event buses. EventSources and subscribers are provisioned synchronously and report failures directly on the request."""
StateReason: TypeAlias = str
