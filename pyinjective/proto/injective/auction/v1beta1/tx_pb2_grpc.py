# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from injective.auction.v1beta1 import tx_pb2 as injective_dot_auction_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the auction Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Bid = channel.unary_unary(
                '/injective.auction.v1beta1.Msg/Bid',
                request_serializer=injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBid.SerializeToString,
                response_deserializer=injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBidResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the auction Msg service.
    """

    def Bid(self, request, context):
        """Bid defines a method for placing a bid for an auction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Bid': grpc.unary_unary_rpc_method_handler(
                    servicer.Bid,
                    request_deserializer=injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBid.FromString,
                    response_serializer=injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBidResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.auction.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the auction Msg service.
    """

    @staticmethod
    def Bid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective.auction.v1beta1.Msg/Bid',
            injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBid.SerializeToString,
            injective_dot_auction_dot_v1beta1_dot_tx__pb2.MsgBidResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
