"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class CannedMessageModuleConfig(google.protobuf.message.Message):
    """
    Canned message module configuration.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGES_FIELD_NUMBER: builtins.int
    messages: builtins.str
    """
    Predefined messages for canned message module separated by '|' characters.
    """
    def __init__(
        self,
        *,
        messages: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["messages", b"messages"]) -> None: ...

global___CannedMessageModuleConfig = CannedMessageModuleConfig
