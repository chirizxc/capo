"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertId``."""

from typing import TypeAlias

"""The stable alert identifier: a 32-character lowercase hex uuid, minted by the backend on create and immutable across updates. It deliberately carries no name, so that a future rename cannot change an alert's identity and break the ARNs, saved links and IAM policies pointing at it. Use {@code name} to display an alert and {@code alertId} to address one."""
AlertId: TypeAlias = str
