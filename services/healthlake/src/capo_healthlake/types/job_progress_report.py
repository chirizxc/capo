"""Generated from Smithy shape ``com.amazonaws.healthlake#JobProgressReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.generic_double
    import capo_healthlake.types.generic_long


class JobProgressReport(TypedDict, closed=True):
    total_number_of_scanned_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files scanned from the Amazon S3 input bucket.</p>"""
    total_size_of_scanned_files_in_mb: NotRequired[
        "capo_healthlake.types.generic_double.GenericDouble"
    ]
    """<p>The size (in MB) of files scanned from the Amazon S3 input bucket.</p>"""
    total_number_of_imported_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files imported.</p>"""
    total_number_of_resources_scanned: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources scanned from the Amazon S3 input bucket.</p>"""
    total_number_of_resources_imported: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources imported.</p>"""
    total_number_of_resources_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of resources that failed due to customer error.</p>"""
    total_number_of_files_read_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of files that failed to be read from the Amazon S3 input bucket due to customer error.</p>"""
    total_number_of_scanned_non_fhir_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR files scanned from the Amazon S3 input bucket.</p>"""
    total_size_of_scanned_non_fhir_files_in_mb: NotRequired[
        "capo_healthlake.types.generic_double.GenericDouble"
    ]
    """<p>The size (in MB) of non-FHIR files scanned from the Amazon S3 input bucket.</p>"""
    total_number_of_imported_non_fhir_files: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR files imported.</p>"""
    total_number_of_non_fhir_resources_scanned: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR resources scanned from the Amazon S3 input bucket.</p>"""
    total_number_of_non_fhir_resources_imported: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR resources imported.</p>"""
    total_number_of_non_fhir_resources_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR resources that failed due to customer error.</p>"""
    total_number_of_non_fhir_files_read_with_customer_error: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>The number of non-FHIR files that failed to be read from the Amazon S3 input bucket due to customer error.</p>"""
    throughput: NotRequired["capo_healthlake.types.generic_double.GenericDouble"]
    """<p>The transaction rate the import job is processed at.</p>"""
    total_files_converted: NotRequired["capo_healthlake.types.generic_long.GenericLong"]
    """<p>Number of CCDA files successfully transformed during the import's transformation phase. Populated only for import jobs that use the two-Step-Function (transformation + ingestion) flow; null for legacy single-SF imports and for pure FHIR imports that skip transformation.</p>"""
    total_resources_generated: NotRequired[
        "capo_healthlake.types.generic_long.GenericLong"
    ]
    """<p>Number of FHIR resources produced by the transformation phase. Populated only for import jobs that use the two-Step-Function flow; null for legacy single-SF imports and for pure FHIR imports.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobProgressReport) -> dict:
    out: dict = {}
    if "total_number_of_scanned_files" in value:
        out["TotalNumberOfScannedFiles"] = value["total_number_of_scanned_files"]
    if "total_size_of_scanned_files_in_mb" in value:
        out["TotalSizeOfScannedFilesInMB"] = (
            "NaN"
            if value["total_size_of_scanned_files_in_mb"]
            != value["total_size_of_scanned_files_in_mb"]
            else "Infinity"
            if value["total_size_of_scanned_files_in_mb"] == float("inf")
            else "-Infinity"
            if value["total_size_of_scanned_files_in_mb"] == float("-inf")
            else value["total_size_of_scanned_files_in_mb"]
        )
    if "total_number_of_imported_files" in value:
        out["TotalNumberOfImportedFiles"] = value["total_number_of_imported_files"]
    if "total_number_of_resources_scanned" in value:
        out["TotalNumberOfResourcesScanned"] = value[
            "total_number_of_resources_scanned"
        ]
    if "total_number_of_resources_imported" in value:
        out["TotalNumberOfResourcesImported"] = value[
            "total_number_of_resources_imported"
        ]
    if "total_number_of_resources_with_customer_error" in value:
        out["TotalNumberOfResourcesWithCustomerError"] = value[
            "total_number_of_resources_with_customer_error"
        ]
    if "total_number_of_files_read_with_customer_error" in value:
        out["TotalNumberOfFilesReadWithCustomerError"] = value[
            "total_number_of_files_read_with_customer_error"
        ]
    if "total_number_of_scanned_non_fhir_files" in value:
        out["TotalNumberOfScannedNonFhirFiles"] = value[
            "total_number_of_scanned_non_fhir_files"
        ]
    if "total_size_of_scanned_non_fhir_files_in_mb" in value:
        out["TotalSizeOfScannedNonFhirFilesInMB"] = (
            "NaN"
            if value["total_size_of_scanned_non_fhir_files_in_mb"]
            != value["total_size_of_scanned_non_fhir_files_in_mb"]
            else "Infinity"
            if value["total_size_of_scanned_non_fhir_files_in_mb"] == float("inf")
            else "-Infinity"
            if value["total_size_of_scanned_non_fhir_files_in_mb"] == float("-inf")
            else value["total_size_of_scanned_non_fhir_files_in_mb"]
        )
    if "total_number_of_imported_non_fhir_files" in value:
        out["TotalNumberOfImportedNonFhirFiles"] = value[
            "total_number_of_imported_non_fhir_files"
        ]
    if "total_number_of_non_fhir_resources_scanned" in value:
        out["TotalNumberOfNonFhirResourcesScanned"] = value[
            "total_number_of_non_fhir_resources_scanned"
        ]
    if "total_number_of_non_fhir_resources_imported" in value:
        out["TotalNumberOfNonFhirResourcesImported"] = value[
            "total_number_of_non_fhir_resources_imported"
        ]
    if "total_number_of_non_fhir_resources_with_customer_error" in value:
        out["TotalNumberOfNonFhirResourcesWithCustomerError"] = value[
            "total_number_of_non_fhir_resources_with_customer_error"
        ]
    if "total_number_of_non_fhir_files_read_with_customer_error" in value:
        out["TotalNumberOfNonFhirFilesReadWithCustomerError"] = value[
            "total_number_of_non_fhir_files_read_with_customer_error"
        ]
    if "throughput" in value:
        out["Throughput"] = (
            "NaN"
            if value["throughput"] != value["throughput"]
            else "Infinity"
            if value["throughput"] == float("inf")
            else "-Infinity"
            if value["throughput"] == float("-inf")
            else value["throughput"]
        )
    if "total_files_converted" in value:
        out["TotalFilesConverted"] = value["total_files_converted"]
    if "total_resources_generated" in value:
        out["TotalResourcesGenerated"] = value["total_resources_generated"]
    return out


def deserialize_aws_json_1_0(data: dict) -> JobProgressReport:
    out: JobProgressReport = {}  # type: ignore[typeddict-item]
    if data.get("TotalNumberOfScannedFiles") is not None:
        out["total_number_of_scanned_files"] = data["TotalNumberOfScannedFiles"]
    if data.get("TotalSizeOfScannedFilesInMB") is not None:
        out["total_size_of_scanned_files_in_mb"] = float(
            data["TotalSizeOfScannedFilesInMB"]
        )
    if data.get("TotalNumberOfImportedFiles") is not None:
        out["total_number_of_imported_files"] = data["TotalNumberOfImportedFiles"]
    if data.get("TotalNumberOfResourcesScanned") is not None:
        out["total_number_of_resources_scanned"] = data["TotalNumberOfResourcesScanned"]
    if data.get("TotalNumberOfResourcesImported") is not None:
        out["total_number_of_resources_imported"] = data[
            "TotalNumberOfResourcesImported"
        ]
    if data.get("TotalNumberOfResourcesWithCustomerError") is not None:
        out["total_number_of_resources_with_customer_error"] = data[
            "TotalNumberOfResourcesWithCustomerError"
        ]
    if data.get("TotalNumberOfFilesReadWithCustomerError") is not None:
        out["total_number_of_files_read_with_customer_error"] = data[
            "TotalNumberOfFilesReadWithCustomerError"
        ]
    if data.get("TotalNumberOfScannedNonFhirFiles") is not None:
        out["total_number_of_scanned_non_fhir_files"] = data[
            "TotalNumberOfScannedNonFhirFiles"
        ]
    if data.get("TotalSizeOfScannedNonFhirFilesInMB") is not None:
        out["total_size_of_scanned_non_fhir_files_in_mb"] = float(
            data["TotalSizeOfScannedNonFhirFilesInMB"]
        )
    if data.get("TotalNumberOfImportedNonFhirFiles") is not None:
        out["total_number_of_imported_non_fhir_files"] = data[
            "TotalNumberOfImportedNonFhirFiles"
        ]
    if data.get("TotalNumberOfNonFhirResourcesScanned") is not None:
        out["total_number_of_non_fhir_resources_scanned"] = data[
            "TotalNumberOfNonFhirResourcesScanned"
        ]
    if data.get("TotalNumberOfNonFhirResourcesImported") is not None:
        out["total_number_of_non_fhir_resources_imported"] = data[
            "TotalNumberOfNonFhirResourcesImported"
        ]
    if data.get("TotalNumberOfNonFhirResourcesWithCustomerError") is not None:
        out["total_number_of_non_fhir_resources_with_customer_error"] = data[
            "TotalNumberOfNonFhirResourcesWithCustomerError"
        ]
    if data.get("TotalNumberOfNonFhirFilesReadWithCustomerError") is not None:
        out["total_number_of_non_fhir_files_read_with_customer_error"] = data[
            "TotalNumberOfNonFhirFilesReadWithCustomerError"
        ]
    if data.get("Throughput") is not None:
        out["throughput"] = float(data["Throughput"])
    if data.get("TotalFilesConverted") is not None:
        out["total_files_converted"] = data["TotalFilesConverted"]
    if data.get("TotalResourcesGenerated") is not None:
        out["total_resources_generated"] = data["TotalResourcesGenerated"]
    return out
