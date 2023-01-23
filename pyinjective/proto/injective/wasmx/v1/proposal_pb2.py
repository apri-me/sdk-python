# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import proposal_pb2 as cosmwasm_dot_wasm_dot_v1_dot_proposal__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/wasmx/v1/proposal.proto',
  package='injective.wasmx.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!injective/wasmx/v1/proposal.proto\x12\x12injective.wasmx.v1\x1a\x14gogoproto/gogo.proto\x1a\x1f\x63osmwasm/wasm/v1/proposal.proto\"\xb1\x01\n#ContractRegistrationRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\\\n\x1d\x63ontract_registration_request\x18\x03 \x01(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb7\x01\n(BatchContractRegistrationRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12]\n\x1e\x63ontract_registration_requests\x18\x03 \x03(\x0b\x32/.injective.wasmx.v1.ContractRegistrationRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"l\n#BatchContractDeregistrationProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x17\n\tcontracts\x18\x03 \x03(\tB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"s\n\x1b\x43ontractRegistrationRequest\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12\x11\n\tgas_limit\x18\x02 \x01(\x04\x12\x11\n\tgas_price\x18\x03 \x01(\x04\x12\x14\n\x0cpin_contract\x18\x04 \x01(\x08\"\x84\x01\n\x16\x42\x61tchStoreCodeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12<\n\tproposals\x18\x03 \x03(\x0b\x32#.cosmwasm.wasm.v1.StoreCodeProposalB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmwasm_dot_wasm_dot_v1_dot_proposal__pb2.DESCRIPTOR,])




_CONTRACTREGISTRATIONREQUESTPROPOSAL = _descriptor.Descriptor(
  name='ContractRegistrationRequestProposal',
  full_name='injective.wasmx.v1.ContractRegistrationRequestProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.wasmx.v1.ContractRegistrationRequestProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.wasmx.v1.ContractRegistrationRequestProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_registration_request', full_name='injective.wasmx.v1.ContractRegistrationRequestProposal.contract_registration_request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=290,
)


_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL = _descriptor.Descriptor(
  name='BatchContractRegistrationRequestProposal',
  full_name='injective.wasmx.v1.BatchContractRegistrationRequestProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.wasmx.v1.BatchContractRegistrationRequestProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.wasmx.v1.BatchContractRegistrationRequestProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contract_registration_requests', full_name='injective.wasmx.v1.BatchContractRegistrationRequestProposal.contract_registration_requests', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=476,
)


_BATCHCONTRACTDEREGISTRATIONPROPOSAL = _descriptor.Descriptor(
  name='BatchContractDeregistrationProposal',
  full_name='injective.wasmx.v1.BatchContractDeregistrationProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.wasmx.v1.BatchContractDeregistrationProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.wasmx.v1.BatchContractDeregistrationProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contracts', full_name='injective.wasmx.v1.BatchContractDeregistrationProposal.contracts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=586,
)


_CONTRACTREGISTRATIONREQUEST = _descriptor.Descriptor(
  name='ContractRegistrationRequest',
  full_name='injective.wasmx.v1.ContractRegistrationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract_address', full_name='injective.wasmx.v1.ContractRegistrationRequest.contract_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_limit', full_name='injective.wasmx.v1.ContractRegistrationRequest.gas_limit', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='injective.wasmx.v1.ContractRegistrationRequest.gas_price', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pin_contract', full_name='injective.wasmx.v1.ContractRegistrationRequest.pin_contract', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=588,
  serialized_end=703,
)


_BATCHSTORECODEPROPOSAL = _descriptor.Descriptor(
  name='BatchStoreCodeProposal',
  full_name='injective.wasmx.v1.BatchStoreCodeProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.wasmx.v1.BatchStoreCodeProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.wasmx.v1.BatchStoreCodeProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposals', full_name='injective.wasmx.v1.BatchStoreCodeProposal.proposals', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=838,
)

_CONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_request'].message_type = _CONTRACTREGISTRATIONREQUEST
_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_requests'].message_type = _CONTRACTREGISTRATIONREQUEST
_BATCHSTORECODEPROPOSAL.fields_by_name['proposals'].message_type = cosmwasm_dot_wasm_dot_v1_dot_proposal__pb2._STORECODEPROPOSAL
DESCRIPTOR.message_types_by_name['ContractRegistrationRequestProposal'] = _CONTRACTREGISTRATIONREQUESTPROPOSAL
DESCRIPTOR.message_types_by_name['BatchContractRegistrationRequestProposal'] = _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL
DESCRIPTOR.message_types_by_name['BatchContractDeregistrationProposal'] = _BATCHCONTRACTDEREGISTRATIONPROPOSAL
DESCRIPTOR.message_types_by_name['ContractRegistrationRequest'] = _CONTRACTREGISTRATIONREQUEST
DESCRIPTOR.message_types_by_name['BatchStoreCodeProposal'] = _BATCHSTORECODEPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContractRegistrationRequestProposal = _reflection.GeneratedProtocolMessageType('ContractRegistrationRequestProposal', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTREGISTRATIONREQUESTPROPOSAL,
  '__module__' : 'injective.wasmx.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.ContractRegistrationRequestProposal)
  })
_sym_db.RegisterMessage(ContractRegistrationRequestProposal)

BatchContractRegistrationRequestProposal = _reflection.GeneratedProtocolMessageType('BatchContractRegistrationRequestProposal', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL,
  '__module__' : 'injective.wasmx.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.BatchContractRegistrationRequestProposal)
  })
_sym_db.RegisterMessage(BatchContractRegistrationRequestProposal)

BatchContractDeregistrationProposal = _reflection.GeneratedProtocolMessageType('BatchContractDeregistrationProposal', (_message.Message,), {
  'DESCRIPTOR' : _BATCHCONTRACTDEREGISTRATIONPROPOSAL,
  '__module__' : 'injective.wasmx.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.BatchContractDeregistrationProposal)
  })
_sym_db.RegisterMessage(BatchContractDeregistrationProposal)

ContractRegistrationRequest = _reflection.GeneratedProtocolMessageType('ContractRegistrationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTREGISTRATIONREQUEST,
  '__module__' : 'injective.wasmx.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.ContractRegistrationRequest)
  })
_sym_db.RegisterMessage(ContractRegistrationRequest)

BatchStoreCodeProposal = _reflection.GeneratedProtocolMessageType('BatchStoreCodeProposal', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSTORECODEPROPOSAL,
  '__module__' : 'injective.wasmx.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.wasmx.v1.BatchStoreCodeProposal)
  })
_sym_db.RegisterMessage(BatchStoreCodeProposal)


DESCRIPTOR._options = None
_CONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_request']._options = None
_CONTRACTREGISTRATIONREQUESTPROPOSAL._options = None
_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL.fields_by_name['contract_registration_requests']._options = None
_BATCHCONTRACTREGISTRATIONREQUESTPROPOSAL._options = None
_BATCHCONTRACTDEREGISTRATIONPROPOSAL.fields_by_name['contracts']._options = None
_BATCHCONTRACTDEREGISTRATIONPROPOSAL._options = None
_BATCHSTORECODEPROPOSAL.fields_by_name['proposals']._options = None
_BATCHSTORECODEPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)