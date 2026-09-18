# Getting Started

## Installation

```
pip install capo-database-migration-service
```

## Usage

```python
from capo_database_migration_service import AsyncDatabaseMigrationServiceClient


async def main():
    async with AsyncDatabaseMigrationServiceClient() as database_migration_service:
        # Example: call the add_tags_to_resource operation
        response = await database_migration_service.add_tags_to_resource()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_database_migration_service import AsyncDatabaseMigrationServiceClient


async def main():
    async with AsyncDatabaseMigrationServiceClient() as database_migration_service:
        # Example: paginate over describe_applicable_individual_assessments
        async for item in database_migration_service.iter_describe_applicable_individual_assessments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_database_migration_service import AsyncDatabaseMigrationServiceClient
from capo_database_migration_service.error import InvalidResourceStateFault


async def main():
    async with AsyncDatabaseMigrationServiceClient() as database_migration_service:
        try:
            await database_migration_service.add_tags_to_resource()
        except InvalidResourceStateFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_database_migration_service import AsyncDatabaseMigrationServiceClient


async def main():
    async with AsyncDatabaseMigrationServiceClient() as database_migration_service:
        # Default: 3 attempts for every operation
        response = await database_migration_service.add_tags_to_resource()

        # Override per operation
        response = await database_migration_service.add_tags_to_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await database_migration_service.add_tags_to_resource(config_overrides={"retry_max_attempts": 1})
```
