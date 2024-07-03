# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/genesis.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.peggy.v1 import types_pb2 as injective_dot_peggy_dot_v1_dot_types__pb2
from pyinjective.proto.injective.peggy.v1 import msgs_pb2 as injective_dot_peggy_dot_v1_dot_msgs__pb2
from pyinjective.proto.injective.peggy.v1 import batch_pb2 as injective_dot_peggy_dot_v1_dot_batch__pb2
from pyinjective.proto.injective.peggy.v1 import attestation_pb2 as injective_dot_peggy_dot_v1_dot_attestation__pb2
from pyinjective.proto.injective.peggy.v1 import params_pb2 as injective_dot_peggy_dot_v1_dot_params__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n injective/peggy/v1/genesis.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\x1a\x1einjective/peggy/v1/types.proto\x1a\x1dinjective/peggy/v1/msgs.proto\x1a\x1einjective/peggy/v1/batch.proto\x1a$injective/peggy/v1/attestation.proto\x1a\x1finjective/peggy/v1/params.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\x80\x06\n\x0cGenesisState\x12*\n\x06params\x18\x01 \x01(\x0b\x32\x1a.injective.peggy.v1.Params\x12\x1b\n\x13last_observed_nonce\x18\x02 \x01(\x04\x12+\n\x07valsets\x18\x03 \x03(\x0b\x32\x1a.injective.peggy.v1.Valset\x12=\n\x0fvalset_confirms\x18\x04 \x03(\x0b\x32$.injective.peggy.v1.MsgValsetConfirm\x12\x34\n\x07\x62\x61tches\x18\x05 \x03(\x0b\x32#.injective.peggy.v1.OutgoingTxBatch\x12;\n\x0e\x62\x61tch_confirms\x18\x06 \x03(\x0b\x32#.injective.peggy.v1.MsgConfirmBatch\x12\x35\n\x0c\x61ttestations\x18\x07 \x03(\x0b\x32\x1f.injective.peggy.v1.Attestation\x12O\n\x16orchestrator_addresses\x18\x08 \x03(\x0b\x32/.injective.peggy.v1.MsgSetOrchestratorAddresses\x12\x39\n\x0f\x65rc20_to_denoms\x18\t \x03(\x0b\x32 .injective.peggy.v1.ERC20ToDenom\x12\x43\n\x13unbatched_transfers\x18\n \x03(\x0b\x32&.injective.peggy.v1.OutgoingTransferTx\x12%\n\x1dlast_observed_ethereum_height\x18\x0b \x01(\x04\x12\x1e\n\x16last_outgoing_batch_id\x18\x0c \x01(\x04\x12\x1d\n\x15last_outgoing_pool_id\x18\r \x01(\x04\x12>\n\x14last_observed_valset\x18\x0e \x01(\x0b\x32\x1a.injective.peggy.v1.ValsetB\x04\xc8\xde\x1f\x00\x12\x1a\n\x12\x65thereum_blacklist\x18\x0f \x03(\tBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _globals['_GENESISSTATE'].fields_by_name['last_observed_valset']._options = None
  _globals['_GENESISSTATE'].fields_by_name['last_observed_valset']._serialized_options = b'\310\336\037\000'
  _globals['_GENESISSTATE']._serialized_start=277
  _globals['_GENESISSTATE']._serialized_end=1045
# @@protoc_insertion_point(module_scope)
