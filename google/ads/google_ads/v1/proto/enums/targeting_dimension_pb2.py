# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/targeting_dimension.proto

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
  name='google/ads/googleads_v1/proto/enums/targeting_dimension.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\027TargetingDimensionProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n=google/ads/googleads_v1/proto/enums/targeting_dimension.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xc4\x01\n\x16TargetingDimensionEnum\"\xa9\x01\n\x12TargetingDimension\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07KEYWORD\x10\x02\x12\x0c\n\x08\x41UDIENCE\x10\x03\x12\t\n\x05TOPIC\x10\x04\x12\n\n\x06GENDER\x10\x05\x12\r\n\tAGE_RANGE\x10\x06\x12\r\n\tPLACEMENT\x10\x07\x12\x13\n\x0fPARENTAL_STATUS\x10\x08\x12\x10\n\x0cINCOME_RANGE\x10\tB\xec\x01\n!com.google.ads.googleads.v1.enumsB\x17TargetingDimensionProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TARGETINGDIMENSIONENUM_TARGETINGDIMENSION = _descriptor.EnumDescriptor(
  name='TargetingDimension',
  full_name='google.ads.googleads.v1.enums.TargetingDimensionEnum.TargetingDimension',
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
      name='KEYWORD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIENCE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOPIC', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENDER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGE_RANGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEMENT', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARENTAL_STATUS', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_TARGETINGDIMENSIONENUM_TARGETINGDIMENSION)


_TARGETINGDIMENSIONENUM = _descriptor.Descriptor(
  name='TargetingDimensionEnum',
  full_name='google.ads.googleads.v1.enums.TargetingDimensionEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TARGETINGDIMENSIONENUM_TARGETINGDIMENSION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=323,
)

_TARGETINGDIMENSIONENUM_TARGETINGDIMENSION.containing_type = _TARGETINGDIMENSIONENUM
DESCRIPTOR.message_types_by_name['TargetingDimensionEnum'] = _TARGETINGDIMENSIONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TargetingDimensionEnum = _reflection.GeneratedProtocolMessageType('TargetingDimensionEnum', (_message.Message,), dict(
  DESCRIPTOR = _TARGETINGDIMENSIONENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.targeting_dimension_pb2'
  ,
  __doc__ = """The dimensions that can be targeted.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.TargetingDimensionEnum)
  ))
_sym_db.RegisterMessage(TargetingDimensionEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
