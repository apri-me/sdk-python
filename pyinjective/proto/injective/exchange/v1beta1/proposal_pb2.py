# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/exchange/v1beta1/proposal.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from pyinjective.proto.cosmos.distribution.v1beta1 import distribution_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_distribution__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.injective.exchange.v1beta1 import exchange_pb2 as injective_dot_exchange_dot_v1beta1_dot_exchange__pb2
from pyinjective.proto.injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)injective/exchange/v1beta1/proposal.proto\x12\x1ainjective.exchange.v1beta1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a.cosmos/distribution/v1beta1/distribution.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a)injective/exchange/v1beta1/exchange.proto\x1a%injective/oracle/v1beta1/oracle.proto\"\xb5\x04\n\x1dSpotMarketParamUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x46\n\x0emaker_fee_rate\x18\x04 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\x05 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16relayer_fee_share_rate\x18\x06 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\x07 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x08 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x38\n\x06status\x18\t \x01(\x0e\x32(.injective.exchange.v1beta1.MarketStatus:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x86\x01\n\x16\x45xchangeEnableProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12>\n\x0c\x65xchangeType\x18\x03 \x01(\x0e\x32(.injective.exchange.v1beta1.ExchangeType:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\"\xe7\t\n!BatchExchangeModificationProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x65\n\"spot_market_param_update_proposals\x18\x03 \x03(\x0b\x32\x39.injective.exchange.v1beta1.SpotMarketParamUpdateProposal\x12q\n(derivative_market_param_update_proposals\x18\x04 \x03(\x0b\x32?.injective.exchange.v1beta1.DerivativeMarketParamUpdateProposal\x12Z\n\x1cspot_market_launch_proposals\x18\x05 \x03(\x0b\x32\x34.injective.exchange.v1beta1.SpotMarketLaunchProposal\x12\x64\n!perpetual_market_launch_proposals\x18\x06 \x03(\x0b\x32\x39.injective.exchange.v1beta1.PerpetualMarketLaunchProposal\x12m\n&expiry_futures_market_launch_proposals\x18\x07 \x03(\x0b\x32=.injective.exchange.v1beta1.ExpiryFuturesMarketLaunchProposal\x12p\n\'trading_reward_campaign_update_proposal\x18\x08 \x01(\x0b\x32?.injective.exchange.v1beta1.TradingRewardCampaignUpdateProposal\x12m\n&binary_options_market_launch_proposals\x18\t \x03(\x0b\x32=.injective.exchange.v1beta1.BinaryOptionsMarketLaunchProposal\x12q\n%binary_options_param_update_proposals\x18\n \x03(\x0b\x32\x42.injective.exchange.v1beta1.BinaryOptionsMarketParamUpdateProposal\x12_\n\x1e\x64\x65nom_decimals_update_proposal\x18\x0b \x01(\x0b\x32\x37.injective.exchange.v1beta1.UpdateDenomDecimalsProposal\x12N\n\x15\x66\x65\x65_discount_proposal\x18\x0c \x01(\x0b\x32/.injective.exchange.v1beta1.FeeDiscountProposal\x12\x66\n\"market_forced_settlement_proposals\x18\r \x03(\x0b\x32:.injective.exchange.v1beta1.MarketForcedSettlementProposal:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xcc\x03\n\x18SpotMarketLaunchProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x12\n\nbase_denom\x18\x04 \x01(\t\x12\x13\n\x0bquote_denom\x18\x05 \x01(\t\x12K\n\x13min_price_tick_size\x18\x06 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x07 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0emaker_fee_rate\x18\x08 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\t \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xe0\x05\n\x1dPerpetualMarketLaunchProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x13\n\x0bquote_denom\x18\x04 \x01(\t\x12\x13\n\x0boracle_base\x18\x05 \x01(\t\x12\x14\n\x0coracle_quote\x18\x06 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x07 \x01(\r\x12\x39\n\x0boracle_type\x18\x08 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12L\n\x14initial_margin_ratio\x18\t \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12P\n\x18maintenance_margin_ratio\x18\n \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0emaker_fee_rate\x18\x0b \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\x0c \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\r \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x0e \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x94\x05\n!BinaryOptionsMarketLaunchProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x15\n\roracle_symbol\x18\x04 \x01(\t\x12\x17\n\x0foracle_provider\x18\x05 \x01(\t\x12\x39\n\x0boracle_type\x18\x06 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x1b\n\x13oracle_scale_factor\x18\x07 \x01(\r\x12\x1c\n\x14\x65xpiration_timestamp\x18\x08 \x01(\x03\x12\x1c\n\x14settlement_timestamp\x18\t \x01(\x03\x12\r\n\x05\x61\x64min\x18\n \x01(\t\x12\x13\n\x0bquote_denom\x18\x0b \x01(\t\x12\x46\n\x0emaker_fee_rate\x18\x0c \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\r \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\x0e \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x0f \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xf4\x05\n!ExpiryFuturesMarketLaunchProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x13\n\x0bquote_denom\x18\x04 \x01(\t\x12\x13\n\x0boracle_base\x18\x05 \x01(\t\x12\x14\n\x0coracle_quote\x18\x06 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x07 \x01(\r\x12\x39\n\x0boracle_type\x18\x08 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x0e\n\x06\x65xpiry\x18\t \x01(\x03\x12L\n\x14initial_margin_ratio\x18\n \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12P\n\x18maintenance_margin_ratio\x18\x0b \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0emaker_fee_rate\x18\x0c \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\r \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\x0e \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x0f \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xb6\x07\n#DerivativeMarketParamUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12L\n\x14initial_margin_ratio\x18\x04 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12P\n\x18maintenance_margin_ratio\x18\x05 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0emaker_fee_rate\x18\x06 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\x07 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16relayer_fee_share_rate\x18\x08 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\t \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\n \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12J\n\x12HourlyInterestRate\x18\x0b \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12L\n\x14HourlyFundingRateCap\x18\x0c \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x38\n\x06status\x18\r \x01(\x0e\x32(.injective.exchange.v1beta1.MarketStatus\x12?\n\roracle_params\x18\x0e \x01(\x0b\x32(.injective.exchange.v1beta1.OracleParams:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xc9\x01\n\x1eMarketForcedSettlementProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12H\n\x10settlement_price\x18\x04 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xac\x01\n\x1bUpdateDenomDecimalsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x41\n\x0e\x64\x65nom_decimals\x18\x03 \x03(\x0b\x32).injective.exchange.v1beta1.DenomDecimals:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x9c\x06\n&BinaryOptionsMarketParamUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x46\n\x0emaker_fee_rate\x18\x04 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x46\n\x0etaker_fee_rate\x18\x05 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16relayer_fee_share_rate\x18\x06 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12K\n\x13min_price_tick_size\x18\x07 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12N\n\x16min_quantity_tick_size\x18\x08 \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\x1c\n\x14\x65xpiration_timestamp\x18\t \x01(\x03\x12\x1c\n\x14settlement_timestamp\x18\n \x01(\x03\x12H\n\x10settlement_price\x18\x0b \x01(\tB.\xc8\xde\x1f\x01\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12\r\n\x05\x61\x64min\x18\x0c \x01(\t\x12\x38\n\x06status\x18\r \x01(\x0e\x32(.injective.exchange.v1beta1.MarketStatus\x12G\n\roracle_params\x18\x0e \x01(\x0b\x32\x30.injective.exchange.v1beta1.ProviderOracleParams:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x90\x01\n\x14ProviderOracleParams\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x03 \x01(\r\x12\x39\n\x0boracle_type\x18\x04 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\"\x91\x01\n\x0cOracleParams\x12\x13\n\x0boracle_base\x18\x01 \x01(\t\x12\x14\n\x0coracle_quote\x18\x02 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x03 \x01(\r\x12\x39\n\x0boracle_type\x18\x04 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\"\x8e\x02\n#TradingRewardCampaignLaunchProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12L\n\rcampaign_info\x18\x03 \x01(\x0b\x32\x35.injective.exchange.v1beta1.TradingRewardCampaignInfo\x12M\n\x15\x63\x61mpaign_reward_pools\x18\x04 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xef\x02\n#TradingRewardCampaignUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12L\n\rcampaign_info\x18\x03 \x01(\x0b\x32\x35.injective.exchange.v1beta1.TradingRewardCampaignInfo\x12W\n\x1f\x63\x61mpaign_reward_pools_additions\x18\x04 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool\x12U\n\x1d\x63\x61mpaign_reward_pools_updates\x18\x05 \x03(\x0b\x32..injective.exchange.v1beta1.CampaignRewardPool:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"p\n\x11RewardPointUpdate\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x01 \x01(\t\x12\x42\n\nnew_points\x18\x0c \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\"\xe3\x01\n(TradingRewardPendingPointsUpdateProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x16pending_pool_timestamp\x18\x03 \x01(\x03\x12K\n\x14reward_point_updates\x18\x04 \x03(\x0b\x32-.injective.exchange.v1beta1.RewardPointUpdate:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xa4\x01\n\x13\x46\x65\x65\x44iscountProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x41\n\x08schedule\x18\x03 \x01(\x0b\x32/.injective.exchange.v1beta1.FeeDiscountSchedule:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xb9\x01\n\x1f\x42\x61tchCommunityPoolSpendProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12J\n\tproposals\x18\x03 \x03(\x0b\x32\x37.cosmos.distribution.v1beta1.CommunityPoolSpendProposal:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\xcd\x01\n.AtomicMarketOrderFeeMultiplierScheduleProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12O\n\x16market_fee_multipliers\x18\x03 \x03(\x0b\x32/.injective.exchange.v1beta1.MarketFeeMultiplier:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content*x\n\x0c\x45xchangeType\x12\x32\n\x14\x45XCHANGE_UNSPECIFIED\x10\x00\x1a\x18\x8a\x9d \x14\x45XCHANGE_UNSPECIFIED\x12\x12\n\x04SPOT\x10\x01\x1a\x08\x8a\x9d \x04SPOT\x12 \n\x0b\x44\x45RIVATIVES\x10\x02\x1a\x0f\x8a\x9d \x0b\x44\x45RIVATIVESBPZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.exchange.v1beta1.proposal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZNgithub.com/InjectiveLabs/injective-core/injective-chain/modules/exchange/types'
  _globals['_EXCHANGETYPE'].values_by_name["EXCHANGE_UNSPECIFIED"]._loaded_options = None
  _globals['_EXCHANGETYPE'].values_by_name["EXCHANGE_UNSPECIFIED"]._serialized_options = b'\212\235 \024EXCHANGE_UNSPECIFIED'
  _globals['_EXCHANGETYPE'].values_by_name["SPOT"]._loaded_options = None
  _globals['_EXCHANGETYPE'].values_by_name["SPOT"]._serialized_options = b'\212\235 \004SPOT'
  _globals['_EXCHANGETYPE'].values_by_name["DERIVATIVES"]._loaded_options = None
  _globals['_EXCHANGETYPE'].values_by_name["DERIVATIVES"]._serialized_options = b'\212\235 \013DERIVATIVES'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL']._loaded_options = None
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_EXCHANGEENABLEPROPOSAL']._loaded_options = None
  _globals['_EXCHANGEENABLEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000'
  _globals['_BATCHEXCHANGEMODIFICATIONPROPOSAL']._loaded_options = None
  _globals['_BATCHEXCHANGEMODIFICATIONPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_SPOTMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_SPOTMARKETLAUNCHPROPOSAL']._loaded_options = None
  _globals['_SPOTMARKETLAUNCHPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['initial_margin_ratio']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['initial_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['maintenance_margin_ratio']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['maintenance_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL']._loaded_options = None
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['initial_margin_ratio']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['initial_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['maintenance_margin_ratio']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['maintenance_margin_ratio']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL']._loaded_options = None
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['initial_margin_ratio']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['initial_margin_ratio']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maintenance_margin_ratio']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maintenance_margin_ratio']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['HourlyInterestRate']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['HourlyInterestRate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['HourlyFundingRateCap']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL'].fields_by_name['HourlyFundingRateCap']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL']._loaded_options = None
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL'].fields_by_name['settlement_price']._loaded_options = None
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL'].fields_by_name['settlement_price']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL']._loaded_options = None
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_UPDATEDENOMDECIMALSPROPOSAL']._loaded_options = None
  _globals['_UPDATEDENOMDECIMALSPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['maker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['taker_fee_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['relayer_fee_share_rate']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_price_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['min_quantity_tick_size']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['settlement_price']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL'].fields_by_name['settlement_price']._serialized_options = b'\310\336\037\001\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL']._loaded_options = None
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_TRADINGREWARDCAMPAIGNLAUNCHPROPOSAL']._loaded_options = None
  _globals['_TRADINGREWARDCAMPAIGNLAUNCHPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_TRADINGREWARDCAMPAIGNUPDATEPROPOSAL']._loaded_options = None
  _globals['_TRADINGREWARDCAMPAIGNUPDATEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_REWARDPOINTUPDATE'].fields_by_name['new_points']._loaded_options = None
  _globals['_REWARDPOINTUPDATE'].fields_by_name['new_points']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _globals['_TRADINGREWARDPENDINGPOINTSUPDATEPROPOSAL']._loaded_options = None
  _globals['_TRADINGREWARDPENDINGPOINTSUPDATEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_FEEDISCOUNTPROPOSAL']._loaded_options = None
  _globals['_FEEDISCOUNTPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_BATCHCOMMUNITYPOOLSPENDPROPOSAL']._loaded_options = None
  _globals['_BATCHCOMMUNITYPOOLSPENDPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_ATOMICMARKETORDERFEEMULTIPLIERSCHEDULEPROPOSAL']._loaded_options = None
  _globals['_ATOMICMARKETORDERFEEMULTIPLIERSCHEDULEPROPOSAL']._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_EXCHANGETYPE']._serialized_start=8872
  _globals['_EXCHANGETYPE']._serialized_end=8992
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL']._serialized_start=310
  _globals['_SPOTMARKETPARAMUPDATEPROPOSAL']._serialized_end=875
  _globals['_EXCHANGEENABLEPROPOSAL']._serialized_start=878
  _globals['_EXCHANGEENABLEPROPOSAL']._serialized_end=1012
  _globals['_BATCHEXCHANGEMODIFICATIONPROPOSAL']._serialized_start=1015
  _globals['_BATCHEXCHANGEMODIFICATIONPROPOSAL']._serialized_end=2270
  _globals['_SPOTMARKETLAUNCHPROPOSAL']._serialized_start=2273
  _globals['_SPOTMARKETLAUNCHPROPOSAL']._serialized_end=2733
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL']._serialized_start=2736
  _globals['_PERPETUALMARKETLAUNCHPROPOSAL']._serialized_end=3472
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL']._serialized_start=3475
  _globals['_BINARYOPTIONSMARKETLAUNCHPROPOSAL']._serialized_end=4135
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL']._serialized_start=4138
  _globals['_EXPIRYFUTURESMARKETLAUNCHPROPOSAL']._serialized_end=4894
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL']._serialized_start=4897
  _globals['_DERIVATIVEMARKETPARAMUPDATEPROPOSAL']._serialized_end=5847
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL']._serialized_start=5850
  _globals['_MARKETFORCEDSETTLEMENTPROPOSAL']._serialized_end=6051
  _globals['_UPDATEDENOMDECIMALSPROPOSAL']._serialized_start=6054
  _globals['_UPDATEDENOMDECIMALSPROPOSAL']._serialized_end=6226
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL']._serialized_start=6229
  _globals['_BINARYOPTIONSMARKETPARAMUPDATEPROPOSAL']._serialized_end=7025
  _globals['_PROVIDERORACLEPARAMS']._serialized_start=7028
  _globals['_PROVIDERORACLEPARAMS']._serialized_end=7172
  _globals['_ORACLEPARAMS']._serialized_start=7175
  _globals['_ORACLEPARAMS']._serialized_end=7320
  _globals['_TRADINGREWARDCAMPAIGNLAUNCHPROPOSAL']._serialized_start=7323
  _globals['_TRADINGREWARDCAMPAIGNLAUNCHPROPOSAL']._serialized_end=7593
  _globals['_TRADINGREWARDCAMPAIGNUPDATEPROPOSAL']._serialized_start=7596
  _globals['_TRADINGREWARDCAMPAIGNUPDATEPROPOSAL']._serialized_end=7963
  _globals['_REWARDPOINTUPDATE']._serialized_start=7965
  _globals['_REWARDPOINTUPDATE']._serialized_end=8077
  _globals['_TRADINGREWARDPENDINGPOINTSUPDATEPROPOSAL']._serialized_start=8080
  _globals['_TRADINGREWARDPENDINGPOINTSUPDATEPROPOSAL']._serialized_end=8307
  _globals['_FEEDISCOUNTPROPOSAL']._serialized_start=8310
  _globals['_FEEDISCOUNTPROPOSAL']._serialized_end=8474
  _globals['_BATCHCOMMUNITYPOOLSPENDPROPOSAL']._serialized_start=8477
  _globals['_BATCHCOMMUNITYPOOLSPENDPROPOSAL']._serialized_end=8662
  _globals['_ATOMICMARKETORDERFEEMULTIPLIERSCHEDULEPROPOSAL']._serialized_start=8665
  _globals['_ATOMICMARKETORDERFEEMULTIPLIERSCHEDULEPROPOSAL']._serialized_end=8870
# @@protoc_insertion_point(module_scope)
