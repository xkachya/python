# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/connection_status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"meshtastic/connection_status.proto\x12\nmeshtastic\"\xb1\x02\n\x16\x44\x65viceConnectionStatus\x12\x33\n\x04wifi\x18\x01 \x01(\x0b\x32 .meshtastic.WifiConnectionStatusH\x00\x88\x01\x01\x12;\n\x08\x65thernet\x18\x02 \x01(\x0b\x32$.meshtastic.EthernetConnectionStatusH\x01\x88\x01\x01\x12=\n\tbluetooth\x18\x03 \x01(\x0b\x32%.meshtastic.BluetoothConnectionStatusH\x02\x88\x01\x01\x12\x37\n\x06serial\x18\x04 \x01(\x0b\x32\".meshtastic.SerialConnectionStatusH\x03\x88\x01\x01\x42\x07\n\x05_wifiB\x0b\n\t_ethernetB\x0c\n\n_bluetoothB\t\n\x07_serial\"g\n\x14WifiConnectionStatus\x12\x33\n\x06status\x18\x01 \x01(\x0b\x32#.meshtastic.NetworkConnectionStatus\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\x0c\n\x04rssi\x18\x03 \x01(\x05\"O\n\x18\x45thernetConnectionStatus\x12\x33\n\x06status\x18\x01 \x01(\x0b\x32#.meshtastic.NetworkConnectionStatus\"{\n\x17NetworkConnectionStatus\x12\x12\n\nip_address\x18\x01 \x01(\x07\x12\x14\n\x0cis_connected\x18\x02 \x01(\x08\x12\x19\n\x11is_mqtt_connected\x18\x03 \x01(\x08\x12\x1b\n\x13is_syslog_connected\x18\x04 \x01(\x08\"L\n\x19\x42luetoothConnectionStatus\x12\x0b\n\x03pin\x18\x01 \x01(\r\x12\x0c\n\x04rssi\x18\x02 \x01(\x05\x12\x14\n\x0cis_connected\x18\x03 \x01(\x08\"<\n\x16SerialConnectionStatus\x12\x0c\n\x04\x62\x61ud\x18\x01 \x01(\r\x12\x14\n\x0cis_connected\x18\x02 \x01(\x08\x42\x65\n\x13\x63om.geeksville.meshB\x10\x43onnStatusProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.connection_status_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\020ConnStatusProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _DEVICECONNECTIONSTATUS._serialized_start=51
  _DEVICECONNECTIONSTATUS._serialized_end=356
  _WIFICONNECTIONSTATUS._serialized_start=358
  _WIFICONNECTIONSTATUS._serialized_end=461
  _ETHERNETCONNECTIONSTATUS._serialized_start=463
  _ETHERNETCONNECTIONSTATUS._serialized_end=542
  _NETWORKCONNECTIONSTATUS._serialized_start=544
  _NETWORKCONNECTIONSTATUS._serialized_end=667
  _BLUETOOTHCONNECTIONSTATUS._serialized_start=669
  _BLUETOOTHCONNECTIONSTATUS._serialized_end=745
  _SERIALCONNECTIONSTATUS._serialized_start=747
  _SERIALCONNECTIONSTATUS._serialized_end=807
# @@protoc_insertion_point(module_scope)