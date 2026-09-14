# Getting Started

## Installation

```
pip install capo-bcm-data-exports
```

## Usage

```python
from capo_bcm_data_exports import AsyncBCMDataExportsClient


async def main():
    async with AsyncBCMDataExportsClient() as bcm_data_exports:
        # Example: call the get_execution operation
        response = await bcm_data_exports.get_execution()
        print(response["execution_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bcm_data_exports import AsyncBCMDataExportsClient


async def main():
    async with AsyncBCMDataExportsClient() as bcm_data_exports:
        # Example: paginate over list_executions
        async for item in bcm_data_exports.iter_list_executions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bcm_data_exports import AsyncBCMDataExportsClient
from capo_bcm_data_exports.error import InternalServerException


async def main():
    async with AsyncBCMDataExportsClient() as bcm_data_exports:
        try:
            await bcm_data_exports.get_execution()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bcm_data_exports import AsyncBCMDataExportsClient


async def main():
    async with AsyncBCMDataExportsClient() as bcm_data_exports:
        # Default: 3 attempts for every operation
        response = await bcm_data_exports.get_execution()

        # Override per operation
        response = await bcm_data_exports.get_execution(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bcm_data_exports.get_execution(config_overrides={"retry_max_attempts": 1})
```
