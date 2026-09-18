# Getting Started

## Installation

```
pip install capo-iotdeviceadvisor
```

## Usage

```python
from capo_iotdeviceadvisor import AsyncIotDeviceAdvisorClient


async def main():
    async with AsyncIotDeviceAdvisorClient() as iot_device_advisor:
        # Example: call the create_suite_definition operation
        response = await iot_device_advisor.create_suite_definition()
        print(response["suite_definition_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iotdeviceadvisor import AsyncIotDeviceAdvisorClient


async def main():
    async with AsyncIotDeviceAdvisorClient() as iot_device_advisor:
        # Example: paginate over list_suite_definitions
        async for item in iot_device_advisor.iter_list_suite_definitions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iotdeviceadvisor import AsyncIotDeviceAdvisorClient
from capo_iotdeviceadvisor.error import InternalServerException


async def main():
    async with AsyncIotDeviceAdvisorClient() as iot_device_advisor:
        try:
            await iot_device_advisor.create_suite_definition()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iotdeviceadvisor import AsyncIotDeviceAdvisorClient


async def main():
    async with AsyncIotDeviceAdvisorClient() as iot_device_advisor:
        # Default: 3 attempts for every operation
        response = await iot_device_advisor.create_suite_definition()

        # Override per operation
        response = await iot_device_advisor.create_suite_definition(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await iot_device_advisor.create_suite_definition(config_overrides={"retry_max_attempts": 1})
```
