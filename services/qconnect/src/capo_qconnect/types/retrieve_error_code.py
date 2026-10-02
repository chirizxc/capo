"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveErrorCode``."""

from typing import TypeAlias

"""<p>The error code that categorizes a per-association retrieval failure.</p> <ul> <li> <p> <code>ACCESS_DENIED</code> – you do not have permission to retrieve from the knowledge base for the assistant association.</p> </li> <li> <p> <code>RESOURCE_NOT_FOUND</code> – the assistant association or its knowledge base could not be found.</p> </li> <li> <p> <code>VALIDATION_ERROR</code> – the retrieval request or the knowledge base configuration for the assistant association was not valid.</p> </li> <li> <p> <code>THROTTLED</code> – the retrieval request for the assistant association was throttled.</p> </li> <li> <p> <code>DEPENDENCY_FAILED</code> – a dependency required to query the assistant association failed.</p> </li> <li> <p> <code>INTERNAL_SERVER_ERROR</code> – an internal error occurred while querying the assistant association.</p> </li> </ul>"""
RetrieveErrorCode: TypeAlias = str
