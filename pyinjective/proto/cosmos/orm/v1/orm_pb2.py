# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/orm/v1/orm.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63osmos/orm/v1/orm.proto\x12\rcosmos.orm.v1\x1a google/protobuf/descriptor.proto\"\xa6\x01\n\x0fTableDescriptor\x12\x44\n\x0bprimary_key\x18\x01 \x01(\x0b\x32#.cosmos.orm.v1.PrimaryKeyDescriptorR\nprimaryKey\x12=\n\x05index\x18\x02 \x03(\x0b\x32\'.cosmos.orm.v1.SecondaryIndexDescriptorR\x05index\x12\x0e\n\x02id\x18\x03 \x01(\rR\x02id\"U\n\x14PrimaryKeyDescriptor\x12\x16\n\x06\x66ields\x18\x01 \x01(\tR\x06\x66ields\x12%\n\x0e\x61uto_increment\x18\x02 \x01(\x08R\rautoIncrement\"Z\n\x18SecondaryIndexDescriptor\x12\x16\n\x06\x66ields\x18\x01 \x01(\tR\x06\x66ields\x12\x0e\n\x02id\x18\x02 \x01(\rR\x02id\x12\x16\n\x06unique\x18\x03 \x01(\x08R\x06unique\"%\n\x13SingletonDescriptor\x12\x0e\n\x02id\x18\x01 \x01(\rR\x02id:X\n\x05table\x12\x1f.google.protobuf.MessageOptions\x18\xee\xb3\xea\x31 \x01(\x0b\x32\x1e.cosmos.orm.v1.TableDescriptorR\x05table:d\n\tsingleton\x12\x1f.google.protobuf.MessageOptions\x18\xef\xb3\xea\x31 \x01(\x0b\x32\".cosmos.orm.v1.SingletonDescriptorR\tsingletonBs\n\x11\x63om.cosmos.orm.v1B\x08OrmProtoP\x01\xa2\x02\x03\x43OX\xaa\x02\rCosmos.Orm.V1\xca\x02\rCosmos\\Orm\\V1\xe2\x02\x19\x43osmos\\Orm\\V1\\GPBMetadata\xea\x02\x0f\x43osmos::Orm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.orm.v1.orm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.cosmos.orm.v1B\010OrmProtoP\001\242\002\003COX\252\002\rCosmos.Orm.V1\312\002\rCosmos\\Orm\\V1\342\002\031Cosmos\\Orm\\V1\\GPBMetadata\352\002\017Cosmos::Orm::V1'
  _globals['_TABLEDESCRIPTOR']._serialized_start=77
  _globals['_TABLEDESCRIPTOR']._serialized_end=243
  _globals['_PRIMARYKEYDESCRIPTOR']._serialized_start=245
  _globals['_PRIMARYKEYDESCRIPTOR']._serialized_end=330
  _globals['_SECONDARYINDEXDESCRIPTOR']._serialized_start=332
  _globals['_SECONDARYINDEXDESCRIPTOR']._serialized_end=422
  _globals['_SINGLETONDESCRIPTOR']._serialized_start=424
  _globals['_SINGLETONDESCRIPTOR']._serialized_end=461
# @@protoc_insertion_point(module_scope)
