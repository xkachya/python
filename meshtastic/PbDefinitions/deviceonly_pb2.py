# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/deviceonly.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic.PbDefinitions import channel_pb2 as meshtastic_dot_channel__pb2
from meshtastic.PbDefinitions import localonly_pb2 as meshtastic_dot_localonly__pb2
from meshtastic.PbDefinitions import mesh_pb2 as meshtastic_dot_mesh__pb2
from meshtastic.PbDefinitions import telemetry_pb2 as meshtastic_dot_telemetry__pb2
from meshtastic.PbDefinitions import module_config_pb2 as meshtastic_dot_module__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmeshtastic/deviceonly.proto\x12\nmeshtastic\x1a\x18meshtastic/channel.proto\x1a\x1ameshtastic/localonly.proto\x1a\x15meshtastic/mesh.proto\x1a\x1ameshtastic/telemetry.proto\x1a\x1emeshtastic/module_config.proto\"\x93\x03\n\x0b\x44\x65viceState\x12\'\n\x07my_node\x18\x02 \x01(\x0b\x32\x16.meshtastic.MyNodeInfo\x12\x1f\n\x05owner\x18\x03 \x01(\x0b\x32\x10.meshtastic.User\x12-\n\rreceive_queue\x18\x05 \x03(\x0b\x32\x16.meshtastic.MeshPacket\x12\x0f\n\x07version\x18\x08 \x01(\r\x12/\n\x0frx_text_message\x18\x07 \x01(\x0b\x32\x16.meshtastic.MeshPacket\x12\x0f\n\x07no_save\x18\t \x01(\x08\x12\x15\n\rdid_gps_reset\x18\x0b \x01(\x08\x12+\n\x0brx_waypoint\x18\x0c \x01(\x0b\x32\x16.meshtastic.MeshPacket\x12\x44\n\x19node_remote_hardware_pins\x18\r \x03(\x0b\x32!.meshtastic.NodeRemoteHardwarePin\x12.\n\x0cnode_db_lite\x18\x0e \x03(\x0b\x32\x18.meshtastic.NodeInfoLite\"\xcc\x01\n\x0cNodeInfoLite\x12\x0b\n\x03num\x18\x01 \x01(\r\x12\x1e\n\x04user\x18\x02 \x01(\x0b\x32\x10.meshtastic.User\x12*\n\x08position\x18\x03 \x01(\x0b\x32\x18.meshtastic.PositionLite\x12\x0b\n\x03snr\x18\x04 \x01(\x02\x12\x12\n\nlast_heard\x18\x05 \x01(\x07\x12\x31\n\x0e\x64\x65vice_metrics\x18\x06 \x01(\x0b\x32\x19.meshtastic.DeviceMetrics\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\r\"\x90\x01\n\x0cPositionLite\x12\x12\n\nlatitude_i\x18\x01 \x01(\x0f\x12\x13\n\x0blongitude_i\x18\x02 \x01(\x0f\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x07\x12\x37\n\x0flocation_source\x18\x05 \x01(\x0e\x32\x1e.meshtastic.Position.LocSource\"E\n\x0b\x43hannelFile\x12%\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x13.meshtastic.Channel\x12\x0f\n\x07version\x18\x02 \x01(\r\"\x97\x02\n\x08OEMStore\x12\x16\n\x0eoem_icon_width\x18\x01 \x01(\r\x12\x17\n\x0foem_icon_height\x18\x02 \x01(\r\x12\x15\n\roem_icon_bits\x18\x03 \x01(\x0c\x12)\n\x08oem_font\x18\x04 \x01(\x0e\x32\x17.meshtastic.ScreenFonts\x12\x10\n\x08oem_text\x18\x05 \x01(\t\x12\x13\n\x0boem_aes_key\x18\x06 \x01(\x0c\x12\x31\n\x10oem_local_config\x18\x07 \x01(\x0b\x32\x17.meshtastic.LocalConfig\x12>\n\x17oem_local_module_config\x18\x08 \x01(\x0b\x32\x1d.meshtastic.LocalModuleConfig\"U\n\x15NodeRemoteHardwarePin\x12\x10\n\x08node_num\x18\x01 \x01(\r\x12*\n\x03pin\x18\x02 \x01(\x0b\x32\x1d.meshtastic.RemoteHardwarePin*>\n\x0bScreenFonts\x12\x0e\n\nFONT_SMALL\x10\x00\x12\x0f\n\x0b\x46ONT_MEDIUM\x10\x01\x12\x0e\n\nFONT_LARGE\x10\x02\x42_\n\x13\x63om.geeksville.meshB\nDeviceOnlyZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.deviceonly_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nDeviceOnlyZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _SCREENFONTS._serialized_start=1380
  _SCREENFONTS._serialized_end=1442
  _DEVICESTATE._serialized_start=181
  _DEVICESTATE._serialized_end=584
  _NODEINFOLITE._serialized_start=587
  _NODEINFOLITE._serialized_end=791
  _POSITIONLITE._serialized_start=794
  _POSITIONLITE._serialized_end=938
  _CHANNELFILE._serialized_start=940
  _CHANNELFILE._serialized_end=1009
  _OEMSTORE._serialized_start=1012
  _OEMSTORE._serialized_end=1291
  _NODEREMOTEHARDWAREPIN._serialized_start=1293
  _NODEREMOTEHARDWAREPIN._serialized_end=1378
# @@protoc_insertion_point(module_scope)