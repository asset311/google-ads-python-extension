# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/enums/payment_mode.proto

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
  name='google/ads/googleads_v2/proto/enums/payment_mode.proto',
  package='google.ads.googleads.v2.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v2.enumsB\020PaymentModeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V2.Enums\312\002\035Google\\Ads\\GoogleAds\\V2\\Enums\352\002!Google::Ads::GoogleAds::V2::Enums'),
  serialized_pb=_b('\n6google/ads/googleads_v2/proto/enums/payment_mode.proto\x12\x1dgoogle.ads.googleads.v2.enums\x1a\x1cgoogle/api/annotations.proto\"q\n\x0fPaymentModeEnum\"^\n\x0bPaymentMode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06\x43LICKS\x10\x04\x12\x14\n\x10\x43ONVERSION_VALUE\x10\x05\x12\x0f\n\x0b\x43ONVERSIONS\x10\x06\x42\xe5\x01\n!com.google.ads.googleads.v2.enumsB\x10PaymentModeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v2/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V2.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V2\\Enums\xea\x02!Google::Ads::GoogleAds::V2::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_PAYMENTMODEENUM_PAYMENTMODE = _descriptor.EnumDescriptor(
  name='PaymentMode',
  full_name='google.ads.googleads.v2.enums.PaymentModeEnum.PaymentMode',
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
      name='CLICKS', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_VALUE', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSIONS', index=4, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=138,
  serialized_end=232,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTMODEENUM_PAYMENTMODE)


_PAYMENTMODEENUM = _descriptor.Descriptor(
  name='PaymentModeEnum',
  full_name='google.ads.googleads.v2.enums.PaymentModeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYMENTMODEENUM_PAYMENTMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=232,
)

_PAYMENTMODEENUM_PAYMENTMODE.containing_type = _PAYMENTMODEENUM
DESCRIPTOR.message_types_by_name['PaymentModeEnum'] = _PAYMENTMODEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentModeEnum = _reflection.GeneratedProtocolMessageType('PaymentModeEnum', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTMODEENUM,
  __module__ = 'google.ads.googleads_v2.proto.enums.payment_mode_pb2'
  ,
  __doc__ = """Container for enum describing possible payment modes.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.enums.PaymentModeEnum)
  ))
_sym_db.RegisterMessage(PaymentModeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
