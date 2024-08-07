# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/mint.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/mint/v1beta1/mint.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xb9\x01\n\x06Minter\x12O\n\tinflation\x18\x01 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.DecR\tinflation\x12^\n\x11\x61nnual_provisions\x18\x02 \x01(\tB1\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.DecR\x10\x61nnualProvisions\"\xed\x03\n\x06Params\x12\x1d\n\nmint_denom\x18\x01 \x01(\tR\tmintDenom\x12j\n\x15inflation_rate_change\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x13inflationRateChange\x12[\n\rinflation_max\x18\x03 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x0cinflationMax\x12[\n\rinflation_min\x18\x04 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\x0cinflationMin\x12W\n\x0bgoal_bonded\x18\x05 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1b\x63osmossdk.io/math.LegacyDec\xd2\xb4-\ncosmos.Dec\xa8\xe7\xb0*\x01R\ngoalBonded\x12&\n\x0f\x62locks_per_year\x18\x06 \x01(\x04R\rblocksPerYear:\x1d\x8a\xe7\xb0*\x18\x63osmos-sdk/x/mint/ParamsB\xbd\x01\n\x17\x63om.cosmos.mint.v1beta1B\tMintProtoP\x01Z)github.com/cosmos/cosmos-sdk/x/mint/types\xa2\x02\x03\x43MX\xaa\x02\x13\x43osmos.Mint.V1beta1\xca\x02\x13\x43osmos\\Mint\\V1beta1\xe2\x02\x1f\x43osmos\\Mint\\V1beta1\\GPBMetadata\xea\x02\x15\x43osmos::Mint::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.mint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.cosmos.mint.v1beta1B\tMintProtoP\001Z)github.com/cosmos/cosmos-sdk/x/mint/types\242\002\003CMX\252\002\023Cosmos.Mint.V1beta1\312\002\023Cosmos\\Mint\\V1beta1\342\002\037Cosmos\\Mint\\V1beta1\\GPBMetadata\352\002\025Cosmos::Mint::V1beta1'
  _globals['_MINTER'].fields_by_name['inflation']._loaded_options = None
  _globals['_MINTER'].fields_by_name['inflation']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _globals['_MINTER'].fields_by_name['annual_provisions']._loaded_options = None
  _globals['_MINTER'].fields_by_name['annual_provisions']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec'
  _globals['_PARAMS'].fields_by_name['inflation_rate_change']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_rate_change']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['inflation_max']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_max']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['inflation_min']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['inflation_min']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS'].fields_by_name['goal_bonded']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['goal_bonded']._serialized_options = b'\310\336\037\000\332\336\037\033cosmossdk.io/math.LegacyDec\322\264-\ncosmos.Dec\250\347\260*\001'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\212\347\260*\030cosmos-sdk/x/mint/Params'
  _globals['_MINTER']._serialized_start=124
  _globals['_MINTER']._serialized_end=309
  _globals['_PARAMS']._serialized_start=312
  _globals['_PARAMS']._serialized_end=805
# @@protoc_insertion_point(module_scope)
