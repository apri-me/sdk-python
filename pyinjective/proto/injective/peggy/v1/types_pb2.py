# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/types.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1einjective/peggy/v1/types.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\":\n\x0f\x42ridgeValidator\x12\r\n\x05power\x18\x01 \x01(\x04\x12\x18\n\x10\x65thereum_address\x18\x02 \x01(\t\"\xba\x01\n\x06Valset\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x34\n\x07members\x18\x02 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x45\n\rreward_amount\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\x12\x14\n\x0creward_token\x18\x05 \x01(\t\"]\n\x1fLastObservedEthereumBlockHeight\x12\x1b\n\x13\x63osmos_block_height\x18\x01 \x01(\x04\x12\x1d\n\x15\x65thereum_block_height\x18\x02 \x01(\x04\"M\n\x0eLastClaimEvent\x12\x1c\n\x14\x65thereum_event_nonce\x18\x01 \x01(\x04\x12\x1d\n\x15\x65thereum_event_height\x18\x02 \x01(\x04\",\n\x0c\x45RC20ToDenom\x12\r\n\x05\x65rc20\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\tBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _globals['_VALSET'].fields_by_name['reward_amount']._loaded_options = None
  _globals['_VALSET'].fields_by_name['reward_amount']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Int'
  _globals['_BRIDGEVALIDATOR']._serialized_start=76
  _globals['_BRIDGEVALIDATOR']._serialized_end=134
  _globals['_VALSET']._serialized_start=137
  _globals['_VALSET']._serialized_end=323
  _globals['_LASTOBSERVEDETHEREUMBLOCKHEIGHT']._serialized_start=325
  _globals['_LASTOBSERVEDETHEREUMBLOCKHEIGHT']._serialized_end=418
  _globals['_LASTCLAIMEVENT']._serialized_start=420
  _globals['_LASTCLAIMEVENT']._serialized_end=497
  _globals['_ERC20TODENOM']._serialized_start=499
  _globals['_ERC20TODENOM']._serialized_end=543
# @@protoc_insertion_point(module_scope)
