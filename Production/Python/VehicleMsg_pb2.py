# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VehicleMsg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VehicleMsg.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10VehicleMsg.proto\"\xf0\x02\n\nVcuWrapper\x12\"\n\x05\x64rive\x18\x01 \x01(\x0b\x32\x11.VcuWrapper.DriveH\x00\x12\"\n\x05orbit\x18\x02 \x01(\x0b\x32\x11.VcuWrapper.OrbitH\x00\x12 \n\x04halt\x18\x03 \x01(\x0b\x32\x10.VcuWrapper.HaltH\x00\x1a\x1c\n\x04Halt\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x01 \x01(\x01\x1aS\n\x05Orbit\x12\x10\n\x08velocity\x18\x01 \x01(\x01\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x01\x12\x0f\n\x07\x64\x65grees\x18\x04 \x01(\x01\x1a~\n\x05\x44rive\x12\x10\n\x08velocity\x18\x01 \x01(\x01\x12\x11\n\tdirection\x18\x02 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x01\x12\x10\n\x08\x64istance\x18\x04 \x01(\x01\x12\x15\n\redge_distance\x18\x05 \x01(\x01\x12\x11\n\tedge_side\x18\x06 \x01(\tB\x05\n\x03msgB$\n\x16\x63om.addrobots.protobufB\nVehicleMsgb\x06proto3')
)




_VCUWRAPPER_HALT = _descriptor.Descriptor(
  name='Halt',
  full_name='VcuWrapper.Halt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='VcuWrapper.Halt.acceleration', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=169,
)

_VCUWRAPPER_ORBIT = _descriptor.Descriptor(
  name='Orbit',
  full_name='VcuWrapper.Orbit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='velocity', full_name='VcuWrapper.Orbit.velocity', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='VcuWrapper.Orbit.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='VcuWrapper.Orbit.acceleration', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='degrees', full_name='VcuWrapper.Orbit.degrees', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=254,
)

_VCUWRAPPER_DRIVE = _descriptor.Descriptor(
  name='Drive',
  full_name='VcuWrapper.Drive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='velocity', full_name='VcuWrapper.Drive.velocity', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='VcuWrapper.Drive.direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='VcuWrapper.Drive.acceleration', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='VcuWrapper.Drive.distance', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge_distance', full_name='VcuWrapper.Drive.edge_distance', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edge_side', full_name='VcuWrapper.Drive.edge_side', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=382,
)

_VCUWRAPPER = _descriptor.Descriptor(
  name='VcuWrapper',
  full_name='VcuWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drive', full_name='VcuWrapper.drive', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orbit', full_name='VcuWrapper.orbit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='halt', full_name='VcuWrapper.halt', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VCUWRAPPER_HALT, _VCUWRAPPER_ORBIT, _VCUWRAPPER_DRIVE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='msg', full_name='VcuWrapper.msg',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=21,
  serialized_end=389,
)

_VCUWRAPPER_HALT.containing_type = _VCUWRAPPER
_VCUWRAPPER_ORBIT.containing_type = _VCUWRAPPER
_VCUWRAPPER_DRIVE.containing_type = _VCUWRAPPER
_VCUWRAPPER.fields_by_name['drive'].message_type = _VCUWRAPPER_DRIVE
_VCUWRAPPER.fields_by_name['orbit'].message_type = _VCUWRAPPER_ORBIT
_VCUWRAPPER.fields_by_name['halt'].message_type = _VCUWRAPPER_HALT
_VCUWRAPPER.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPER.fields_by_name['drive'])
_VCUWRAPPER.fields_by_name['drive'].containing_oneof = _VCUWRAPPER.oneofs_by_name['msg']
_VCUWRAPPER.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPER.fields_by_name['orbit'])
_VCUWRAPPER.fields_by_name['orbit'].containing_oneof = _VCUWRAPPER.oneofs_by_name['msg']
_VCUWRAPPER.oneofs_by_name['msg'].fields.append(
  _VCUWRAPPER.fields_by_name['halt'])
_VCUWRAPPER.fields_by_name['halt'].containing_oneof = _VCUWRAPPER.oneofs_by_name['msg']
DESCRIPTOR.message_types_by_name['VcuWrapper'] = _VCUWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VcuWrapper = _reflection.GeneratedProtocolMessageType('VcuWrapper', (_message.Message,), dict(

  Halt = _reflection.GeneratedProtocolMessageType('Halt', (_message.Message,), dict(
    DESCRIPTOR = _VCUWRAPPER_HALT,
    __module__ = 'VehicleMsg_pb2'
    # @@protoc_insertion_point(class_scope:VcuWrapper.Halt)
    ))
  ,

  Orbit = _reflection.GeneratedProtocolMessageType('Orbit', (_message.Message,), dict(
    DESCRIPTOR = _VCUWRAPPER_ORBIT,
    __module__ = 'VehicleMsg_pb2'
    # @@protoc_insertion_point(class_scope:VcuWrapper.Orbit)
    ))
  ,

  Drive = _reflection.GeneratedProtocolMessageType('Drive', (_message.Message,), dict(
    DESCRIPTOR = _VCUWRAPPER_DRIVE,
    __module__ = 'VehicleMsg_pb2'
    # @@protoc_insertion_point(class_scope:VcuWrapper.Drive)
    ))
  ,
  DESCRIPTOR = _VCUWRAPPER,
  __module__ = 'VehicleMsg_pb2'
  # @@protoc_insertion_point(class_scope:VcuWrapper)
  ))
_sym_db.RegisterMessage(VcuWrapper)
_sym_db.RegisterMessage(VcuWrapper.Halt)
_sym_db.RegisterMessage(VcuWrapper.Orbit)
_sym_db.RegisterMessage(VcuWrapper.Drive)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.addrobots.protobufB\nVehicleMsg'))
# @@protoc_insertion_point(module_scope)
