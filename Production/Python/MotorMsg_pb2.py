# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MotorMsg.proto

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
  name='MotorMsg.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eMotorMsg.proto\"\x94\n\n\nMcuWrapper\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12+\n\nmotor_data\x18\x02 \x01(\x0b\x32\x15.McuWrapper.MotorDataH\x00\x12)\n\tmotor_cmd\x18\x03 \x01(\x0b\x32\x14.McuWrapper.MotorCmdH\x00\x1a\xcb\x03\n\tMotorData\x12\x30\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32 .McuWrapper.MotorData.DataAction\x12/\n\x06params\x18\x02 \x03(\x0b\x32\x1f.McuWrapper.MotorData.DataParam\x1a\xa3\x02\n\tDataParam\x12\x37\n\x02id\x18\x01 \x01(\x0e\x32+.McuWrapper.MotorData.DataParam.MotorDataId\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x1e\n\x04unit\x18\x03 \x01(\x0e\x32\x10.McuWrapper.Unit\"\xad\x01\n\x0bMotorDataId\x12\x0e\n\nUNKNOWN_ID\x10\x00\x12\x08\n\x04UUID\x10\x01\x12\x0b\n\x07VERSION\x10\x02\x12\x15\n\x11MFG_DATE_YYYYMMDD\x10\x03\x12\n\n\x06MFG_ID\x10\x04\x12\x0c\n\x08MODEL_ID\x10\x05\x12\x0e\n\nSTEP_COUNT\x10\x06\x12\x0e\n\nINDUCTANCE\x10\x08\x12\x0b\n\x07\x43UR_POS\x10\x0c\x12\x0b\n\x07\x43UR_AMP\x10\r\x12\x0c\n\x08\x43UR_VOLT\x10\x0e\"5\n\nDataAction\x12\x12\n\x0eUKNONWN_ACTION\x10\x00\x12\x07\n\x03GET\x10\x01\x12\n\n\x06RESULT\x10\x02\x1a\xb6\x04\n\x08MotorCmd\x12\x30\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32 .McuWrapper.MotorCmd.MotorAction\x12-\n\x06params\x18\x02 \x03(\x0b\x32\x1d.McuWrapper.MotorCmd.CmdParam\x1a\xfb\x02\n\x08\x43mdParam\x12\x39\n\x02id\x18\x01 \x01(\x0e\x32-.McuWrapper.MotorCmd.CmdParam.MotorCmdParamId\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x1e\n\x04unit\x18\x03 \x01(\x0e\x32\x10.McuWrapper.Unit\"\x84\x02\n\x0fMotorCmdParamId\x12\x11\n\rUNKNOWN_PARAM\x10\x00\x12\r\n\tCLOCKWISE\x10\x01\x12\x0c\n\x08POSITION\x10\x02\x12\x0c\n\x08VELOCITY\x10\x03\x12\t\n\x05\x41\x43\x43\x45L\x10\x04\x12\x0f\n\x0bHOLD_TORQUE\x10\x05\x12\r\n\tBREAKAWAY\x10\x06\x12\x15\n\x11MIN_CURRENT_LIMIT\x10\x07\x12\x15\n\x11MAX_CURRENT_LIMIT\x10\x08\x12\x15\n\x11MIN_VOLT_VELOCITY\x10\t\x12\x15\n\x11MAX_VOLT_VELOCITY\x10\n\x12\x15\n\x11MIN_VOLTAGE_LIMIT\x10\x0b\x12\x15\n\x11MAX_VOLTAGE_LIMIT\x10\x0c\"K\n\x0bMotorAction\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x42RAKE\x10\x01\x12\r\n\tFREEWHEEL\x10\x02\x12\x07\n\x03RUN\x10\x03\x12\x0c\n\x08GOTO_POS\x10\x04\"\x8d\x01\n\x04Unit\x12\x10\n\x0cUNKNOWN_UNIT\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x12\n\n\x06SECOND\x10\x05\x12\n\n\x06\x44\x45GREE\x10\x06\x12\x07\n\x03\x41MP\x10\x07\x12\x08\n\x04VOLT\x10\x08\x12\n\n\x06NEWTON\x10\t\x12\n\n\x06UHENRY\x10\nB\t\n\x07\x63ontentB\"\n\x16\x63om.addrobots.protobufB\x08MotorMsgb\x06proto3')
)



_MCUWRAPPER_MOTORDATA_DATAPARAM_MOTORDATAID = _descriptor.EnumDescriptor(
  name='MotorDataId',
  full_name='McuWrapper.MotorData.DataParam.MotorDataId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UUID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MFG_DATE_YYYYMMDD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MFG_ID', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MODEL_ID', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STEP_COUNT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDUCTANCE', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUR_POS', index=8, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUR_AMP', index=9, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUR_VOLT', index=10, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=367,
  serialized_end=540,
)
_sym_db.RegisterEnumDescriptor(_MCUWRAPPER_MOTORDATA_DATAPARAM_MOTORDATAID)

_MCUWRAPPER_MOTORDATA_DATAACTION = _descriptor.EnumDescriptor(
  name='DataAction',
  full_name='McuWrapper.MotorData.DataAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UKNONWN_ACTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=542,
  serialized_end=595,
)
_sym_db.RegisterEnumDescriptor(_MCUWRAPPER_MOTORDATA_DATAACTION)

_MCUWRAPPER_MOTORCMD_CMDPARAM_MOTORCMDPARAMID = _descriptor.EnumDescriptor(
  name='MotorCmdParamId',
  full_name='McuWrapper.MotorCmd.CmdParam.MotorCmdParamId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PARAM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOCKWISE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VELOCITY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCEL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLD_TORQUE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREAKAWAY', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_CURRENT_LIMIT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_CURRENT_LIMIT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_VOLT_VELOCITY', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_VOLT_VELOCITY', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_VOLTAGE_LIMIT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_VOLTAGE_LIMIT', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=827,
  serialized_end=1087,
)
_sym_db.RegisterEnumDescriptor(_MCUWRAPPER_MOTORCMD_CMDPARAM_MOTORCMDPARAMID)

_MCUWRAPPER_MOTORCMD_MOTORACTION = _descriptor.EnumDescriptor(
  name='MotorAction',
  full_name='McuWrapper.MotorCmd.MotorAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BRAKE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FREEWHEEL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUN', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOTO_POS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1089,
  serialized_end=1164,
)
_sym_db.RegisterEnumDescriptor(_MCUWRAPPER_MOTORCMD_MOTORACTION)

_MCUWRAPPER_UNIT = _descriptor.EnumDescriptor(
  name='Unit',
  full_name='McuWrapper.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTEGER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECOND', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEGREE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEWTON', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UHENRY', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1167,
  serialized_end=1308,
)
_sym_db.RegisterEnumDescriptor(_MCUWRAPPER_UNIT)


_MCUWRAPPER_MOTORDATA_DATAPARAM = _descriptor.Descriptor(
  name='DataParam',
  full_name='McuWrapper.MotorData.DataParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='McuWrapper.MotorData.DataParam.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='McuWrapper.MotorData.DataParam.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='McuWrapper.MotorData.DataParam.unit', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MCUWRAPPER_MOTORDATA_DATAPARAM_MOTORDATAID,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=540,
)

_MCUWRAPPER_MOTORDATA = _descriptor.Descriptor(
  name='MotorData',
  full_name='McuWrapper.MotorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='McuWrapper.MotorData.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='McuWrapper.MotorData.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MCUWRAPPER_MOTORDATA_DATAPARAM, ],
  enum_types=[
    _MCUWRAPPER_MOTORDATA_DATAACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=595,
)

_MCUWRAPPER_MOTORCMD_CMDPARAM = _descriptor.Descriptor(
  name='CmdParam',
  full_name='McuWrapper.MotorCmd.CmdParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='McuWrapper.MotorCmd.CmdParam.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='McuWrapper.MotorCmd.CmdParam.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='McuWrapper.MotorCmd.CmdParam.unit', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MCUWRAPPER_MOTORCMD_CMDPARAM_MOTORCMDPARAMID,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=708,
  serialized_end=1087,
)

_MCUWRAPPER_MOTORCMD = _descriptor.Descriptor(
  name='MotorCmd',
  full_name='McuWrapper.MotorCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='McuWrapper.MotorCmd.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='McuWrapper.MotorCmd.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MCUWRAPPER_MOTORCMD_CMDPARAM, ],
  enum_types=[
    _MCUWRAPPER_MOTORCMD_MOTORACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=598,
  serialized_end=1164,
)

_MCUWRAPPER = _descriptor.Descriptor(
  name='McuWrapper',
  full_name='McuWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='McuWrapper.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motor_data', full_name='McuWrapper.motor_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motor_cmd', full_name='McuWrapper.motor_cmd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MCUWRAPPER_MOTORDATA, _MCUWRAPPER_MOTORCMD, ],
  enum_types=[
    _MCUWRAPPER_UNIT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='McuWrapper.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=19,
  serialized_end=1319,
)

_MCUWRAPPER_MOTORDATA_DATAPARAM.fields_by_name['id'].enum_type = _MCUWRAPPER_MOTORDATA_DATAPARAM_MOTORDATAID
_MCUWRAPPER_MOTORDATA_DATAPARAM.fields_by_name['unit'].enum_type = _MCUWRAPPER_UNIT
_MCUWRAPPER_MOTORDATA_DATAPARAM.containing_type = _MCUWRAPPER_MOTORDATA
_MCUWRAPPER_MOTORDATA_DATAPARAM_MOTORDATAID.containing_type = _MCUWRAPPER_MOTORDATA_DATAPARAM
_MCUWRAPPER_MOTORDATA.fields_by_name['action'].enum_type = _MCUWRAPPER_MOTORDATA_DATAACTION
_MCUWRAPPER_MOTORDATA.fields_by_name['params'].message_type = _MCUWRAPPER_MOTORDATA_DATAPARAM
_MCUWRAPPER_MOTORDATA.containing_type = _MCUWRAPPER
_MCUWRAPPER_MOTORDATA_DATAACTION.containing_type = _MCUWRAPPER_MOTORDATA
_MCUWRAPPER_MOTORCMD_CMDPARAM.fields_by_name['id'].enum_type = _MCUWRAPPER_MOTORCMD_CMDPARAM_MOTORCMDPARAMID
_MCUWRAPPER_MOTORCMD_CMDPARAM.fields_by_name['unit'].enum_type = _MCUWRAPPER_UNIT
_MCUWRAPPER_MOTORCMD_CMDPARAM.containing_type = _MCUWRAPPER_MOTORCMD
_MCUWRAPPER_MOTORCMD_CMDPARAM_MOTORCMDPARAMID.containing_type = _MCUWRAPPER_MOTORCMD_CMDPARAM
_MCUWRAPPER_MOTORCMD.fields_by_name['action'].enum_type = _MCUWRAPPER_MOTORCMD_MOTORACTION
_MCUWRAPPER_MOTORCMD.fields_by_name['params'].message_type = _MCUWRAPPER_MOTORCMD_CMDPARAM
_MCUWRAPPER_MOTORCMD.containing_type = _MCUWRAPPER
_MCUWRAPPER_MOTORCMD_MOTORACTION.containing_type = _MCUWRAPPER_MOTORCMD
_MCUWRAPPER.fields_by_name['motor_data'].message_type = _MCUWRAPPER_MOTORDATA
_MCUWRAPPER.fields_by_name['motor_cmd'].message_type = _MCUWRAPPER_MOTORCMD
_MCUWRAPPER_UNIT.containing_type = _MCUWRAPPER
_MCUWRAPPER.oneofs_by_name['content'].fields.append(
  _MCUWRAPPER.fields_by_name['motor_data'])
_MCUWRAPPER.fields_by_name['motor_data'].containing_oneof = _MCUWRAPPER.oneofs_by_name['content']
_MCUWRAPPER.oneofs_by_name['content'].fields.append(
  _MCUWRAPPER.fields_by_name['motor_cmd'])
_MCUWRAPPER.fields_by_name['motor_cmd'].containing_oneof = _MCUWRAPPER.oneofs_by_name['content']
DESCRIPTOR.message_types_by_name['McuWrapper'] = _MCUWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

McuWrapper = _reflection.GeneratedProtocolMessageType('McuWrapper', (_message.Message,), dict(

  MotorData = _reflection.GeneratedProtocolMessageType('MotorData', (_message.Message,), dict(

    DataParam = _reflection.GeneratedProtocolMessageType('DataParam', (_message.Message,), dict(
      DESCRIPTOR = _MCUWRAPPER_MOTORDATA_DATAPARAM,
      __module__ = 'MotorMsg_pb2'
      # @@protoc_insertion_point(class_scope:McuWrapper.MotorData.DataParam)
      ))
    ,
    DESCRIPTOR = _MCUWRAPPER_MOTORDATA,
    __module__ = 'MotorMsg_pb2'
    # @@protoc_insertion_point(class_scope:McuWrapper.MotorData)
    ))
  ,

  MotorCmd = _reflection.GeneratedProtocolMessageType('MotorCmd', (_message.Message,), dict(

    CmdParam = _reflection.GeneratedProtocolMessageType('CmdParam', (_message.Message,), dict(
      DESCRIPTOR = _MCUWRAPPER_MOTORCMD_CMDPARAM,
      __module__ = 'MotorMsg_pb2'
      # @@protoc_insertion_point(class_scope:McuWrapper.MotorCmd.CmdParam)
      ))
    ,
    DESCRIPTOR = _MCUWRAPPER_MOTORCMD,
    __module__ = 'MotorMsg_pb2'
    # @@protoc_insertion_point(class_scope:McuWrapper.MotorCmd)
    ))
  ,
  DESCRIPTOR = _MCUWRAPPER,
  __module__ = 'MotorMsg_pb2'
  # @@protoc_insertion_point(class_scope:McuWrapper)
  ))
_sym_db.RegisterMessage(McuWrapper)
_sym_db.RegisterMessage(McuWrapper.MotorData)
_sym_db.RegisterMessage(McuWrapper.MotorData.DataParam)
_sym_db.RegisterMessage(McuWrapper.MotorCmd)
_sym_db.RegisterMessage(McuWrapper.MotorCmd.CmdParam)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026com.addrobots.protobufB\010MotorMsg'))
# @@protoc_insertion_point(module_scope)
