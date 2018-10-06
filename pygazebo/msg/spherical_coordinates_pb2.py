# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spherical_coordinates.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spherical_coordinates.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x1bspherical_coordinates.proto\x12\x0bgazebo.msgs\"\xd3\x01\n\x14SphericalCoordinates\x12\x45\n\rsurface_model\x18\x01 \x02(\x0e\x32..gazebo.msgs.SphericalCoordinates.SurfaceModel\x12\x14\n\x0clatitude_deg\x18\x02 \x02(\x01\x12\x15\n\rlongitude_deg\x18\x03 \x02(\x01\x12\x11\n\televation\x18\x04 \x02(\x01\x12\x13\n\x0bheading_deg\x18\x05 \x02(\x01\"\x1f\n\x0cSurfaceModel\x12\x0f\n\x0b\x45\x41RTH_WGS84\x10\x01')
)



_SPHERICALCOORDINATES_SURFACEMODEL = _descriptor.EnumDescriptor(
  name='SurfaceModel',
  full_name='gazebo.msgs.SphericalCoordinates.SurfaceModel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EARTH_WGS84', index=0, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=225,
  serialized_end=256,
)
_sym_db.RegisterEnumDescriptor(_SPHERICALCOORDINATES_SURFACEMODEL)


_SPHERICALCOORDINATES = _descriptor.Descriptor(
  name='SphericalCoordinates',
  full_name='gazebo.msgs.SphericalCoordinates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='surface_model', full_name='gazebo.msgs.SphericalCoordinates.surface_model', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='gazebo.msgs.SphericalCoordinates.latitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='gazebo.msgs.SphericalCoordinates.longitude_deg', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='gazebo.msgs.SphericalCoordinates.elevation', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading_deg', full_name='gazebo.msgs.SphericalCoordinates.heading_deg', index=4,
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
    _SPHERICALCOORDINATES_SURFACEMODEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=256,
)

_SPHERICALCOORDINATES.fields_by_name['surface_model'].enum_type = _SPHERICALCOORDINATES_SURFACEMODEL
_SPHERICALCOORDINATES_SURFACEMODEL.containing_type = _SPHERICALCOORDINATES
DESCRIPTOR.message_types_by_name['SphericalCoordinates'] = _SPHERICALCOORDINATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SphericalCoordinates = _reflection.GeneratedProtocolMessageType('SphericalCoordinates', (_message.Message,), dict(
  DESCRIPTOR = _SPHERICALCOORDINATES,
  __module__ = 'spherical_coordinates_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.SphericalCoordinates)
  ))
_sym_db.RegisterMessage(SphericalCoordinates)


# @@protoc_insertion_point(module_scope)
