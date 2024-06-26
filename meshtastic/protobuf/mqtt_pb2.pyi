"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import meshtastic.protobuf.config_pb2
import meshtastic.protobuf.mesh_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ServiceEnvelope(google.protobuf.message.Message):
    """
    This message wraps a MeshPacket with extra metadata about the sender and how it arrived.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PACKET_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    channel_id: builtins.str
    """
    The global channel ID it was sent on
    """
    gateway_id: builtins.str
    """
    The sending gateway node ID. Can we use this to authenticate/prevent fake
    nodeid impersonation for senders? - i.e. use gateway/mesh id (which is authenticated) + local node id as
    the globally trusted nodenum
    """
    @property
    def packet(self) -> meshtastic.protobuf.mesh_pb2.MeshPacket:
        """
        The (probably encrypted) packet
        """

    def __init__(
        self,
        *,
        packet: meshtastic.protobuf.mesh_pb2.MeshPacket | None = ...,
        channel_id: builtins.str = ...,
        gateway_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["packet", b"packet"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["channel_id", b"channel_id", "gateway_id", b"gateway_id", "packet", b"packet"]) -> None: ...

global___ServiceEnvelope = ServiceEnvelope

@typing.final
class MapReport(google.protobuf.message.Message):
    """
    Information about a node intended to be reported unencrypted to a map using MQTT.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LONG_NAME_FIELD_NUMBER: builtins.int
    SHORT_NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    HW_MODEL_FIELD_NUMBER: builtins.int
    FIRMWARE_VERSION_FIELD_NUMBER: builtins.int
    REGION_FIELD_NUMBER: builtins.int
    MODEM_PRESET_FIELD_NUMBER: builtins.int
    HAS_DEFAULT_CHANNEL_FIELD_NUMBER: builtins.int
    LATITUDE_I_FIELD_NUMBER: builtins.int
    LONGITUDE_I_FIELD_NUMBER: builtins.int
    ALTITUDE_FIELD_NUMBER: builtins.int
    POSITION_PRECISION_FIELD_NUMBER: builtins.int
    NUM_ONLINE_LOCAL_NODES_FIELD_NUMBER: builtins.int
    long_name: builtins.str
    """
    A full name for this user, i.e. "Kevin Hester"
    """
    short_name: builtins.str
    """
    A VERY short name, ideally two characters.
    Suitable for a tiny OLED screen
    """
    role: meshtastic.protobuf.config_pb2.Config.DeviceConfig.Role.ValueType
    """
    Role of the node that applies specific settings for a particular use-case
    """
    hw_model: meshtastic.protobuf.mesh_pb2.HardwareModel.ValueType
    """
    Hardware model of the node, i.e. T-Beam, Heltec V3, etc...
    """
    firmware_version: builtins.str
    """
    Device firmware version string
    """
    region: meshtastic.protobuf.config_pb2.Config.LoRaConfig.RegionCode.ValueType
    """
    The region code for the radio (US, CN, EU433, etc...)
    """
    modem_preset: meshtastic.protobuf.config_pb2.Config.LoRaConfig.ModemPreset.ValueType
    """
    Modem preset used by the radio (LongFast, MediumSlow, etc...)
    """
    has_default_channel: builtins.bool
    """
    Whether the node has a channel with default PSK and name (LongFast, MediumSlow, etc...)
    and it uses the default frequency slot given the region and modem preset.
    """
    latitude_i: builtins.int
    """
    Latitude: multiply by 1e-7 to get degrees in floating point
    """
    longitude_i: builtins.int
    """
    Longitude: multiply by 1e-7 to get degrees in floating point
    """
    altitude: builtins.int
    """
    Altitude in meters above MSL
    """
    position_precision: builtins.int
    """
    Indicates the bits of precision for latitude and longitude set by the sending node
    """
    num_online_local_nodes: builtins.int
    """
    Number of online nodes (heard in the last 2 hours) this node has in its list that were received locally (not via MQTT)
    """
    def __init__(
        self,
        *,
        long_name: builtins.str = ...,
        short_name: builtins.str = ...,
        role: meshtastic.protobuf.config_pb2.Config.DeviceConfig.Role.ValueType = ...,
        hw_model: meshtastic.protobuf.mesh_pb2.HardwareModel.ValueType = ...,
        firmware_version: builtins.str = ...,
        region: meshtastic.protobuf.config_pb2.Config.LoRaConfig.RegionCode.ValueType = ...,
        modem_preset: meshtastic.protobuf.config_pb2.Config.LoRaConfig.ModemPreset.ValueType = ...,
        has_default_channel: builtins.bool = ...,
        latitude_i: builtins.int = ...,
        longitude_i: builtins.int = ...,
        altitude: builtins.int = ...,
        position_precision: builtins.int = ...,
        num_online_local_nodes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["altitude", b"altitude", "firmware_version", b"firmware_version", "has_default_channel", b"has_default_channel", "hw_model", b"hw_model", "latitude_i", b"latitude_i", "long_name", b"long_name", "longitude_i", b"longitude_i", "modem_preset", b"modem_preset", "num_online_local_nodes", b"num_online_local_nodes", "position_precision", b"position_precision", "region", b"region", "role", b"role", "short_name", b"short_name"]) -> None: ...

global___MapReport = MapReport
