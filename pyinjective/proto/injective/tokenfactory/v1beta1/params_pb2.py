# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: injective/tokenfactory/v1beta1/params.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'injective/tokenfactory/v1beta1/params.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.tokenfactory.v1beta1 import authorityMetadata_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_authorityMetadata__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+injective/tokenfactory/v1beta1/params.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x36injective/tokenfactory/v1beta1/authorityMetadata.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x11\x61mino/amino.proto\"\xc5\x01\n\x06Params\x12\x96\x01\n\x12\x64\x65nom_creation_fee\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBM\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"denom_creation_fee\"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsR\x10\x64\x65nomCreationFee:\"\x8a\xe7\xb0*\x1dinjective/tokenfactory/ParamsB\x9f\x02\n\"com.injective.tokenfactory.v1beta1B\x0bParamsProtoP\x01ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\xa2\x02\x03ITX\xaa\x02\x1eInjective.Tokenfactory.V1beta1\xca\x02\x1eInjective\\Tokenfactory\\V1beta1\xe2\x02*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\xea\x02 Injective::Tokenfactory::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.injective.tokenfactory.v1beta1B\013ParamsProtoP\001ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types\242\002\003ITX\252\002\036Injective.Tokenfactory.V1beta1\312\002\036Injective\\Tokenfactory\\V1beta1\342\002*Injective\\Tokenfactory\\V1beta1\\GPBMetadata\352\002 Injective::Tokenfactory::V1beta1'
  _globals['_PARAMS'].fields_by_name['denom_creation_fee']._loaded_options = None
  _globals['_PARAMS'].fields_by_name['denom_creation_fee']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"denom_creation_fee\"\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_PARAMS']._loaded_options = None
  _globals['_PARAMS']._serialized_options = b'\212\347\260*\035injective/tokenfactory/Params'
  _globals['_PARAMS']._serialized_start=236
  _globals['_PARAMS']._serialized_end=433
# @@protoc_insertion_point(module_scope)
