# Getting Started

## Installation

```
pip install capo-backupsearch
```

## Usage

```python
from capo_backupsearch import AsyncBackupSearchClient


async def main():
    async with AsyncBackupSearchClient() as backup_search:
        # Example: call the list_search_job_backups operation
        response = await backup_search.list_search_job_backups()
        print(response["results"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_backupsearch import AsyncBackupSearchClient


async def main():
    async with AsyncBackupSearchClient() as backup_search:
        # Example: paginate over list_search_job_backups
        async for item in backup_search.iter_list_search_job_backups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_backupsearch import AsyncBackupSearchClient
from capo_backupsearch.error import AccessDeniedException


async def main():
    async with AsyncBackupSearchClient() as backup_search:
        try:
            await backup_search.list_search_job_backups()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_backupsearch import AsyncBackupSearchClient


async def main():
    async with AsyncBackupSearchClient() as backup_search:
        # Default: 3 attempts for every operation
        response = await backup_search.list_search_job_backups()

        # Override per operation
        response = await backup_search.list_search_job_backups(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await backup_search.list_search_job_backups(config_overrides={"retry_max_attempts": 1})
```
