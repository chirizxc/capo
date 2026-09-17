# Getting Started

## Installation

```
pip install capo-arc-zonal-shift
```

## Usage

```python
from capo_arc_zonal_shift import AsyncARCZonalShiftClient


async def main():
    async with AsyncARCZonalShiftClient() as arc_zonal_shift:
        # Example: call the list_autoshifts operation
        response = await arc_zonal_shift.list_autoshifts()
        print(response["items"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_arc_zonal_shift import AsyncARCZonalShiftClient


async def main():
    async with AsyncARCZonalShiftClient() as arc_zonal_shift:
        # Example: paginate over list_autoshifts
        async for item in arc_zonal_shift.iter_list_autoshifts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_arc_zonal_shift import AsyncARCZonalShiftClient
from capo_arc_zonal_shift.error import AccessDeniedException


async def main():
    async with AsyncARCZonalShiftClient() as arc_zonal_shift:
        try:
            await arc_zonal_shift.list_autoshifts()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_arc_zonal_shift import AsyncARCZonalShiftClient


async def main():
    async with AsyncARCZonalShiftClient() as arc_zonal_shift:
        # Default: 3 attempts for every operation
        response = await arc_zonal_shift.list_autoshifts()

        # Override per operation
        response = await arc_zonal_shift.list_autoshifts(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await arc_zonal_shift.list_autoshifts(config_overrides={"retry_max_attempts": 1})
```
