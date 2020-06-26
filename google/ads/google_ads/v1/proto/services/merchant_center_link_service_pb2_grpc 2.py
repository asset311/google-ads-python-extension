# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import merchant_center_link_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_merchant__center__link__pb2
from google.ads.google_ads.v1.proto.services import merchant_center_link_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2


class MerchantCenterLinkServiceStub(object):
  """Proto file describing the MerchantCenterLink service.

  This service allows management of links between Google Ads and Google
  Merchant Center.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListMerchantCenterLinks = channel.unary_unary(
        '/google.ads.googleads.v1.services.MerchantCenterLinkService/ListMerchantCenterLinks',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.ListMerchantCenterLinksRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.ListMerchantCenterLinksResponse.FromString,
        )
    self.GetMerchantCenterLink = channel.unary_unary(
        '/google.ads.googleads.v1.services.MerchantCenterLinkService/GetMerchantCenterLink',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.GetMerchantCenterLinkRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_merchant__center__link__pb2.MerchantCenterLink.FromString,
        )
    self.MutateMerchantCenterLink = channel.unary_unary(
        '/google.ads.googleads.v1.services.MerchantCenterLinkService/MutateMerchantCenterLink',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.MutateMerchantCenterLinkRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.MutateMerchantCenterLinkResponse.FromString,
        )


class MerchantCenterLinkServiceServicer(object):
  """Proto file describing the MerchantCenterLink service.

  This service allows management of links between Google Ads and Google
  Merchant Center.
  """

  def ListMerchantCenterLinks(self, request, context):
    """Returns Merchant Center links available tor this customer.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetMerchantCenterLink(self, request, context):
    """Returns the Merchant Center link in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateMerchantCenterLink(self, request, context):
    """Updates status or removes a Merchant Center link.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MerchantCenterLinkServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListMerchantCenterLinks': grpc.unary_unary_rpc_method_handler(
          servicer.ListMerchantCenterLinks,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.ListMerchantCenterLinksRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.ListMerchantCenterLinksResponse.SerializeToString,
      ),
      'GetMerchantCenterLink': grpc.unary_unary_rpc_method_handler(
          servicer.GetMerchantCenterLink,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.GetMerchantCenterLinkRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_merchant__center__link__pb2.MerchantCenterLink.SerializeToString,
      ),
      'MutateMerchantCenterLink': grpc.unary_unary_rpc_method_handler(
          servicer.MutateMerchantCenterLink,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.MutateMerchantCenterLinkRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_merchant__center__link__service__pb2.MutateMerchantCenterLinkResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.MerchantCenterLinkService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
