# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quaternion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='quaternion.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x10quaternion.proto\x12\x0bgazebo.msgs\"8\n\nQuaternion\x12\t\n\x01x\x18\x02 \x02(\x01\x12\t\n\x01y\x18\x03 \x02(\x01\x12\t\n\x01z\x18\x04 \x02(\x01\x12\t\n\x01w\x18\x05 \x02(\x01')
)




_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='gazebo.msgs.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='gazebo.msgs.Quaternion.x', index=0,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='gazebo.msgs.Quaternion.y', index=1,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='gazebo.msgs.Quaternion.z', index=2,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='gazebo.msgs.Quaternion.w', index=3,
      number=5, type=1, cpp_type=5, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'quaternion_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)


# @@protoc_insertion_point(module_scope)
