# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: planegeom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vector3d_pb2 as vector3d__pb2
from . import vector2d_pb2 as vector2d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='planegeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x0fplanegeom.proto\x12\x0bgazebo.msgs\x1a\x0evector3d.proto\x1a\x0evector2d.proto\"e\n\tPlaneGeom\x12%\n\x06normal\x18\x01 \x02(\x0b\x32\x15.gazebo.msgs.Vector3d\x12#\n\x04size\x18\x02 \x02(\x0b\x32\x15.gazebo.msgs.Vector2d\x12\x0c\n\x01\x64\x18\x03 \x01(\x01:\x01\x30')
  ,
  dependencies=[vector3d__pb2.DESCRIPTOR,vector2d__pb2.DESCRIPTOR,])




_PLANEGEOM = _descriptor.Descriptor(
  name='PlaneGeom',
  full_name='gazebo.msgs.PlaneGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='normal', full_name='gazebo.msgs.PlaneGeom.normal', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='gazebo.msgs.PlaneGeom.size', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='gazebo.msgs.PlaneGeom.d', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=64,
  serialized_end=165,
)

_PLANEGEOM.fields_by_name['normal'].message_type = vector3d__pb2._VECTOR3D
_PLANEGEOM.fields_by_name['size'].message_type = vector2d__pb2._VECTOR2D
DESCRIPTOR.message_types_by_name['PlaneGeom'] = _PLANEGEOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlaneGeom = _reflection.GeneratedProtocolMessageType('PlaneGeom', (_message.Message,), dict(
  DESCRIPTOR = _PLANEGEOM,
  __module__ = 'planegeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PlaneGeom)
  ))
_sym_db.RegisterMessage(PlaneGeom)


# @@protoc_insertion_point(module_scope)
