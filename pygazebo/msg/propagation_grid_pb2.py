# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propagation_grid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import propagation_particle_pb2 as propagation__particle__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='propagation_grid.proto',
  package='gazebo.msgs',
  syntax='proto2',
  options=None,
  serialized_pb=_b('\n\x16propagation_grid.proto\x12\x0bgazebo.msgs\x1a\x1apropagation_particle.proto\"E\n\x0fPropagationGrid\x12\x32\n\x08particle\x18\x01 \x03(\x0b\x32 .gazebo.msgs.PropagationParticle')
  ,
  dependencies=[propagation__particle__pb2.DESCRIPTOR,])




_PROPAGATIONGRID = _descriptor.Descriptor(
  name='PropagationGrid',
  full_name='gazebo.msgs.PropagationGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='particle', full_name='gazebo.msgs.PropagationGrid.particle', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=67,
  serialized_end=136,
)

_PROPAGATIONGRID.fields_by_name['particle'].message_type = propagation__particle__pb2._PROPAGATIONPARTICLE
DESCRIPTOR.message_types_by_name['PropagationGrid'] = _PROPAGATIONGRID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PropagationGrid = _reflection.GeneratedProtocolMessageType('PropagationGrid', (_message.Message,), dict(
  DESCRIPTOR = _PROPAGATIONGRID,
  __module__ = 'propagation_grid_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.PropagationGrid)
  ))
_sym_db.RegisterMessage(PropagationGrid)


# @@protoc_insertion_point(module_scope)
