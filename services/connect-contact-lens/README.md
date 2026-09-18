# Getting Started

## Installation

```
pip install capo-connect-contact-lens
```

## Usage

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient


async def main():
    async with AsyncConnectContactLensClient() as connect_contact_lens:
        # Example: call the list_realtime_contact_analysis_segments operation
        response = await connect_contact_lens.list_realtime_contact_analysis_segments()
        print(response["segments"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient


async def main():
    async with AsyncConnectContactLensClient() as connect_contact_lens:
        # Example: paginate over list_realtime_contact_analysis_segments
        async for item in connect_contact_lens.iter_list_realtime_contact_analysis_segments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient
from capo_connect_contact_lens.error import AccessDeniedException


async def main():
    async with AsyncConnectContactLensClient() as connect_contact_lens:
        try:
            await connect_contact_lens.list_realtime_contact_analysis_segments()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connect_contact_lens import AsyncConnectContactLensClient


async def main():
    async with AsyncConnectContactLensClient() as connect_contact_lens:
        # Default: 3 attempts for every operation
        response = await connect_contact_lens.list_realtime_contact_analysis_segments()

        # Override per operation
        response = await connect_contact_lens.list_realtime_contact_analysis_segments(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await connect_contact_lens.list_realtime_contact_analysis_segments(config_overrides={"retry_max_attempts": 1})
```
