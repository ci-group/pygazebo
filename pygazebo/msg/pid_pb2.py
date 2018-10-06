# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pid.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\tpid.proto\x12\x0bgazebo.msgs\"\x87\x01\n\x03PID\x12\x11\n\x06target\x18\x01 \x01(\x01:\x01\x30\x12\x11\n\x06p_gain\x18\x02 \x01(\x01:\x01\x30\x12\x11\n\x06i_gain\x18\x03 \x01(\x01:\x01\x30\x12\x11\n\x06\x64_gain\x18\x04 \x01(\x01:\x01\x30\x12\x10\n\x05i_max\x18\x05 \x01(\x01:\x01\x30\x12\x10\n\x05i_min\x18\x06 \x01(\x01:\x01\x30\x12\x10\n\x05limit\x18\x07 \x01(\x01:\x01\x30')
)




_PID = _descriptor.Descriptor(
  name='PID',
  full_name='gazebo.msgs.PID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='gazebo.msgs.PID.target', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_gain', full_name='gazebo.msgs.PID.p_gain', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i_gain', full_name='gazebo.msgs.PID.i_gain', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d_gain', full_name='gazebo.msgs.PID.d_gain', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i_max', full_name='gazebo.msgs.PID.i_max', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i_min', full_name='gazebo.msgs.PID.i_min', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='gazebo.msgs.PID.limit', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['PID'] = _PID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PID = _reflection.GeneratedProtocolMessageType('PID', (_message.Message,), dict(
  DESCRIPTOR = _PID,
  __module__ = 'pid_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PID)
  ))
_sym_db.RegisterMessage(PID)


# @@protoc_insertion_point(module_scope)
