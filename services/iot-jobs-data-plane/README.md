# Getting Started

## Installation

```
pip install capo-iot-jobs-data-plane
```

## Usage

```python
from capo_iot_jobs_data_plane import AsyncIoTJobsDataPlaneClient


async def main():
    async with AsyncIoTJobsDataPlaneClient() as io_t_jobs_data_plane:
        # Example: call the describe_job_execution operation
        response = await io_t_jobs_data_plane.describe_job_execution()
        print(response["execution"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_jobs_data_plane import AsyncIoTJobsDataPlaneClient
from capo_iot_jobs_data_plane.error import CertificateValidationException


async def main():
    async with AsyncIoTJobsDataPlaneClient() as io_t_jobs_data_plane:
        try:
            await io_t_jobs_data_plane.describe_job_execution()
        except CertificateValidationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_jobs_data_plane import AsyncIoTJobsDataPlaneClient


async def main():
    async with AsyncIoTJobsDataPlaneClient() as io_t_jobs_data_plane:
        # Default: 3 attempts for every operation
        response = await io_t_jobs_data_plane.describe_job_execution()

        # Override per operation
        response = await io_t_jobs_data_plane.describe_job_execution(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_jobs_data_plane.describe_job_execution(config_overrides={"retry_max_attempts": 1})
```
