# Getting Started

## Installation

```
pip install capo-artifact
```

## Usage

```python
from capo_artifact import AsyncArtifactClient


async def main():
    async with AsyncArtifactClient() as artifact:
        # Example: call the get_account_settings operation
        response = await artifact.get_account_settings()
        print(response["account_settings"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_artifact import AsyncArtifactClient


async def main():
    async with AsyncArtifactClient() as artifact:
        # Example: paginate over list_customer_agreements
        async for item in artifact.iter_list_customer_agreements():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_artifact import AsyncArtifactClient
from capo_artifact.error import AccessDeniedException


async def main():
    async with AsyncArtifactClient() as artifact:
        try:
            await artifact.get_account_settings()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_artifact import AsyncArtifactClient


async def main():
    async with AsyncArtifactClient() as artifact:
        # Default: 3 attempts for every operation
        response = await artifact.get_account_settings()

        # Override per operation
        response = await artifact.get_account_settings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await artifact.get_account_settings(config_overrides={"retry_max_attempts": 1})
```
