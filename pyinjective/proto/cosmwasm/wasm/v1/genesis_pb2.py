# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmwasm/wasm/v1/genesis.proto
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
    'cosmwasm/wasm/v1/genesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmwasm/wasm/v1/genesis.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xcf\x02\n\x0cGenesisState\x12;\n\x06params\x18\x01 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params\x12J\n\x05\x63odes\x18\x02 \x03(\x0b\x32\x16.cosmwasm.wasm.v1.CodeB\x1c\xc8\xde\x1f\x00\xea\xde\x1f\x0f\x63odes,omitempty\xa8\xe7\xb0*\x01R\x05\x63odes\x12Z\n\tcontracts\x18\x03 \x03(\x0b\x32\x1a.cosmwasm.wasm.v1.ContractB \xc8\xde\x1f\x00\xea\xde\x1f\x13\x63ontracts,omitempty\xa8\xe7\xb0*\x01R\tcontracts\x12Z\n\tsequences\x18\x04 \x03(\x0b\x32\x1a.cosmwasm.wasm.v1.SequenceB \xc8\xde\x1f\x00\xea\xde\x1f\x13sequences,omitempty\xa8\xe7\xb0*\x01R\tsequences\"\xa6\x01\n\x04\x43ode\x12#\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeIDR\x06\x63odeId\x12\x42\n\tcode_info\x18\x02 \x01(\x0b\x32\x1a.cosmwasm.wasm.v1.CodeInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x08\x63odeInfo\x12\x1d\n\ncode_bytes\x18\x03 \x01(\x0cR\tcodeBytes\x12\x16\n\x06pinned\x18\x04 \x01(\x08R\x06pinned\"\xd5\x02\n\x08\x43ontract\x12\x43\n\x10\x63ontract_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0f\x63ontractAddress\x12N\n\rcontract_info\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.ContractInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x0c\x63ontractInfo\x12I\n\x0e\x63ontract_state\x18\x03 \x03(\x0b\x32\x17.cosmwasm.wasm.v1.ModelB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\rcontractState\x12i\n\x15\x63ontract_code_history\x18\x04 \x03(\x0b\x32*.cosmwasm.wasm.v1.ContractCodeHistoryEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x13\x63ontractCodeHistory\"B\n\x08Sequence\x12 \n\x06id_key\x18\x01 \x01(\x0c\x42\t\xe2\xde\x1f\x05IDKeyR\x05idKey\x12\x14\n\x05value\x18\x02 \x01(\x04R\x05valueB\xae\x01\n\x14\x63om.cosmwasm.wasm.v1B\x0cGenesisProtoP\x01Z&github.com/CosmWasm/wasmd/x/wasm/types\xa2\x02\x03\x43WX\xaa\x02\x10\x43osmwasm.Wasm.V1\xca\x02\x10\x43osmwasm\\Wasm\\V1\xe2\x02\x1c\x43osmwasm\\Wasm\\V1\\GPBMetadata\xea\x02\x12\x43osmwasm::Wasm::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.cosmwasm.wasm.v1B\014GenesisProtoP\001Z&github.com/CosmWasm/wasmd/x/wasm/types\242\002\003CWX\252\002\020Cosmwasm.Wasm.V1\312\002\020Cosmwasm\\Wasm\\V1\342\002\034Cosmwasm\\Wasm\\V1\\GPBMetadata\352\002\022Cosmwasm::Wasm::V1'
  _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['codes']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['codes']._serialized_options = b'\310\336\037\000\352\336\037\017codes,omitempty\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['contracts']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['contracts']._serialized_options = b'\310\336\037\000\352\336\037\023contracts,omitempty\250\347\260*\001'
  _globals['_GENESISSTATE'].fields_by_name['sequences']._loaded_options = None
  _globals['_GENESISSTATE'].fields_by_name['sequences']._serialized_options = b'\310\336\037\000\352\336\037\023sequences,omitempty\250\347\260*\001'
  _globals['_CODE'].fields_by_name['code_id']._loaded_options = None
  _globals['_CODE'].fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _globals['_CODE'].fields_by_name['code_info']._loaded_options = None
  _globals['_CODE'].fields_by_name['code_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_CONTRACT'].fields_by_name['contract_address']._loaded_options = None
  _globals['_CONTRACT'].fields_by_name['contract_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_CONTRACT'].fields_by_name['contract_info']._loaded_options = None
  _globals['_CONTRACT'].fields_by_name['contract_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_CONTRACT'].fields_by_name['contract_state']._loaded_options = None
  _globals['_CONTRACT'].fields_by_name['contract_state']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_CONTRACT'].fields_by_name['contract_code_history']._loaded_options = None
  _globals['_CONTRACT'].fields_by_name['contract_code_history']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_SEQUENCE'].fields_by_name['id_key']._loaded_options = None
  _globals['_SEQUENCE'].fields_by_name['id_key']._serialized_options = b'\342\336\037\005IDKey'
  _globals['_GENESISSTATE']._serialized_start=151
  _globals['_GENESISSTATE']._serialized_end=486
  _globals['_CODE']._serialized_start=489
  _globals['_CODE']._serialized_end=655
  _globals['_CONTRACT']._serialized_start=658
  _globals['_CONTRACT']._serialized_end=999
  _globals['_SEQUENCE']._serialized_start=1001
  _globals['_SEQUENCE']._serialized_end=1067
# @@protoc_insertion_point(module_scope)
