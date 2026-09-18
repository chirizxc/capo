# Getting Started

## Installation

```
pip install capo-chime-sdk-messaging
```

## Usage

```python
from capo_chime_sdk_messaging import AsyncChimeSDKMessagingClient


async def main():
    async with AsyncChimeSDKMessagingClient() as chime_sdk_messaging:
        # Example: call the associate_channel_flow operation
        response = await chime_sdk_messaging.associate_channel_flow()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime_sdk_messaging import AsyncChimeSDKMessagingClient


async def main():
    async with AsyncChimeSDKMessagingClient() as chime_sdk_messaging:
        # Example: paginate over list_channel_bans
        async for item in chime_sdk_messaging.iter_list_channel_bans():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime_sdk_messaging import AsyncChimeSDKMessagingClient
from capo_chime_sdk_messaging.error import BadRequestException


async def main():
    async with AsyncChimeSDKMessagingClient() as chime_sdk_messaging:
        try:
            await chime_sdk_messaging.associate_channel_flow()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime_sdk_messaging import AsyncChimeSDKMessagingClient


async def main():
    async with AsyncChimeSDKMessagingClient() as chime_sdk_messaging:
        # Default: 3 attempts for every operation
        response = await chime_sdk_messaging.associate_channel_flow()

        # Override per operation
        response = await chime_sdk_messaging.associate_channel_flow(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime_sdk_messaging.associate_channel_flow(config_overrides={"retry_max_attempts": 1})
```
