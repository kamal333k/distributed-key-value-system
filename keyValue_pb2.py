# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keyValue.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keyValue.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0ekeyValue.proto\":\n\x10\x43lientPutRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\"+\n\x10\x43lientGetRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\"H\n\x0e\x43lientResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\x0e\n\x06status\x18\x03 \x01(\x08\x12\r\n\x05value\x18\x04 \x01(\t\"N\n\x11ReplicaPutRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\r\"?\n\x11ReplicaGetRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\x11\n\ttimestamp\x18\x03 \x01(\r\"l\n\x0fReplicaResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\x0e\n\x06status\x18\x03 \x01(\x08\x12\r\n\x05value\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\r\x12\x0e\n\x06nodeid\x18\x06 \x01(\t\"\xbc\x02\n\x0fKeyValueMessage\x12-\n\x10\x63lientputrequest\x18\x01 \x01(\x0b\x32\x11.ClientPutRequestH\x00\x12-\n\x10\x63lientgetrequest\x18\x02 \x01(\x0b\x32\x11.ClientGetRequestH\x00\x12)\n\x0e\x63lientresponse\x18\x03 \x01(\x0b\x32\x0f.ClientResponseH\x00\x12/\n\x11replicaputrequest\x18\x04 \x01(\x0b\x32\x12.ReplicaPutRequestH\x00\x12/\n\x11replicagetrequest\x18\x05 \x01(\x0b\x32\x12.ReplicaGetRequestH\x00\x12+\n\x0freplicaresponse\x18\x06 \x01(\x0b\x32\x10.ReplicaResponseH\x00\x42\x11\n\x0fkeyvaluemessageb\x06proto3')
)




_CLIENTPUTREQUEST = _descriptor.Descriptor(
  name='ClientPutRequest',
  full_name='ClientPutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ClientPutRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientPutRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientPutRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=76,
)


_CLIENTGETREQUEST = _descriptor.Descriptor(
  name='ClientGetRequest',
  full_name='ClientGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ClientGetRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientGetRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=78,
  serialized_end=121,
)


_CLIENTRESPONSE = _descriptor.Descriptor(
  name='ClientResponse',
  full_name='ClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ClientResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ClientResponse.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientResponse.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientResponse.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=123,
  serialized_end=195,
)


_REPLICAPUTREQUEST = _descriptor.Descriptor(
  name='ReplicaPutRequest',
  full_name='ReplicaPutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ReplicaPutRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaPutRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaPutRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaPutRequest.timestamp', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=275,
)


_REPLICAGETREQUEST = _descriptor.Descriptor(
  name='ReplicaGetRequest',
  full_name='ReplicaGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ReplicaGetRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaGetRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaGetRequest.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=277,
  serialized_end=340,
)


_REPLICARESPONSE = _descriptor.Descriptor(
  name='ReplicaResponse',
  full_name='ReplicaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ReplicaResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaResponse.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ReplicaResponse.status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaResponse.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaResponse.timestamp', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeid', full_name='ReplicaResponse.nodeid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=342,
  serialized_end=450,
)


_KEYVALUEMESSAGE = _descriptor.Descriptor(
  name='KeyValueMessage',
  full_name='KeyValueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientputrequest', full_name='KeyValueMessage.clientputrequest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientgetrequest', full_name='KeyValueMessage.clientgetrequest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientresponse', full_name='KeyValueMessage.clientresponse', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicaputrequest', full_name='KeyValueMessage.replicaputrequest', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicagetrequest', full_name='KeyValueMessage.replicagetrequest', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replicaresponse', full_name='KeyValueMessage.replicaresponse', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='keyvaluemessage', full_name='KeyValueMessage.keyvaluemessage',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=453,
  serialized_end=769,
)

_KEYVALUEMESSAGE.fields_by_name['clientputrequest'].message_type = _CLIENTPUTREQUEST
_KEYVALUEMESSAGE.fields_by_name['clientgetrequest'].message_type = _CLIENTGETREQUEST
_KEYVALUEMESSAGE.fields_by_name['clientresponse'].message_type = _CLIENTRESPONSE
_KEYVALUEMESSAGE.fields_by_name['replicaputrequest'].message_type = _REPLICAPUTREQUEST
_KEYVALUEMESSAGE.fields_by_name['replicagetrequest'].message_type = _REPLICAGETREQUEST
_KEYVALUEMESSAGE.fields_by_name['replicaresponse'].message_type = _REPLICARESPONSE
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['clientputrequest'])
_KEYVALUEMESSAGE.fields_by_name['clientputrequest'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['clientgetrequest'])
_KEYVALUEMESSAGE.fields_by_name['clientgetrequest'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['clientresponse'])
_KEYVALUEMESSAGE.fields_by_name['clientresponse'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replicaputrequest'])
_KEYVALUEMESSAGE.fields_by_name['replicaputrequest'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replicagetrequest'])
_KEYVALUEMESSAGE.fields_by_name['replicagetrequest'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
_KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replicaresponse'])
_KEYVALUEMESSAGE.fields_by_name['replicaresponse'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['keyvaluemessage']
DESCRIPTOR.message_types_by_name['ClientPutRequest'] = _CLIENTPUTREQUEST
DESCRIPTOR.message_types_by_name['ClientGetRequest'] = _CLIENTGETREQUEST
DESCRIPTOR.message_types_by_name['ClientResponse'] = _CLIENTRESPONSE
DESCRIPTOR.message_types_by_name['ReplicaPutRequest'] = _REPLICAPUTREQUEST
DESCRIPTOR.message_types_by_name['ReplicaGetRequest'] = _REPLICAGETREQUEST
DESCRIPTOR.message_types_by_name['ReplicaResponse'] = _REPLICARESPONSE
DESCRIPTOR.message_types_by_name['KeyValueMessage'] = _KEYVALUEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientPutRequest = _reflection.GeneratedProtocolMessageType('ClientPutRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTPUTREQUEST,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ClientPutRequest)
  ))
_sym_db.RegisterMessage(ClientPutRequest)

ClientGetRequest = _reflection.GeneratedProtocolMessageType('ClientGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTGETREQUEST,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ClientGetRequest)
  ))
_sym_db.RegisterMessage(ClientGetRequest)

ClientResponse = _reflection.GeneratedProtocolMessageType('ClientResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRESPONSE,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ClientResponse)
  ))
_sym_db.RegisterMessage(ClientResponse)

ReplicaPutRequest = _reflection.GeneratedProtocolMessageType('ReplicaPutRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPLICAPUTREQUEST,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaPutRequest)
  ))
_sym_db.RegisterMessage(ReplicaPutRequest)

ReplicaGetRequest = _reflection.GeneratedProtocolMessageType('ReplicaGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPLICAGETREQUEST,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaGetRequest)
  ))
_sym_db.RegisterMessage(ReplicaGetRequest)

ReplicaResponse = _reflection.GeneratedProtocolMessageType('ReplicaResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLICARESPONSE,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaResponse)
  ))
_sym_db.RegisterMessage(ReplicaResponse)

KeyValueMessage = _reflection.GeneratedProtocolMessageType('KeyValueMessage', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEMESSAGE,
  __module__ = 'keyValue_pb2'
  # @@protoc_insertion_point(class_scope:KeyValueMessage)
  ))
_sym_db.RegisterMessage(KeyValueMessage)


# @@protoc_insertion_point(module_scope)
