# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/wasmx/v1/wasmx.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.wasmx.v1 import proposal_pb2 as injective_dot_wasmx_dot_v1_dot_proposal__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1einjective/wasmx/v1/wasmx.proto\x12\x12injective.wasmx.v1\x1a\x14gogoproto/gogo.proto\x1a!injective/wasmx/v1/proposal.proto\"\x86\x01\n\x06Params\x12\x1c\n\x14is_execution_enabled\x18\x01 \x01(\x08\x12!\n\x19max_begin_block_total_gas\x18\x02 \x01(\x04\x12\x1e\n\x16max_contract_gas_limit\x18\x03 \x01(\x04\x12\x15\n\rmin_gas_price\x18\x04 \x01(\x04:\x04\xe8\xa0\x1f\x01\"\xde\x01\n\x12RegisteredContract\x12\x11\n\tgas_limit\x18\x01 \x01(\x04\x12\x11\n\tgas_price\x18\x02 \x01(\x04\x12\x15\n\ris_executable\x18\x03 \x01(\x08\x12\x15\n\x07\x63ode_id\x18\x04 \x01(\x04\x42\x04\xc8\xde\x1f\x01\x12\x1b\n\radmin_address\x18\x05 \x01(\tB\x04\xc8\xde\x1f\x01\x12\x1d\n\x0fgranter_address\x18\x06 \x01(\tB\x04\xc8\xde\x1f\x01\x12\x32\n\tfund_mode\x18\x07 \x01(\x0e\x32\x1f.injective.wasmx.v1.FundingMode:\x04\xe8\xa0\x1f\x01\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.wasmx.v1.wasmx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/wasmx/types'
  _globals['_PARAMS']._options = None
  _globals['_PARAMS']._serialized_options = b'\350\240\037\001'
  _globals['_REGISTEREDCONTRACT'].fields_by_name['code_id']._options = None
  _globals['_REGISTEREDCONTRACT'].fields_by_name['code_id']._serialized_options = b'\310\336\037\001'
  _globals['_REGISTEREDCONTRACT'].fields_by_name['admin_address']._options = None
  _globals['_REGISTEREDCONTRACT'].fields_by_name['admin_address']._serialized_options = b'\310\336\037\001'
  _globals['_REGISTEREDCONTRACT'].fields_by_name['granter_address']._options = None
  _globals['_REGISTEREDCONTRACT'].fields_by_name['granter_address']._serialized_options = b'\310\336\037\001'
  _globals['_REGISTEREDCONTRACT']._options = None
  _globals['_REGISTEREDCONTRACT']._serialized_options = b'\350\240\037\001'
  _globals['_PARAMS']._serialized_start=112
  _globals['_PARAMS']._serialized_end=246
  _globals['_REGISTEREDCONTRACT']._serialized_start=249
  _globals['_REGISTEREDCONTRACT']._serialized_end=471
# @@protoc_insertion_point(module_scope)
