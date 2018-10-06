# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: joint_cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pid_pb2 as pid__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='joint_cmd.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x0fjoint_cmd.proto\x12\x0bgazebo.msgs\x1a\tpid.proto\"\x8f\x01\n\x08JointCmd\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x04\x61xis\x18\x02 \x01(\x05:\x01\x30\x12\r\n\x05\x66orce\x18\x03 \x01(\x01\x12\"\n\x08position\x18\x04 \x01(\x0b\x32\x10.gazebo.msgs.PID\x12\"\n\x08velocity\x18\x05 \x01(\x0b\x32\x10.gazebo.msgs.PID\x12\r\n\x05reset\x18\x06 \x01(\x08')
  ,
  dependencies=[pid__pb2.DESCRIPTOR,])




_JOINTCMD = _descriptor.Descriptor(
  name='JointCmd',
  full_name='gazebo.msgs.JointCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.JointCmd.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='axis', full_name='gazebo.msgs.JointCmd.axis', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='gazebo.msgs.JointCmd.force', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='gazebo.msgs.JointCmd.position', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='gazebo.msgs.JointCmd.velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset', full_name='gazebo.msgs.JointCmd.reset', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=44,
  serialized_end=187,
)

_JOINTCMD.fields_by_name['position'].message_type = pid__pb2._PID
_JOINTCMD.fields_by_name['velocity'].message_type = pid__pb2._PID
DESCRIPTOR.message_types_by_name['JointCmd'] = _JOINTCMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JointCmd = _reflection.GeneratedProtocolMessageType('JointCmd', (_message.Message,), dict(
  DESCRIPTOR = _JOINTCMD,
  __module__ = 'joint_cmd_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.JointCmd)
  ))
_sym_db.RegisterMessage(JointCmd)


# @@protoc_insertion_point(module_scope)
