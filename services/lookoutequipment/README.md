# Getting Started

## Installation

```
pip install capo-lookoutequipment
```

## Usage

```python
from capo_lookoutequipment import AsyncLookoutEquipmentClient


async def main():
    async with AsyncLookoutEquipmentClient() as lookout_equipment:
        # Example: call the create_dataset operation
        response = await lookout_equipment.create_dataset()
        print(response["dataset_name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_lookoutequipment import AsyncLookoutEquipmentClient


async def main():
    async with AsyncLookoutEquipmentClient() as lookout_equipment:
        # Example: paginate over list_data_ingestion_jobs
        async for item in lookout_equipment.iter_list_data_ingestion_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_lookoutequipment import AsyncLookoutEquipmentClient
from capo_lookoutequipment.error import AccessDeniedException


async def main():
    async with AsyncLookoutEquipmentClient() as lookout_equipment:
        try:
            await lookout_equipment.create_dataset()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_lookoutequipment import AsyncLookoutEquipmentClient


async def main():
    async with AsyncLookoutEquipmentClient() as lookout_equipment:
        # Default: 3 attempts for every operation
        response = await lookout_equipment.create_dataset()

        # Override per operation
        response = await lookout_equipment.create_dataset(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await lookout_equipment.create_dataset(config_overrides={"retry_max_attempts": 1})
```
