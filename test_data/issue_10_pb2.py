# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: issue_10.proto

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
  name='issue_10.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0eissue_10.proto\"^\n\x0bSomeRequest\x12(\n\tshipments\x18\x01 \x03(\x0b\x32\x15.SomeRequest.Shipment\x1a%\n\x08Shipment\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"h\n\x10SomeOtherRequest\x12-\n\tshipments\x18\x01 \x03(\x0b\x32\x1a.SomeOtherRequest.Shipment\x1a%\n\x08Shipment\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x18\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t2W\n\x04\x43\x61lc\x12!\n\x04\x43\x61lc\x12\x0c.SomeRequest\x1a\t.Response\"\x00\x12,\n\nSingleCalc\x12\x11.SomeOtherRequest\x1a\t.Response\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SOMEREQUEST_SHIPMENT = _descriptor.Descriptor(
  name='Shipment',
  full_name='SomeRequest.Shipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SomeRequest.Shipment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SomeRequest.Shipment.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=75,
  serialized_end=112,
)

_SOMEREQUEST = _descriptor.Descriptor(
  name='SomeRequest',
  full_name='SomeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipments', full_name='SomeRequest.shipments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SOMEREQUEST_SHIPMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=112,
)


_SOMEOTHERREQUEST_SHIPMENT = _descriptor.Descriptor(
  name='Shipment',
  full_name='SomeOtherRequest.Shipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SomeOtherRequest.Shipment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SomeOtherRequest.Shipment.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=75,
  serialized_end=112,
)

_SOMEOTHERREQUEST = _descriptor.Descriptor(
  name='SomeOtherRequest',
  full_name='SomeOtherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shipments', full_name='SomeOtherRequest.shipments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SOMEOTHERREQUEST_SHIPMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=218,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Response.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=220,
  serialized_end=244,
)

_SOMEREQUEST_SHIPMENT.containing_type = _SOMEREQUEST
_SOMEREQUEST.fields_by_name['shipments'].message_type = _SOMEREQUEST_SHIPMENT
_SOMEOTHERREQUEST_SHIPMENT.containing_type = _SOMEOTHERREQUEST
_SOMEOTHERREQUEST.fields_by_name['shipments'].message_type = _SOMEOTHERREQUEST_SHIPMENT
DESCRIPTOR.message_types_by_name['SomeRequest'] = _SOMEREQUEST
DESCRIPTOR.message_types_by_name['SomeOtherRequest'] = _SOMEOTHERREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

SomeRequest = _reflection.GeneratedProtocolMessageType('SomeRequest', (_message.Message,), dict(

  Shipment = _reflection.GeneratedProtocolMessageType('Shipment', (_message.Message,), dict(
    DESCRIPTOR = _SOMEREQUEST_SHIPMENT,
    __module__ = 'issue_10_pb2'
    # @@protoc_insertion_point(class_scope:SomeRequest.Shipment)
    ))
  ,
  DESCRIPTOR = _SOMEREQUEST,
  __module__ = 'issue_10_pb2'
  # @@protoc_insertion_point(class_scope:SomeRequest)
  ))
_sym_db.RegisterMessage(SomeRequest)
_sym_db.RegisterMessage(SomeRequest.Shipment)

SomeOtherRequest = _reflection.GeneratedProtocolMessageType('SomeOtherRequest', (_message.Message,), dict(

  Shipment = _reflection.GeneratedProtocolMessageType('Shipment', (_message.Message,), dict(
    DESCRIPTOR = _SOMEOTHERREQUEST_SHIPMENT,
    __module__ = 'issue_10_pb2'
    # @@protoc_insertion_point(class_scope:SomeOtherRequest.Shipment)
    ))
  ,
  DESCRIPTOR = _SOMEOTHERREQUEST,
  __module__ = 'issue_10_pb2'
  # @@protoc_insertion_point(class_scope:SomeOtherRequest)
  ))
_sym_db.RegisterMessage(SomeOtherRequest)
_sym_db.RegisterMessage(SomeOtherRequest.Shipment)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'issue_10_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
