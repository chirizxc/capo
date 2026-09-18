# Getting Started

## Installation

```
pip install capo-docdb-elastic
```

## Usage

```python
from capo_docdb_elastic import AsyncDocDBElasticClient


async def main():
    async with AsyncDocDBElasticClient() as doc_db_elastic:
        # Example: call the apply_pending_maintenance_action operation
        response = await doc_db_elastic.apply_pending_maintenance_action()
        print(response["resource_pending_maintenance_action"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_docdb_elastic import AsyncDocDBElasticClient


async def main():
    async with AsyncDocDBElasticClient() as doc_db_elastic:
        # Example: paginate over list_clusters
        async for item in doc_db_elastic.iter_list_clusters():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_docdb_elastic import AsyncDocDBElasticClient
from capo_docdb_elastic.error import AccessDeniedException


async def main():
    async with AsyncDocDBElasticClient() as doc_db_elastic:
        try:
            await doc_db_elastic.apply_pending_maintenance_action()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_docdb_elastic import AsyncDocDBElasticClient


async def main():
    async with AsyncDocDBElasticClient() as doc_db_elastic:
        # Default: 3 attempts for every operation
        response = await doc_db_elastic.apply_pending_maintenance_action()

        # Override per operation
        response = await doc_db_elastic.apply_pending_maintenance_action(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await doc_db_elastic.apply_pending_maintenance_action(config_overrides={"retry_max_attempts": 1})
```
