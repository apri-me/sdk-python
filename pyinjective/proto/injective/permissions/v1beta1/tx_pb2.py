# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: injective/permissions/v1beta1/tx.proto
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
    'injective/permissions/v1beta1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.injective.permissions.v1beta1 import params_pb2 as injective_dot_permissions_dot_v1beta1_dot_params__pb2
from pyinjective.proto.injective.permissions.v1beta1 import permissions_pb2 as injective_dot_permissions_dot_v1beta1_dot_permissions__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&injective/permissions/v1beta1/tx.proto\x12\x1dinjective.permissions.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a*injective/permissions/v1beta1/params.proto\x1a/injective/permissions/v1beta1/permissions.proto\x1a\x11\x61mino/amino.proto\"\xbe\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x43\n\x06params\x18\x02 \x01(\x0b\x32%.injective.permissions.v1beta1.ParamsB\x04\xc8\xde\x1f\x00R\x06params:.\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1bpermissions/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xbd\x01\n\x12MsgCreateNamespace\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12L\n\tnamespace\x18\x02 \x01(\x0b\x32(.injective.permissions.v1beta1.NamespaceB\x04\xc8\xde\x1f\x00R\tnamespace:.\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1epermissions/MsgCreateNamespace\"\x1c\n\x1aMsgCreateNamespaceResponse\"\x98\x01\n\x12MsgDeleteNamespace\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\'\n\x0fnamespace_denom\x18\x02 \x01(\tR\x0enamespaceDenom:.\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1epermissions/MsgDeleteNamespace\"\x1c\n\x1aMsgDeleteNamespaceResponse\"\xf4\x05\n\x12MsgUpdateNamespace\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\'\n\x0fnamespace_denom\x18\x02 \x01(\tR\x0enamespaceDenom\x12]\n\twasm_hook\x18\x03 \x01(\x0b\x32@.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetWasmHookR\x08wasmHook\x12\x66\n\x0cmints_paused\x18\x04 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetMintsPausedR\x0bmintsPaused\x12\x66\n\x0csends_paused\x18\x05 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetSendsPausedR\x0bsendsPaused\x12\x66\n\x0c\x62urns_paused\x18\x06 \x01(\x0b\x32\x43.injective.permissions.v1beta1.MsgUpdateNamespace.MsgSetBurnsPausedR\x0b\x62urnsPaused\x1a-\n\x0eMsgSetWasmHook\x12\x1b\n\tnew_value\x18\x01 \x01(\tR\x08newValue\x1a\x30\n\x11MsgSetMintsPaused\x12\x1b\n\tnew_value\x18\x01 \x01(\x08R\x08newValue\x1a\x30\n\x11MsgSetSendsPaused\x12\x1b\n\tnew_value\x18\x01 \x01(\x08R\x08newValue\x1a\x30\n\x11MsgSetBurnsPaused\x12\x1b\n\tnew_value\x18\x01 \x01(\x08R\x08newValue:.\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1epermissions/MsgUpdateNamespace\"\x1c\n\x1aMsgUpdateNamespaceResponse\"\xc4\x02\n\x17MsgUpdateNamespaceRoles\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\'\n\x0fnamespace_denom\x18\x02 \x01(\tR\x0enamespaceDenom\x12N\n\x10role_permissions\x18\x03 \x03(\x0b\x32#.injective.permissions.v1beta1.RoleR\x0frolePermissions\x12P\n\raddress_roles\x18\x04 \x03(\x0b\x32+.injective.permissions.v1beta1.AddressRolesR\x0c\x61\x64\x64ressRoles:3\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*#permissions/MsgUpdateNamespaceRoles\"!\n\x1fMsgUpdateNamespaceRolesResponse\"\x86\x02\n\x17MsgRevokeNamespaceRoles\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\'\n\x0fnamespace_denom\x18\x02 \x01(\tR\x0enamespaceDenom\x12\x62\n\x17\x61\x64\x64ress_roles_to_revoke\x18\x03 \x03(\x0b\x32+.injective.permissions.v1beta1.AddressRolesR\x14\x61\x64\x64ressRolesToRevoke:3\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*#permissions/MsgRevokeNamespaceRoles\"!\n\x1fMsgRevokeNamespaceRolesResponse\"\x7f\n\x0fMsgClaimVoucher\x12)\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"R\x06sender\x12\x14\n\x05\x64\x65nom\x18\x02 \x01(\tR\x05\x64\x65nom:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bpermissions/MsgClaimVoucher\"\x19\n\x17MsgClaimVoucherResponse2\xa1\x07\n\x03Msg\x12v\n\x0cUpdateParams\x12..injective.permissions.v1beta1.MsgUpdateParams\x1a\x36.injective.permissions.v1beta1.MsgUpdateParamsResponse\x12\x7f\n\x0f\x43reateNamespace\x12\x31.injective.permissions.v1beta1.MsgCreateNamespace\x1a\x39.injective.permissions.v1beta1.MsgCreateNamespaceResponse\x12\x7f\n\x0f\x44\x65leteNamespace\x12\x31.injective.permissions.v1beta1.MsgDeleteNamespace\x1a\x39.injective.permissions.v1beta1.MsgDeleteNamespaceResponse\x12\x7f\n\x0fUpdateNamespace\x12\x31.injective.permissions.v1beta1.MsgUpdateNamespace\x1a\x39.injective.permissions.v1beta1.MsgUpdateNamespaceResponse\x12\x8e\x01\n\x14UpdateNamespaceRoles\x12\x36.injective.permissions.v1beta1.MsgUpdateNamespaceRoles\x1a>.injective.permissions.v1beta1.MsgUpdateNamespaceRolesResponse\x12\x8e\x01\n\x14RevokeNamespaceRoles\x12\x36.injective.permissions.v1beta1.MsgRevokeNamespaceRoles\x1a>.injective.permissions.v1beta1.MsgRevokeNamespaceRolesResponse\x12v\n\x0c\x43laimVoucher\x12..injective.permissions.v1beta1.MsgClaimVoucher\x1a\x36.injective.permissions.v1beta1.MsgClaimVoucherResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x95\x02\n!com.injective.permissions.v1beta1B\x07TxProtoP\x01ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\xa2\x02\x03IPX\xaa\x02\x1dInjective.Permissions.V1beta1\xca\x02\x1dInjective\\Permissions\\V1beta1\xe2\x02)Injective\\Permissions\\V1beta1\\GPBMetadata\xea\x02\x1fInjective::Permissions::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.permissions.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.injective.permissions.v1beta1B\007TxProtoP\001ZQgithub.com/InjectiveLabs/injective-core/injective-chain/modules/permissions/types\242\002\003IPX\252\002\035Injective.Permissions.V1beta1\312\002\035Injective\\Permissions\\V1beta1\342\002)Injective\\Permissions\\V1beta1\\GPBMetadata\352\002\037Injective::Permissions::V1beta1'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\033permissions/MsgUpdateParams'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._loaded_options = None
  _globals['_MSGCREATENAMESPACE'].fields_by_name['namespace']._serialized_options = b'\310\336\037\000'
  _globals['_MSGCREATENAMESPACE']._loaded_options = None
  _globals['_MSGCREATENAMESPACE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\036permissions/MsgCreateNamespace'
  _globals['_MSGDELETENAMESPACE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGDELETENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGDELETENAMESPACE']._loaded_options = None
  _globals['_MSGDELETENAMESPACE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\036permissions/MsgDeleteNamespace'
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATENAMESPACE'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATENAMESPACE']._loaded_options = None
  _globals['_MSGUPDATENAMESPACE']._serialized_options = b'\202\347\260*\006sender\212\347\260*\036permissions/MsgUpdateNamespace'
  _globals['_MSGUPDATENAMESPACEROLES'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGUPDATENAMESPACEROLES'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGUPDATENAMESPACEROLES']._loaded_options = None
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_options = b'\202\347\260*\006sender\212\347\260*#permissions/MsgUpdateNamespaceRoles'
  _globals['_MSGREVOKENAMESPACEROLES'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGREVOKENAMESPACEROLES'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGREVOKENAMESPACEROLES']._loaded_options = None
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_options = b'\202\347\260*\006sender\212\347\260*#permissions/MsgRevokeNamespaceRoles'
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._loaded_options = None
  _globals['_MSGCLAIMVOUCHER'].fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _globals['_MSGCLAIMVOUCHER']._loaded_options = None
  _globals['_MSGCLAIMVOUCHER']._serialized_options = b'\202\347\260*\006sender\212\347\260*\033permissions/MsgClaimVoucher'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._serialized_start=324
  _globals['_MSGUPDATEPARAMS']._serialized_end=514
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=516
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=541
  _globals['_MSGCREATENAMESPACE']._serialized_start=544
  _globals['_MSGCREATENAMESPACE']._serialized_end=733
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_start=735
  _globals['_MSGCREATENAMESPACERESPONSE']._serialized_end=763
  _globals['_MSGDELETENAMESPACE']._serialized_start=766
  _globals['_MSGDELETENAMESPACE']._serialized_end=918
  _globals['_MSGDELETENAMESPACERESPONSE']._serialized_start=920
  _globals['_MSGDELETENAMESPACERESPONSE']._serialized_end=948
  _globals['_MSGUPDATENAMESPACE']._serialized_start=951
  _globals['_MSGUPDATENAMESPACE']._serialized_end=1707
  _globals['_MSGUPDATENAMESPACE_MSGSETWASMHOOK']._serialized_start=1464
  _globals['_MSGUPDATENAMESPACE_MSGSETWASMHOOK']._serialized_end=1509
  _globals['_MSGUPDATENAMESPACE_MSGSETMINTSPAUSED']._serialized_start=1511
  _globals['_MSGUPDATENAMESPACE_MSGSETMINTSPAUSED']._serialized_end=1559
  _globals['_MSGUPDATENAMESPACE_MSGSETSENDSPAUSED']._serialized_start=1561
  _globals['_MSGUPDATENAMESPACE_MSGSETSENDSPAUSED']._serialized_end=1609
  _globals['_MSGUPDATENAMESPACE_MSGSETBURNSPAUSED']._serialized_start=1611
  _globals['_MSGUPDATENAMESPACE_MSGSETBURNSPAUSED']._serialized_end=1659
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_start=1709
  _globals['_MSGUPDATENAMESPACERESPONSE']._serialized_end=1737
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_start=1740
  _globals['_MSGUPDATENAMESPACEROLES']._serialized_end=2064
  _globals['_MSGUPDATENAMESPACEROLESRESPONSE']._serialized_start=2066
  _globals['_MSGUPDATENAMESPACEROLESRESPONSE']._serialized_end=2099
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_start=2102
  _globals['_MSGREVOKENAMESPACEROLES']._serialized_end=2364
  _globals['_MSGREVOKENAMESPACEROLESRESPONSE']._serialized_start=2366
  _globals['_MSGREVOKENAMESPACEROLESRESPONSE']._serialized_end=2399
  _globals['_MSGCLAIMVOUCHER']._serialized_start=2401
  _globals['_MSGCLAIMVOUCHER']._serialized_end=2528
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_start=2530
  _globals['_MSGCLAIMVOUCHERRESPONSE']._serialized_end=2555
  _globals['_MSG']._serialized_start=2558
  _globals['_MSG']._serialized_end=3487
# @@protoc_insertion_point(module_scope)
