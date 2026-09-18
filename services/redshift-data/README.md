# Getting Started

## Installation

```
pip install capo-redshift-data
```

## Usage

```python
from capo_redshift_data import AsyncRedshiftDataClient


async def main():
    async with AsyncRedshiftDataClient() as redshift_data:
        # Example: call the batch_execute_statement operation
        response = await redshift_data.batch_execute_statement()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_redshift_data import AsyncRedshiftDataClient


async def main():
    async with AsyncRedshiftDataClient() as redshift_data:
        # Example: paginate over describe_table
        async for item in redshift_data.iter_describe_table():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_redshift_data import AsyncRedshiftDataClient
from capo_redshift_data.error import ActiveSessionsExceededException


async def main():
    async with AsyncRedshiftDataClient() as redshift_data:
        try:
            await redshift_data.batch_execute_statement()
        except ActiveSessionsExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_redshift_data import AsyncRedshiftDataClient


async def main():
    async with AsyncRedshiftDataClient() as redshift_data:
        # Default: 3 attempts for every operation
        response = await redshift_data.batch_execute_statement()

        # Override per operation
        response = await redshift_data.batch_execute_statement(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await redshift_data.batch_execute_statement(config_overrides={"retry_max_attempts": 1})
```
