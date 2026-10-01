"""Generated from Smithy shape ``com.amazonaws.inspector2#InheritanceMode``."""

from typing import TypeAlias

"""<p>The inheritance behavior for a scan-type configuration. Used with <code>UpdateConfigurationInheritance</code> to reset a member account's configuration to inherit from the delegated administrator. The only valid value is <code>INHERIT_FROM_ADMIN</code>, which resets the member account's configuration so that it inherits scan settings from the delegated administrator.</p>"""
InheritanceMode: TypeAlias = str
