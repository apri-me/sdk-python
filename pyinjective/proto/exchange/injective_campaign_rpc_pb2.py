# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_campaign_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%exchange/injective_campaign_rpc.proto\x12\x16injective_campaign_rpc\"n\n\x0eRankingRequest\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x0c\n\x04skip\x18\x05 \x01(\x04\"\xaa\x01\n\x0fRankingResponse\x12\x32\n\x08\x63\x61mpaign\x18\x01 \x01(\x0b\x32 .injective_campaign_rpc.Campaign\x12\x33\n\x05users\x18\x02 \x03(\x0b\x32$.injective_campaign_rpc.CampaignUser\x12.\n\x06paging\x18\x03 \x01(\x0b\x32\x1e.injective_campaign_rpc.Paging\"\x99\x01\n\x08\x43\x61mpaign\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x13\n\x0btotal_score\x18\x04 \x01(\t\x12\x14\n\x0clast_updated\x18\x05 \x01(\x12\x12\x12\n\nstart_date\x18\x06 \x01(\x12\x12\x10\n\x08\x65nd_date\x18\x07 \x01(\x12\x12\x14\n\x0cis_claimable\x18\x08 \x01(\x08\"\xd3\x01\n\x0c\x43\x61mpaignUser\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x17\n\x0f\x61\x63\x63ount_address\x18\x03 \x01(\t\x12\r\n\x05score\x18\x04 \x01(\t\x12\x18\n\x10\x63ontract_updated\x18\x05 \x01(\x08\x12\x14\n\x0c\x62lock_height\x18\x06 \x01(\x12\x12\x12\n\nblock_time\x18\x07 \x01(\x12\x12\x18\n\x10purchased_amount\x18\x08 \x01(\t\x12\x15\n\rgalxe_updated\x18\t \x01(\x08\"\\\n\x06Paging\x12\r\n\x05total\x18\x01 \x01(\x12\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x11\x12\n\n\x02to\x18\x03 \x01(\x11\x12\x1b\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12\x12\x0c\n\x04next\x18\x05 \x03(\t\"\\\n\x11ListGuildsRequest\x12\x19\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x11\x12\x0c\n\x04skip\x18\x03 \x01(\x11\x12\x0f\n\x07sort_by\x18\x04 \x01(\t\"\xca\x01\n\x12ListGuildsResponse\x12-\n\x06guilds\x18\x01 \x03(\x0b\x32\x1d.injective_campaign_rpc.Guild\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x1e.injective_campaign_rpc.Paging\x12\x12\n\nupdated_at\x18\x03 \x01(\x12\x12\x41\n\x10\x63\x61mpaign_summary\x18\x04 \x01(\x0b\x32\'.injective_campaign_rpc.CampaignSummary\"\xb9\x02\n\x05Guild\x12\x19\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\t\x12\x10\n\x08guild_id\x18\x02 \x01(\t\x12\x16\n\x0emaster_address\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\x12\x12\x11\n\ttvl_score\x18\x05 \x01(\t\x12\x14\n\x0cvolume_score\x18\x06 \x01(\t\x12\x16\n\x0erank_by_volume\x18\x07 \x01(\x11\x12\x13\n\x0brank_by_tvl\x18\x08 \x01(\x11\x12\x0c\n\x04logo\x18\t \x01(\t\x12\x11\n\ttotal_tvl\x18\n \x01(\t\x12\x12\n\nupdated_at\x18\x0b \x01(\x12\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x11\n\tis_active\x18\r \x01(\x08\x12\x16\n\x0emaster_balance\x18\x0f \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x10 \x01(\t\"\xf8\x01\n\x0f\x43\x61mpaignSummary\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x19\n\x11\x63\x61mpaign_contract\x18\x02 \x01(\t\x12\x1a\n\x12total_guilds_count\x18\x03 \x01(\x11\x12\x11\n\ttotal_tvl\x18\x04 \x01(\t\x12\x19\n\x11total_average_tvl\x18\x05 \x01(\t\x12\x14\n\x0ctotal_volume\x18\x06 \x01(\t\x12\x12\n\nupdated_at\x18\x07 \x01(\x12\x12\x1b\n\x13total_members_count\x18\x08 \x01(\x11\x12\x12\n\nstart_time\x18\t \x01(\x12\x12\x10\n\x08\x65nd_time\x18\n \x01(\x12\"\x90\x01\n\x17ListGuildMembersRequest\x12\x19\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\t\x12\x10\n\x08guild_id\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x11\x12\x0c\n\x04skip\x18\x04 \x01(\x11\x12\x1a\n\x12include_guild_info\x18\x05 \x01(\x08\x12\x0f\n\x07sort_by\x18\x06 \x01(\t\"\xb3\x01\n\x18ListGuildMembersResponse\x12\x34\n\x07members\x18\x01 \x03(\x0b\x32#.injective_campaign_rpc.GuildMember\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x1e.injective_campaign_rpc.Paging\x12\x31\n\nguild_info\x18\x03 \x01(\x0b\x32\x1d.injective_campaign_rpc.Guild\"\xd9\x01\n\x0bGuildMember\x12\x19\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\t\x12\x10\n\x08guild_id\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x11\n\tjoined_at\x18\x04 \x01(\x12\x12\x11\n\ttvl_score\x18\x05 \x01(\t\x12\x14\n\x0cvolume_score\x18\x06 \x01(\t\x12\x11\n\ttotal_tvl\x18\x07 \x01(\t\x12\x1f\n\x17volume_score_percentage\x18\x08 \x01(\x01\x12\x1c\n\x14tvl_score_percentage\x18\t \x01(\x01\"C\n\x15GetGuildMemberRequest\x12\x19\n\x11\x63\x61mpaign_contract\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"K\n\x16GetGuildMemberResponse\x12\x31\n\x04info\x18\x01 \x01(\x0b\x32#.injective_campaign_rpc.GuildMember2\xbf\x03\n\x14InjectiveCampaignRPC\x12Z\n\x07Ranking\x12&.injective_campaign_rpc.RankingRequest\x1a\'.injective_campaign_rpc.RankingResponse\x12\x63\n\nListGuilds\x12).injective_campaign_rpc.ListGuildsRequest\x1a*.injective_campaign_rpc.ListGuildsResponse\x12u\n\x10ListGuildMembers\x12/.injective_campaign_rpc.ListGuildMembersRequest\x1a\x30.injective_campaign_rpc.ListGuildMembersResponse\x12o\n\x0eGetGuildMember\x12-.injective_campaign_rpc.GetGuildMemberRequest\x1a..injective_campaign_rpc.GetGuildMemberResponseB\x1bZ\x19/injective_campaign_rpcpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_campaign_rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\031/injective_campaign_rpcpb'
  _globals['_RANKINGREQUEST']._serialized_start=65
  _globals['_RANKINGREQUEST']._serialized_end=175
  _globals['_RANKINGRESPONSE']._serialized_start=178
  _globals['_RANKINGRESPONSE']._serialized_end=348
  _globals['_CAMPAIGN']._serialized_start=351
  _globals['_CAMPAIGN']._serialized_end=504
  _globals['_CAMPAIGNUSER']._serialized_start=507
  _globals['_CAMPAIGNUSER']._serialized_end=718
  _globals['_PAGING']._serialized_start=720
  _globals['_PAGING']._serialized_end=812
  _globals['_LISTGUILDSREQUEST']._serialized_start=814
  _globals['_LISTGUILDSREQUEST']._serialized_end=906
  _globals['_LISTGUILDSRESPONSE']._serialized_start=909
  _globals['_LISTGUILDSRESPONSE']._serialized_end=1111
  _globals['_GUILD']._serialized_start=1114
  _globals['_GUILD']._serialized_end=1427
  _globals['_CAMPAIGNSUMMARY']._serialized_start=1430
  _globals['_CAMPAIGNSUMMARY']._serialized_end=1678
  _globals['_LISTGUILDMEMBERSREQUEST']._serialized_start=1681
  _globals['_LISTGUILDMEMBERSREQUEST']._serialized_end=1825
  _globals['_LISTGUILDMEMBERSRESPONSE']._serialized_start=1828
  _globals['_LISTGUILDMEMBERSRESPONSE']._serialized_end=2007
  _globals['_GUILDMEMBER']._serialized_start=2010
  _globals['_GUILDMEMBER']._serialized_end=2227
  _globals['_GETGUILDMEMBERREQUEST']._serialized_start=2229
  _globals['_GETGUILDMEMBERREQUEST']._serialized_end=2296
  _globals['_GETGUILDMEMBERRESPONSE']._serialized_start=2298
  _globals['_GETGUILDMEMBERRESPONSE']._serialized_end=2373
  _globals['_INJECTIVECAMPAIGNRPC']._serialized_start=2376
  _globals['_INJECTIVECAMPAIGNRPC']._serialized_end=2823
# @@protoc_insertion_point(module_scope)
