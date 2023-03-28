# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/oracle/v1beta1/proposal.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a%injective/oracle/v1beta1/oracle.proto\"b\n GrantBandOraclePrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08relayers\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"c\n!RevokeBandOraclePrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08relayers\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x80\x01\n!GrantPriceFeederPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x03 \x01(\t\x12\r\n\x05quote\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"r\n\x1eGrantProviderPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x10\n\x08relayers\x18\x04 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"s\n\x1fRevokeProviderPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x81\x01\n\"RevokePriceFeederPrivilegeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x03 \x01(\t\x12\r\n\x05quote\x18\x04 \x01(\t\x12\x10\n\x08relayers\x18\x05 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x96\x01\n\"AuthorizeBandOracleRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x42\n\x07request\x18\x03 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequestB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb7\x01\n\x1fUpdateBandOracleRequestProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65lete_request_ids\x18\x03 \x03(\x04\x12J\n\x15update_oracle_request\x18\x04 \x01(\x0b\x32+.injective.oracle.v1beta1.BandOracleRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x8d\x01\n\x15\x45nableBandIBCProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x46\n\x0f\x62\x61nd_ibc_params\x18\x03 \x01(\x0b\x32\'.injective.oracle.v1beta1.BandIBCParamsB\x04\xc8\xde\x1f\x00:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42NZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.oracle.v1beta1.proposal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types'
  _GRANTBANDORACLEPRIVILEGEPROPOSAL._options = None
  _GRANTBANDORACLEPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _REVOKEBANDORACLEPRIVILEGEPROPOSAL._options = None
  _REVOKEBANDORACLEPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GRANTPRICEFEEDERPRIVILEGEPROPOSAL._options = None
  _GRANTPRICEFEEDERPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GRANTPROVIDERPRIVILEGEPROPOSAL._options = None
  _GRANTPROVIDERPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _REVOKEPROVIDERPRIVILEGEPROPOSAL._options = None
  _REVOKEPROVIDERPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL._options = None
  _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL.fields_by_name['request']._options = None
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL.fields_by_name['request']._serialized_options = b'\310\336\037\000'
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL._options = None
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _UPDATEBANDORACLEREQUESTPROPOSAL._options = None
  _UPDATEBANDORACLEREQUESTPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _ENABLEBANDIBCPROPOSAL.fields_by_name['band_ibc_params']._options = None
  _ENABLEBANDIBCPROPOSAL.fields_by_name['band_ibc_params']._serialized_options = b'\310\336\037\000'
  _ENABLEBANDIBCPROPOSAL._options = None
  _ENABLEBANDIBCPROPOSAL._serialized_options = b'\350\240\037\000\210\240\037\000'
  _GRANTBANDORACLEPRIVILEGEPROPOSAL._serialized_start=162
  _GRANTBANDORACLEPRIVILEGEPROPOSAL._serialized_end=260
  _REVOKEBANDORACLEPRIVILEGEPROPOSAL._serialized_start=262
  _REVOKEBANDORACLEPRIVILEGEPROPOSAL._serialized_end=361
  _GRANTPRICEFEEDERPRIVILEGEPROPOSAL._serialized_start=364
  _GRANTPRICEFEEDERPRIVILEGEPROPOSAL._serialized_end=492
  _GRANTPROVIDERPRIVILEGEPROPOSAL._serialized_start=494
  _GRANTPROVIDERPRIVILEGEPROPOSAL._serialized_end=608
  _REVOKEPROVIDERPRIVILEGEPROPOSAL._serialized_start=610
  _REVOKEPROVIDERPRIVILEGEPROPOSAL._serialized_end=725
  _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL._serialized_start=728
  _REVOKEPRICEFEEDERPRIVILEGEPROPOSAL._serialized_end=857
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL._serialized_start=860
  _AUTHORIZEBANDORACLEREQUESTPROPOSAL._serialized_end=1010
  _UPDATEBANDORACLEREQUESTPROPOSAL._serialized_start=1013
  _UPDATEBANDORACLEREQUESTPROPOSAL._serialized_end=1196
  _ENABLEBANDIBCPROPOSAL._serialized_start=1199
  _ENABLEBANDIBCPROPOSAL._serialized_end=1340
# @@protoc_insertion_point(module_scope)
