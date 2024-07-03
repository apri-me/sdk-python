# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from pyinjective.proto.injective.oracle.v1beta1 import tx_pb2 as injective_dot_oracle_dot_v1beta1_dot_tx__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in injective/oracle/v1beta1/tx_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class MsgStub(object):
    """Msg defines the oracle Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RelayProviderPrices = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayProviderPrices',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPrices.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPricesResponse.FromString,
                _registered_method=True)
        self.RelayPriceFeedPrice = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayPriceFeedPrice',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.FromString,
                _registered_method=True)
        self.RelayBandRates = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayBandRates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.FromString,
                _registered_method=True)
        self.RequestBandIBCRates = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RequestBandIBCRates',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.FromString,
                _registered_method=True)
        self.RelayCoinbaseMessages = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayCoinbaseMessages',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.FromString,
                _registered_method=True)
        self.RelayPythPrices = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/RelayPythPrices',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPrices.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPricesResponse.FromString,
                _registered_method=True)
        self.UpdateParams = channel.unary_unary(
                '/injective.oracle.v1beta1.Msg/UpdateParams',
                request_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
                response_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the oracle Msg service.
    """

    def RelayProviderPrices(self, request, context):
        """RelayProviderPrice defines a method for relaying a price for a
        provider-based oracle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayPriceFeedPrice(self, request, context):
        """RelayPriceFeedPrice defines a method for relaying a price for a price
        feeder-based oracle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayBandRates(self, request, context):
        """RelayBandRates defines a method for relaying rates from Band
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestBandIBCRates(self, request, context):
        """RequestBandIBCRates defines a method for fetching rates from Band ibc
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayCoinbaseMessages(self, request, context):
        """RelayCoinbaseMessages defines a method for relaying price messages from
        Coinbase API
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelayPythPrices(self, request, context):
        """RelayPythPrices defines a method for relaying rates from the Pyth contract
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParams(self, request, context):
        """UpdateParams enables updating oracle module's params via governance
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RelayProviderPrices': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayProviderPrices,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPrices.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPricesResponse.SerializeToString,
            ),
            'RelayPriceFeedPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayPriceFeedPrice,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.SerializeToString,
            ),
            'RelayBandRates': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayBandRates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.SerializeToString,
            ),
            'RequestBandIBCRates': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestBandIBCRates,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.SerializeToString,
            ),
            'RelayCoinbaseMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayCoinbaseMessages,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.SerializeToString,
            ),
            'RelayPythPrices': grpc.unary_unary_rpc_method_handler(
                    servicer.RelayPythPrices,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPrices.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPricesResponse.SerializeToString,
            ),
            'UpdateParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateParams,
                    request_deserializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.FromString,
                    response_serializer=injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.oracle.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.oracle.v1beta1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the oracle Msg service.
    """

    @staticmethod
    def RelayProviderPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RelayProviderPrices',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPrices.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayProviderPricesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RelayPriceFeedPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RelayPriceFeedPrice',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPrice.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPriceFeedPriceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RelayBandRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RelayBandRates',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRates.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayBandRatesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RequestBandIBCRates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RequestBandIBCRates',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRates.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRequestBandIBCRatesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RelayCoinbaseMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RelayCoinbaseMessages',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessages.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayCoinbaseMessagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RelayPythPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/RelayPythPrices',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPrices.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgRelayPythPricesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.oracle.v1beta1.Msg/UpdateParams',
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            injective_dot_oracle_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
