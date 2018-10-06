# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vector3d_pb2 as vector3d__pb2
from . import quaternion_pb2 as quaternion__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\npose.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\x1a\x10quaternion.proto\"w\n\x04Pose\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\'\n\x08position\x18\x03 \x02(\x0b\x32\x15.gazebo.msgs.Vector3d\x12,\n\x0borientation\x18\x04 \x02(\x0b\x32\x17.gazebo.msgs.Quaternion')
  ,
  dependencies=[vector3d__pb2.DESCRIPTOR,quaternion__pb2.DESCRIPTOR,])




_POSE = _descriptor.Descriptor(
  name='Pose',
  full_name='gazebo.msgs.Pose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Pose.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='gazebo.msgs.Pose.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='gazebo.msgs.Pose.position', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='gazebo.msgs.Pose.orientation', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=61,
  serialized_end=180,
)

_POSE.fields_by_name['position'].message_type = vector3d__pb2._VECTOR3D
_POSE.fields_by_name['orientation'].message_type = quaternion__pb2._QUATERNION
DESCRIPTOR.message_types_by_name['Pose'] = _POSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pose = _reflection.GeneratedProtocolMessageType('Pose', (_message.Message,), dict(
  DESCRIPTOR = _POSE,
  __module__ = 'pose_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Pose)
  ))
_sym_db.RegisterMessage(Pose)


# @@protoc_insertion_point(module_scope)
