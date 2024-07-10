# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cosmos/distribution/v1beta1/tx.proto
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
    'cosmos/distribution/v1beta1/tx.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2
from pyinjective.proto.cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/distribution/v1beta1/tx.proto\x12\x1b\x63osmos.distribution.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\"\xeb\x01\n\x15MsgSetWithdrawAddress\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12\x43\n\x10withdraw_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x0fwithdrawAddress:F\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*#cosmos-sdk/MsgModifyWithdrawAddress\"\x1f\n\x1dMsgSetWithdrawAddressResponse\"\xfe\x01\n\x1aMsgWithdrawDelegatorReward\x12\x45\n\x11\x64\x65legator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x10\x64\x65legatorAddress\x12N\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress:I\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11\x64\x65legator_address\x8a\xe7\xb0*&cosmos-sdk/MsgWithdrawDelegationReward\"\x9f\x01\n\"MsgWithdrawDelegatorRewardResponse\x12y\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount\"\xb8\x01\n\x1eMsgWithdrawValidatorCommission\x12N\n\x11validator_address\x18\x01 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress:F\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*#cosmos-sdk/MsgWithdrawValCommission\"\xa3\x01\n&MsgWithdrawValidatorCommissionResponse\x12y\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount\"\x85\x02\n\x14MsgFundCommunityPool\x12y\n\x06\x61mount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount\x12\x36\n\tdepositor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tdepositor::\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*\x1f\x63osmos-sdk/MsgFundCommunityPool\"\x1e\n\x1cMsgFundCommunityPoolResponse\"\xcd\x01\n\x0fMsgUpdateParams\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x46\n\x06params\x18\x02 \x01(\x0b\x32#.cosmos.distribution.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x06params::\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\'cosmos-sdk/distribution/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xa3\x02\n\x15MsgCommunityPoolSpend\x12\x36\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tauthority\x12\x1c\n\trecipient\x18\x02 \x01(\tR\trecipient\x12y\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount:9\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*&cosmos-sdk/distr/MsgCommunityPoolSpend\"\x1f\n\x1dMsgCommunityPoolSpendResponse\"\xe5\x02\n\x1eMsgDepositValidatorRewardsPool\x12\x36\n\tdepositor\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\tdepositor\x12N\n\x11validator_address\x18\x02 \x01(\tB!\xd2\xb4-\x1d\x63osmos.ValidatorAddressStringR\x10validatorAddress\x12y\n\x06\x61mount\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x9a\xe7\xb0*\x0clegacy_coins\xa8\xe7\xb0*\x01R\x06\x61mount:@\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\tdepositor\x8a\xe7\xb0*%cosmos-sdk/distr/MsgDepositValRewards\"(\n&MsgDepositValidatorRewardsPoolResponse2\xec\x07\n\x03Msg\x12\x84\x01\n\x12SetWithdrawAddress\x12\x32.cosmos.distribution.v1beta1.MsgSetWithdrawAddress\x1a:.cosmos.distribution.v1beta1.MsgSetWithdrawAddressResponse\x12\x93\x01\n\x17WithdrawDelegatorReward\x12\x37.cosmos.distribution.v1beta1.MsgWithdrawDelegatorReward\x1a?.cosmos.distribution.v1beta1.MsgWithdrawDelegatorRewardResponse\x12\x9f\x01\n\x1bWithdrawValidatorCommission\x12;.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommission\x1a\x43.cosmos.distribution.v1beta1.MsgWithdrawValidatorCommissionResponse\x12\x81\x01\n\x11\x46undCommunityPool\x12\x31.cosmos.distribution.v1beta1.MsgFundCommunityPool\x1a\x39.cosmos.distribution.v1beta1.MsgFundCommunityPoolResponse\x12r\n\x0cUpdateParams\x12,.cosmos.distribution.v1beta1.MsgUpdateParams\x1a\x34.cosmos.distribution.v1beta1.MsgUpdateParamsResponse\x12\x84\x01\n\x12\x43ommunityPoolSpend\x12\x32.cosmos.distribution.v1beta1.MsgCommunityPoolSpend\x1a:.cosmos.distribution.v1beta1.MsgCommunityPoolSpendResponse\x12\x9f\x01\n\x1b\x44\x65positValidatorRewardsPool\x12;.cosmos.distribution.v1beta1.MsgDepositValidatorRewardsPool\x1a\x43.cosmos.distribution.v1beta1.MsgDepositValidatorRewardsPoolResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xef\x01\n\x1f\x63om.cosmos.distribution.v1beta1B\x07TxProtoP\x01Z1github.com/cosmos/cosmos-sdk/x/distribution/types\xa2\x02\x03\x43\x44X\xaa\x02\x1b\x43osmos.Distribution.V1beta1\xca\x02\x1b\x43osmos\\Distribution\\V1beta1\xe2\x02\'Cosmos\\Distribution\\V1beta1\\GPBMetadata\xea\x02\x1d\x43osmos::Distribution::V1beta1\xa8\xe2\x1e\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.distribution.v1beta1.tx_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.cosmos.distribution.v1beta1B\007TxProtoP\001Z1github.com/cosmos/cosmos-sdk/x/distribution/types\242\002\003CDX\252\002\033Cosmos.Distribution.V1beta1\312\002\033Cosmos\\Distribution\\V1beta1\342\002\'Cosmos\\Distribution\\V1beta1\\GPBMetadata\352\002\035Cosmos::Distribution::V1beta1\250\342\036\001'
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['withdraw_address']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS'].fields_by_name['withdraw_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGSETWITHDRAWADDRESS']._loaded_options = None
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address\212\347\260*#cosmos-sdk/MsgModifyWithdrawAddress'
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['delegator_address']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['delegator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGWITHDRAWDELEGATORREWARD']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021delegator_address\212\347\260*&cosmos-sdk/MsgWithdrawDelegationReward'
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\021validator_address\212\347\260*#cosmos-sdk/MsgWithdrawValCommission'
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['depositor']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGFUNDCOMMUNITYPOOL']._loaded_options = None
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tdepositor\212\347\260*\037cosmos-sdk/MsgFundCommunityPool'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._loaded_options = None
  _globals['_MSGUPDATEPARAMS'].fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _globals['_MSGUPDATEPARAMS']._loaded_options = None
  _globals['_MSGUPDATEPARAMS']._serialized_options = b'\202\347\260*\tauthority\212\347\260*\'cosmos-sdk/distribution/MsgUpdateParams'
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['authority']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGCOMMUNITYPOOLSPEND']._loaded_options = None
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_options = b'\202\347\260*\tauthority\212\347\260*&cosmos-sdk/distr/MsgCommunityPoolSpend'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['depositor']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['depositor']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['validator_address']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['validator_address']._serialized_options = b'\322\264-\035cosmos.ValidatorAddressString'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['amount']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL'].fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\232\347\260*\014legacy_coins\250\347\260*\001'
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._loaded_options = None
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\tdepositor\212\347\260*%cosmos-sdk/distr/MsgDepositValRewards'
  _globals['_MSG']._loaded_options = None
  _globals['_MSG']._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_start=243
  _globals['_MSGSETWITHDRAWADDRESS']._serialized_end=478
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_start=480
  _globals['_MSGSETWITHDRAWADDRESSRESPONSE']._serialized_end=511
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_start=514
  _globals['_MSGWITHDRAWDELEGATORREWARD']._serialized_end=768
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_start=771
  _globals['_MSGWITHDRAWDELEGATORREWARDRESPONSE']._serialized_end=930
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_start=933
  _globals['_MSGWITHDRAWVALIDATORCOMMISSION']._serialized_end=1117
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_start=1120
  _globals['_MSGWITHDRAWVALIDATORCOMMISSIONRESPONSE']._serialized_end=1283
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_start=1286
  _globals['_MSGFUNDCOMMUNITYPOOL']._serialized_end=1547
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_start=1549
  _globals['_MSGFUNDCOMMUNITYPOOLRESPONSE']._serialized_end=1579
  _globals['_MSGUPDATEPARAMS']._serialized_start=1582
  _globals['_MSGUPDATEPARAMS']._serialized_end=1787
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1789
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1814
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_start=1817
  _globals['_MSGCOMMUNITYPOOLSPEND']._serialized_end=2108
  _globals['_MSGCOMMUNITYPOOLSPENDRESPONSE']._serialized_start=2110
  _globals['_MSGCOMMUNITYPOOLSPENDRESPONSE']._serialized_end=2141
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_start=2144
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOL']._serialized_end=2501
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOLRESPONSE']._serialized_start=2503
  _globals['_MSGDEPOSITVALIDATORREWARDSPOOLRESPONSE']._serialized_end=2543
  _globals['_MSG']._serialized_start=2546
  _globals['_MSG']._serialized_end=3550
# @@protoc_insertion_point(module_scope)
