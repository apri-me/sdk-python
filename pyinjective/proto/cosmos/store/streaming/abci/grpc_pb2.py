# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/store/streaming/abci/grpc.proto
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
    'cosmos/store/streaming/abci/grpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
from pyinjective.proto.cosmos.store.v1beta1 import listening_pb2 as cosmos_dot_store_dot_v1beta1_dot_listening__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cosmos/store/streaming/abci/grpc.proto\x12\x1b\x63osmos.store.streaming.abci\x1a\x1btendermint/abci/types.proto\x1a$cosmos/store/v1beta1/listening.proto\"\x8f\x01\n\x1aListenFinalizeBlockRequest\x12\x37\n\x03req\x18\x01 \x01(\x0b\x32%.tendermint.abci.RequestFinalizeBlockR\x03req\x12\x38\n\x03res\x18\x02 \x01(\x0b\x32&.tendermint.abci.ResponseFinalizeBlockR\x03res\"\x1d\n\x1bListenFinalizeBlockResponse\"\xad\x01\n\x13ListenCommitRequest\x12!\n\x0c\x62lock_height\x18\x01 \x01(\x03R\x0b\x62lockHeight\x12\x31\n\x03res\x18\x02 \x01(\x0b\x32\x1f.tendermint.abci.ResponseCommitR\x03res\x12@\n\nchange_set\x18\x03 \x03(\x0b\x32!.cosmos.store.v1beta1.StoreKVPairR\tchangeSet\"\x16\n\x14ListenCommitResponse2\x95\x02\n\x13\x41\x42\x43IListenerService\x12\x88\x01\n\x13ListenFinalizeBlock\x12\x37.cosmos.store.streaming.abci.ListenFinalizeBlockRequest\x1a\x38.cosmos.store.streaming.abci.ListenFinalizeBlockResponse\x12s\n\x0cListenCommit\x12\x30.cosmos.store.streaming.abci.ListenCommitRequest\x1a\x31.cosmos.store.streaming.abci.ListenCommitResponseB\xdf\x01\n\x1f\x63om.cosmos.store.streaming.abciB\tGrpcProtoP\x01Z!cosmossdk.io/store/streaming/abci\xa2\x02\x04\x43SSA\xaa\x02\x1b\x43osmos.Store.Streaming.Abci\xca\x02\x1b\x43osmos\\Store\\Streaming\\Abci\xe2\x02\'Cosmos\\Store\\Streaming\\Abci\\GPBMetadata\xea\x02\x1e\x43osmos::Store::Streaming::Abcib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.store.streaming.abci.grpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.cosmos.store.streaming.abciB\tGrpcProtoP\001Z!cosmossdk.io/store/streaming/abci\242\002\004CSSA\252\002\033Cosmos.Store.Streaming.Abci\312\002\033Cosmos\\Store\\Streaming\\Abci\342\002\'Cosmos\\Store\\Streaming\\Abci\\GPBMetadata\352\002\036Cosmos::Store::Streaming::Abci'
  _globals['_LISTENFINALIZEBLOCKREQUEST']._serialized_start=139
  _globals['_LISTENFINALIZEBLOCKREQUEST']._serialized_end=282
  _globals['_LISTENFINALIZEBLOCKRESPONSE']._serialized_start=284
  _globals['_LISTENFINALIZEBLOCKRESPONSE']._serialized_end=313
  _globals['_LISTENCOMMITREQUEST']._serialized_start=316
  _globals['_LISTENCOMMITREQUEST']._serialized_end=489
  _globals['_LISTENCOMMITRESPONSE']._serialized_start=491
  _globals['_LISTENCOMMITRESPONSE']._serialized_end=513
  _globals['_ABCILISTENERSERVICE']._serialized_start=516
  _globals['_ABCILISTENERSERVICE']._serialized_end=793
# @@protoc_insertion_point(module_scope)
