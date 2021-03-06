# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bootstrap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bootstrap.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x62ootstrap.proto\"{\n\x16ServiceRegisterRequest\x12\x17\n\x0fservice_address\x18\x01 \x01(\t\x12\x12\n\nservice_id\x18\x02 \x01(\t\x12\x1e\n\x16service_server_address\x18\x03 \x01(\t\x12\x14\n\x0cservice_name\x18\x04 \x01(\t\"e\n ServiceRegistrationStatusRequest\x12\x17\n\x0fservice_address\x18\x01 \x01(\t\x12\x12\n\nservice_id\x18\x02 \x01(\t\x12\x14\n\x0cservice_name\x18\x03 \x01(\t\"\xe8\x01\n!ServiceRegistrationStatusResponse\x12!\n\x19\x62ootstrap_service_address\x18\x01 \x01(\t\x12\x1c\n\x14\x62ootstrap_service_id\x18\x02 \x01(\t\x12\x1c\n\x14registered_addresses\x18\x03 \x03(\t\x12\x16\n\x0eregistered_ids\x18\x04 \x03(\t\x12#\n\x1bregistered_server_addresses\x18\x05 \x03(\t\x12\x18\n\x10registered_count\x18\x06 \x01(\x05\x12\r\n\x05ready\x18\x07 \x01(\x08\x32\xcc\x01\n\x0f\x42ootstrapServer\x12P\n\x0fRegisterService\x12\x17.ServiceRegisterRequest\x1a\".ServiceRegistrationStatusResponse\"\x00\x12g\n\x1cGetServiceRegistrationStatus\x12!.ServiceRegistrationStatusRequest\x1a\".ServiceRegistrationStatusResponse\"\x00\x62\x06proto3'
)




_SERVICEREGISTERREQUEST = _descriptor.Descriptor(
  name='ServiceRegisterRequest',
  full_name='ServiceRegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_address', full_name='ServiceRegisterRequest.service_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_id', full_name='ServiceRegisterRequest.service_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_server_address', full_name='ServiceRegisterRequest.service_server_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ServiceRegisterRequest.service_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=142,
)


_SERVICEREGISTRATIONSTATUSREQUEST = _descriptor.Descriptor(
  name='ServiceRegistrationStatusRequest',
  full_name='ServiceRegistrationStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_address', full_name='ServiceRegistrationStatusRequest.service_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_id', full_name='ServiceRegistrationStatusRequest.service_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ServiceRegistrationStatusRequest.service_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=245,
)


_SERVICEREGISTRATIONSTATUSRESPONSE = _descriptor.Descriptor(
  name='ServiceRegistrationStatusResponse',
  full_name='ServiceRegistrationStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bootstrap_service_address', full_name='ServiceRegistrationStatusResponse.bootstrap_service_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bootstrap_service_id', full_name='ServiceRegistrationStatusResponse.bootstrap_service_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_addresses', full_name='ServiceRegistrationStatusResponse.registered_addresses', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_ids', full_name='ServiceRegistrationStatusResponse.registered_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_server_addresses', full_name='ServiceRegistrationStatusResponse.registered_server_addresses', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registered_count', full_name='ServiceRegistrationStatusResponse.registered_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ready', full_name='ServiceRegistrationStatusResponse.ready', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=480,
)

DESCRIPTOR.message_types_by_name['ServiceRegisterRequest'] = _SERVICEREGISTERREQUEST
DESCRIPTOR.message_types_by_name['ServiceRegistrationStatusRequest'] = _SERVICEREGISTRATIONSTATUSREQUEST
DESCRIPTOR.message_types_by_name['ServiceRegistrationStatusResponse'] = _SERVICEREGISTRATIONSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServiceRegisterRequest = _reflection.GeneratedProtocolMessageType('ServiceRegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREGISTERREQUEST,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:ServiceRegisterRequest)
  })
_sym_db.RegisterMessage(ServiceRegisterRequest)

ServiceRegistrationStatusRequest = _reflection.GeneratedProtocolMessageType('ServiceRegistrationStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREGISTRATIONSTATUSREQUEST,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:ServiceRegistrationStatusRequest)
  })
_sym_db.RegisterMessage(ServiceRegistrationStatusRequest)

ServiceRegistrationStatusResponse = _reflection.GeneratedProtocolMessageType('ServiceRegistrationStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEREGISTRATIONSTATUSRESPONSE,
  '__module__' : 'bootstrap_pb2'
  # @@protoc_insertion_point(class_scope:ServiceRegistrationStatusResponse)
  })
_sym_db.RegisterMessage(ServiceRegistrationStatusResponse)



_BOOTSTRAPSERVER = _descriptor.ServiceDescriptor(
  name='BootstrapServer',
  full_name='BootstrapServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=483,
  serialized_end=687,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterService',
    full_name='BootstrapServer.RegisterService',
    index=0,
    containing_service=None,
    input_type=_SERVICEREGISTERREQUEST,
    output_type=_SERVICEREGISTRATIONSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServiceRegistrationStatus',
    full_name='BootstrapServer.GetServiceRegistrationStatus',
    index=1,
    containing_service=None,
    input_type=_SERVICEREGISTRATIONSTATUSREQUEST,
    output_type=_SERVICEREGISTRATIONSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOTSTRAPSERVER)

DESCRIPTOR.services_by_name['BootstrapServer'] = _BOOTSTRAPSERVER

# @@protoc_insertion_point(module_scope)
