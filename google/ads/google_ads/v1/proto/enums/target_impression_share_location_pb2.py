# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/target_impression_share_location.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/target_impression_share_location.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\"TargetImpressionShareLocationProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nJgoogle/ads/googleads_v1/proto/enums/target_impression_share_location.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xa3\x01\n!TargetImpressionShareLocationEnum\"~\n\x1dTargetImpressionShareLocation\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x14\n\x10\x41NYWHERE_ON_PAGE\x10\x02\x12\x0f\n\x0bTOP_OF_PAGE\x10\x03\x12\x18\n\x14\x41\x42SOLUTE_TOP_OF_PAGE\x10\x04\x42\xf7\x01\n!com.google.ads.googleads.v1.enumsB\"TargetImpressionShareLocationProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TARGETIMPRESSIONSHARELOCATIONENUM_TARGETIMPRESSIONSHARELOCATION = _descriptor.EnumDescriptor(
  name='TargetImpressionShareLocation',
  full_name='google.ads.googleads.v1.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANYWHERE_ON_PAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP_OF_PAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABSOLUTE_TOP_OF_PAGE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=177,
  serialized_end=303,
)
_sym_db.RegisterEnumDescriptor(_TARGETIMPRESSIONSHARELOCATIONENUM_TARGETIMPRESSIONSHARELOCATION)


_TARGETIMPRESSIONSHARELOCATIONENUM = _descriptor.Descriptor(
  name='TargetImpressionShareLocationEnum',
  full_name='google.ads.googleads.v1.enums.TargetImpressionShareLocationEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TARGETIMPRESSIONSHARELOCATIONENUM_TARGETIMPRESSIONSHARELOCATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=303,
)

_TARGETIMPRESSIONSHARELOCATIONENUM_TARGETIMPRESSIONSHARELOCATION.containing_type = _TARGETIMPRESSIONSHARELOCATIONENUM
DESCRIPTOR.message_types_by_name['TargetImpressionShareLocationEnum'] = _TARGETIMPRESSIONSHARELOCATIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetImpressionShareLocationEnum = _reflection.GeneratedProtocolMessageType('TargetImpressionShareLocationEnum', (_message.Message,), dict(
  DESCRIPTOR = _TARGETIMPRESSIONSHARELOCATIONENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.target_impression_share_location_pb2'
  ,
  __doc__ = """Container for enum describing where on the first search results page the
  automated bidding system should target impressions for the
  TargetImpressionShare bidding strategy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.TargetImpressionShareLocationEnum)
  ))
_sym_db.RegisterMessage(TargetImpressionShareLocationEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
