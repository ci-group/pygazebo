# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sonar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pose_pb2 as pose__pb2
from . import vector3d_pb2 as vector3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sonar.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x0bsonar.proto\x12\x0bgazebo.msgs\x1a\npose.proto\x1a\x0evector3d.proto\"\xaa\x01\n\x05Sonar\x12\r\n\x05\x66rame\x18\x01 \x02(\t\x12%\n\nworld_pose\x18\x02 \x02(\x0b\x32\x11.gazebo.msgs.Pose\x12\x11\n\trange_min\x18\x03 \x02(\x01\x12\x11\n\trange_max\x18\x04 \x02(\x01\x12\x0e\n\x06radius\x18\x05 \x02(\x01\x12\r\n\x05range\x18\x06 \x02(\x01\x12&\n\x07\x63ontact\x18\x07 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d')
  ,
  dependencies=[pose__pb2.DESCRIPTOR,vector3d__pb2.DESCRIPTOR,])




_SONAR = _descriptor.Descriptor(
  name='Sonar',
  full_name='gazebo.msgs.Sonar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='gazebo.msgs.Sonar.frame', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='world_pose', full_name='gazebo.msgs.Sonar.world_pose', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='gazebo.msgs.Sonar.range_min', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='gazebo.msgs.Sonar.range_max', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='gazebo.msgs.Sonar.radius', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='gazebo.msgs.Sonar.range', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contact', full_name='gazebo.msgs.Sonar.contact', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=57,
  serialized_end=227,
)

_SONAR.fields_by_name['world_pose'].message_type = pose__pb2._POSE
_SONAR.fields_by_name['contact'].message_type = vector3d__pb2._VECTOR3D
DESCRIPTOR.message_types_by_name['Sonar'] = _SONAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sonar = _reflection.GeneratedProtocolMessageType('Sonar', (_message.Message,), dict(
  DESCRIPTOR = _SONAR,
  __module__ = 'sonar_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Sonar)
  ))
_sym_db.RegisterMessage(Sonar)


# @@protoc_insertion_point(module_scope)
