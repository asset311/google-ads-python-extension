# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/ad_error.proto

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
  name='google/ads/googleads_v1/proto/errors/ad_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\014AdErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\n3google/ads/googleads_v1/proto/errors/ad_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\xf0 \n\x0b\x41\x64\x45rrorEnum\"\xe0 \n\x07\x41\x64\x45rror\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12,\n(AD_CUSTOMIZERS_NOT_SUPPORTED_FOR_AD_TYPE\x10\x02\x12\x1a\n\x16\x41PPROXIMATELY_TOO_LONG\x10\x03\x12\x1b\n\x17\x41PPROXIMATELY_TOO_SHORT\x10\x04\x12\x0f\n\x0b\x42\x41\x44_SNIPPET\x10\x05\x12\x14\n\x10\x43\x41NNOT_MODIFY_AD\x10\x06\x12\'\n#CANNOT_SET_BUSINESS_NAME_IF_URL_SET\x10\x07\x12\x14\n\x10\x43\x41NNOT_SET_FIELD\x10\x08\x12*\n&CANNOT_SET_FIELD_WITH_ORIGIN_AD_ID_SET\x10\t\x12/\n+CANNOT_SET_FIELD_WITH_AD_ID_SET_FOR_SHARING\x10\n\x12)\n%CANNOT_SET_ALLOW_FLEXIBLE_COLOR_FALSE\x10\x0b\x12\x37\n3CANNOT_SET_COLOR_CONTROL_WHEN_NATIVE_FORMAT_SETTING\x10\x0c\x12\x12\n\x0e\x43\x41NNOT_SET_URL\x10\r\x12!\n\x1d\x43\x41NNOT_SET_WITHOUT_FINAL_URLS\x10\x0e\x12\x1e\n\x1a\x43\x41NNOT_SET_WITH_FINAL_URLS\x10\x0f\x12\x1c\n\x18\x43\x41NNOT_SET_WITH_URL_DATA\x10\x11\x12\'\n#CANNOT_USE_AD_SUBCLASS_FOR_OPERATOR\x10\x12\x12#\n\x1f\x43USTOMER_NOT_APPROVED_MOBILEADS\x10\x13\x12(\n$CUSTOMER_NOT_APPROVED_THIRDPARTY_ADS\x10\x14\x12\x31\n-CUSTOMER_NOT_APPROVED_THIRDPARTY_REDIRECT_ADS\x10\x15\x12\x19\n\x15\x43USTOMER_NOT_ELIGIBLE\x10\x16\x12\x31\n-CUSTOMER_NOT_ELIGIBLE_FOR_UPDATING_BEACON_URL\x10\x17\x12\x1e\n\x1a\x44IMENSION_ALREADY_IN_UNION\x10\x18\x12\x19\n\x15\x44IMENSION_MUST_BE_SET\x10\x19\x12\x1a\n\x16\x44IMENSION_NOT_IN_UNION\x10\x1a\x12#\n\x1f\x44ISPLAY_URL_CANNOT_BE_SPECIFIED\x10\x1b\x12 \n\x1c\x44OMESTIC_PHONE_NUMBER_FORMAT\x10\x1c\x12\x1a\n\x16\x45MERGENCY_PHONE_NUMBER\x10\x1d\x12\x0f\n\x0b\x45MPTY_FIELD\x10\x1e\x12\x30\n,FEED_ATTRIBUTE_MUST_HAVE_MAPPING_FOR_TYPE_ID\x10\x1f\x12(\n$FEED_ATTRIBUTE_MAPPING_TYPE_MISMATCH\x10 \x12!\n\x1dILLEGAL_AD_CUSTOMIZER_TAG_USE\x10!\x12\x13\n\x0fILLEGAL_TAG_USE\x10\"\x12\x1b\n\x17INCONSISTENT_DIMENSIONS\x10#\x12)\n%INCONSISTENT_STATUS_IN_TEMPLATE_UNION\x10$\x12\x14\n\x10INCORRECT_LENGTH\x10%\x12\x1a\n\x16INELIGIBLE_FOR_UPGRADE\x10&\x12&\n\"INVALID_AD_ADDRESS_CAMPAIGN_TARGET\x10\'\x12\x13\n\x0fINVALID_AD_TYPE\x10(\x12\'\n#INVALID_ATTRIBUTES_FOR_MOBILE_IMAGE\x10)\x12&\n\"INVALID_ATTRIBUTES_FOR_MOBILE_TEXT\x10*\x12\x1f\n\x1bINVALID_CALL_TO_ACTION_TEXT\x10+\x12\x1d\n\x19INVALID_CHARACTER_FOR_URL\x10,\x12\x18\n\x14INVALID_COUNTRY_CODE\x10-\x12*\n&INVALID_EXPANDED_DYNAMIC_SEARCH_AD_TAG\x10/\x12\x11\n\rINVALID_INPUT\x10\x30\x12\x1b\n\x17INVALID_MARKUP_LANGUAGE\x10\x31\x12\x1a\n\x16INVALID_MOBILE_CARRIER\x10\x32\x12!\n\x1dINVALID_MOBILE_CARRIER_TARGET\x10\x33\x12\x1e\n\x1aINVALID_NUMBER_OF_ELEMENTS\x10\x34\x12\x1f\n\x1bINVALID_PHONE_NUMBER_FORMAT\x10\x35\x12\x31\n-INVALID_RICH_MEDIA_CERTIFIED_VENDOR_FORMAT_ID\x10\x36\x12\x19\n\x15INVALID_TEMPLATE_DATA\x10\x37\x12\'\n#INVALID_TEMPLATE_ELEMENT_FIELD_TYPE\x10\x38\x12\x17\n\x13INVALID_TEMPLATE_ID\x10\x39\x12\x11\n\rLINE_TOO_WIDE\x10:\x12!\n\x1dMISSING_AD_CUSTOMIZER_MAPPING\x10;\x12\x1d\n\x19MISSING_ADDRESS_COMPONENT\x10<\x12\x1e\n\x1aMISSING_ADVERTISEMENT_NAME\x10=\x12\x19\n\x15MISSING_BUSINESS_NAME\x10>\x12\x18\n\x14MISSING_DESCRIPTION1\x10?\x12\x18\n\x14MISSING_DESCRIPTION2\x10@\x12\x1f\n\x1bMISSING_DESTINATION_URL_TAG\x10\x41\x12 \n\x1cMISSING_LANDING_PAGE_URL_TAG\x10\x42\x12\x15\n\x11MISSING_DIMENSION\x10\x43\x12\x17\n\x13MISSING_DISPLAY_URL\x10\x44\x12\x14\n\x10MISSING_HEADLINE\x10\x45\x12\x12\n\x0eMISSING_HEIGHT\x10\x46\x12\x11\n\rMISSING_IMAGE\x10G\x12-\n)MISSING_MARKETING_IMAGE_OR_PRODUCT_VIDEOS\x10H\x12\x1c\n\x18MISSING_MARKUP_LANGUAGES\x10I\x12\x1a\n\x16MISSING_MOBILE_CARRIER\x10J\x12\x11\n\rMISSING_PHONE\x10K\x12$\n MISSING_REQUIRED_TEMPLATE_FIELDS\x10L\x12 \n\x1cMISSING_TEMPLATE_FIELD_VALUE\x10M\x12\x10\n\x0cMISSING_TEXT\x10N\x12\x17\n\x13MISSING_VISIBLE_URL\x10O\x12\x11\n\rMISSING_WIDTH\x10P\x12\'\n#MULTIPLE_DISTINCT_FEEDS_UNSUPPORTED\x10Q\x12$\n MUST_USE_TEMP_AD_UNION_ID_ON_ADD\x10R\x12\x0c\n\x08TOO_LONG\x10S\x12\r\n\tTOO_SHORT\x10T\x12\"\n\x1eUNION_DIMENSIONS_CANNOT_CHANGE\x10U\x12\x1d\n\x19UNKNOWN_ADDRESS_COMPONENT\x10V\x12\x16\n\x12UNKNOWN_FIELD_NAME\x10W\x12\x17\n\x13UNKNOWN_UNIQUE_NAME\x10X\x12\x1a\n\x16UNSUPPORTED_DIMENSIONS\x10Y\x12\x16\n\x12URL_INVALID_SCHEME\x10Z\x12 \n\x1cURL_INVALID_TOP_LEVEL_DOMAIN\x10[\x12\x11\n\rURL_MALFORMED\x10\\\x12\x0f\n\x0bURL_NO_HOST\x10]\x12\x16\n\x12URL_NOT_EQUIVALENT\x10^\x12\x1a\n\x16URL_HOST_NAME_TOO_LONG\x10_\x12\x11\n\rURL_NO_SCHEME\x10`\x12\x1b\n\x17URL_NO_TOP_LEVEL_DOMAIN\x10\x61\x12\x18\n\x14URL_PATH_NOT_ALLOWED\x10\x62\x12\x18\n\x14URL_PORT_NOT_ALLOWED\x10\x63\x12\x19\n\x15URL_QUERY_NOT_ALLOWED\x10\x64\x12\x34\n0URL_SCHEME_BEFORE_EXPANDED_DYNAMIC_SEARCH_AD_TAG\x10\x66\x12)\n%USER_DOES_NOT_HAVE_ACCESS_TO_TEMPLATE\x10g\x12$\n INCONSISTENT_EXPANDABLE_SETTINGS\x10h\x12\x12\n\x0eINVALID_FORMAT\x10i\x12\x16\n\x12INVALID_FIELD_TEXT\x10j\x12\x17\n\x13\x45LEMENT_NOT_PRESENT\x10k\x12\x0f\n\x0bIMAGE_ERROR\x10l\x12\x16\n\x12VALUE_NOT_IN_RANGE\x10m\x12\x15\n\x11\x46IELD_NOT_PRESENT\x10n\x12\x18\n\x14\x41\x44\x44RESS_NOT_COMPLETE\x10o\x12\x13\n\x0f\x41\x44\x44RESS_INVALID\x10p\x12\x19\n\x15VIDEO_RETRIEVAL_ERROR\x10q\x12\x0f\n\x0b\x41UDIO_ERROR\x10r\x12\x1f\n\x1bINVALID_YOUTUBE_DISPLAY_URL\x10s\x12\x1b\n\x17TOO_MANY_PRODUCT_IMAGES\x10t\x12\x1b\n\x17TOO_MANY_PRODUCT_VIDEOS\x10u\x12.\n*INCOMPATIBLE_AD_TYPE_AND_DEVICE_PREFERENCE\x10v\x12*\n&CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10w\x12-\n)CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED\x10x\x12\x1a\n\x16\x44ISALLOWED_NUMBER_TYPE\x10y\x12*\n&PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY\x10z\x12<\n8PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY\x10{\x12#\n\x1fPREMIUM_RATE_NUMBER_NOT_ALLOWED\x10|\x12#\n\x1fVANITY_PHONE_NUMBER_NOT_ALLOWED\x10}\x12#\n\x1fINVALID_CALL_CONVERSION_TYPE_ID\x10~\x12=\n9CANNOT_DISABLE_CALL_CONVERSION_AND_SET_CONVERSION_TYPE_ID\x10\x7f\x12#\n\x1e\x43\x41NNOT_SET_PATH2_WITHOUT_PATH1\x10\x80\x01\x12\x33\n.MISSING_DYNAMIC_SEARCH_ADS_SETTING_DOMAIN_NAME\x10\x81\x01\x12\'\n\"INCOMPATIBLE_WITH_RESTRICTION_TYPE\x10\x82\x01\x12\x31\n,CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED\x10\x83\x01\x12\"\n\x1dMISSING_IMAGE_OR_MEDIA_BUNDLE\x10\x84\x01\x12\x30\n+PRODUCT_TYPE_NOT_SUPPORTED_IN_THIS_CAMPAIGN\x10\x85\x01\x42\xe7\x01\n\"com.google.ads.googleads.v1.errorsB\x0c\x41\x64\x45rrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADERRORENUM_ADERROR = _descriptor.EnumDescriptor(
  name='AdError',
  full_name='google.ads.googleads.v1.errors.AdErrorEnum.AdError',
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
      name='AD_CUSTOMIZERS_NOT_SUPPORTED_FOR_AD_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROXIMATELY_TOO_LONG', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROXIMATELY_TOO_SHORT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_SNIPPET', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_AD', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_BUSINESS_NAME_IF_URL_SET', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_FIELD', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_FIELD_WITH_ORIGIN_AD_ID_SET', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_FIELD_WITH_AD_ID_SET_FOR_SHARING', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_ALLOW_FLEXIBLE_COLOR_FALSE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_COLOR_CONTROL_WHEN_NATIVE_FORMAT_SETTING', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_URL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITHOUT_FINAL_URLS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITH_FINAL_URLS', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITH_URL_DATA', index=16, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_USE_AD_SUBCLASS_FOR_OPERATOR', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_APPROVED_MOBILEADS', index=18, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_APPROVED_THIRDPARTY_ADS', index=19, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_APPROVED_THIRDPARTY_REDIRECT_ADS', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_ELIGIBLE', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_ELIGIBLE_FOR_UPDATING_BEACON_URL', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIMENSION_ALREADY_IN_UNION', index=23, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIMENSION_MUST_BE_SET', index=24, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIMENSION_NOT_IN_UNION', index=25, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_URL_CANNOT_BE_SPECIFIED', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOMESTIC_PHONE_NUMBER_FORMAT', index=27, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY_PHONE_NUMBER', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY_FIELD', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_ATTRIBUTE_MUST_HAVE_MAPPING_FOR_TYPE_ID', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_ATTRIBUTE_MAPPING_TYPE_MISMATCH', index=31, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_AD_CUSTOMIZER_TAG_USE', index=32, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_TAG_USE', index=33, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_DIMENSIONS', index=34, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_STATUS_IN_TEMPLATE_UNION', index=35, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCORRECT_LENGTH', index=36, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INELIGIBLE_FOR_UPGRADE', index=37, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AD_ADDRESS_CAMPAIGN_TARGET', index=38, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_AD_TYPE', index=39, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ATTRIBUTES_FOR_MOBILE_IMAGE', index=40, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ATTRIBUTES_FOR_MOBILE_TEXT', index=41, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CALL_TO_ACTION_TEXT', index=42, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CHARACTER_FOR_URL', index=43, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COUNTRY_CODE', index=44, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EXPANDED_DYNAMIC_SEARCH_AD_TAG', index=45, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=46, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MARKUP_LANGUAGE', index=47, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MOBILE_CARRIER', index=48, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MOBILE_CARRIER_TARGET', index=49, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_NUMBER_OF_ELEMENTS', index=50, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PHONE_NUMBER_FORMAT', index=51, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_RICH_MEDIA_CERTIFIED_VENDOR_FORMAT_ID', index=52, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TEMPLATE_DATA', index=53, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TEMPLATE_ELEMENT_FIELD_TYPE', index=54, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TEMPLATE_ID', index=55, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINE_TOO_WIDE', index=56, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_AD_CUSTOMIZER_MAPPING', index=57, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_ADDRESS_COMPONENT', index=58, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_ADVERTISEMENT_NAME', index=59, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_BUSINESS_NAME', index=60, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DESCRIPTION1', index=61, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DESCRIPTION2', index=62, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DESTINATION_URL_TAG', index=63, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_LANDING_PAGE_URL_TAG', index=64, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DIMENSION', index=65, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DISPLAY_URL', index=66, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_HEADLINE', index=67, number=69,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_HEIGHT', index=68, number=70,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_IMAGE', index=69, number=71,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_MARKETING_IMAGE_OR_PRODUCT_VIDEOS', index=70, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_MARKUP_LANGUAGES', index=71, number=73,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_MOBILE_CARRIER', index=72, number=74,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_PHONE', index=73, number=75,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_REQUIRED_TEMPLATE_FIELDS', index=74, number=76,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_TEMPLATE_FIELD_VALUE', index=75, number=77,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_TEXT', index=76, number=78,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_VISIBLE_URL', index=77, number=79,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_WIDTH', index=78, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_DISTINCT_FEEDS_UNSUPPORTED', index=79, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUST_USE_TEMP_AD_UNION_ID_ON_ADD', index=80, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_LONG', index=81, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_SHORT', index=82, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNION_DIMENSIONS_CANNOT_CHANGE', index=83, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ADDRESS_COMPONENT', index=84, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_FIELD_NAME', index=85, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_UNIQUE_NAME', index=86, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_DIMENSIONS', index=87, number=89,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_INVALID_SCHEME', index=88, number=90,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_INVALID_TOP_LEVEL_DOMAIN', index=89, number=91,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_MALFORMED', index=90, number=92,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_NO_HOST', index=91, number=93,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_NOT_EQUIVALENT', index=92, number=94,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_HOST_NAME_TOO_LONG', index=93, number=95,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_NO_SCHEME', index=94, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_NO_TOP_LEVEL_DOMAIN', index=95, number=97,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_PATH_NOT_ALLOWED', index=96, number=98,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_PORT_NOT_ALLOWED', index=97, number=99,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_QUERY_NOT_ALLOWED', index=98, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_SCHEME_BEFORE_EXPANDED_DYNAMIC_SEARCH_AD_TAG', index=99, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_DOES_NOT_HAVE_ACCESS_TO_TEMPLATE', index=100, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_EXPANDABLE_SETTINGS', index=101, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FORMAT', index=102, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FIELD_TEXT', index=103, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_NOT_PRESENT', index=104, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_ERROR', index=105, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_NOT_IN_RANGE', index=106, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_NOT_PRESENT', index=107, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_NOT_COMPLETE', index=108, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_INVALID', index=109, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_RETRIEVAL_ERROR', index=110, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIO_ERROR', index=111, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_YOUTUBE_DISPLAY_URL', index=112, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_PRODUCT_IMAGES', index=113, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_PRODUCT_VIDEOS', index=114, number=117,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_AD_TYPE_AND_DEVICE_PREFERENCE', index=115, number=118,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY', index=116, number=119,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED', index=117, number=120,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISALLOWED_NUMBER_TYPE', index=118, number=121,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY', index=119, number=122,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY', index=120, number=123,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM_RATE_NUMBER_NOT_ALLOWED', index=121, number=124,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VANITY_PHONE_NUMBER_NOT_ALLOWED', index=122, number=125,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CALL_CONVERSION_TYPE_ID', index=123, number=126,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_DISABLE_CALL_CONVERSION_AND_SET_CONVERSION_TYPE_ID', index=124, number=127,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_PATH2_WITHOUT_PATH1', index=125, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_DYNAMIC_SEARCH_ADS_SETTING_DOMAIN_NAME', index=126, number=129,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_WITH_RESTRICTION_TYPE', index=127, number=130,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED', index=128, number=131,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_IMAGE_OR_MEDIA_BUNDLE', index=129, number=132,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TYPE_NOT_SUPPORTED_IN_THIS_CAMPAIGN', index=130, number=133,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=134,
  serialized_end=4326,
)
_sym_db.RegisterEnumDescriptor(_ADERRORENUM_ADERROR)


_ADERRORENUM = _descriptor.Descriptor(
  name='AdErrorEnum',
  full_name='google.ads.googleads.v1.errors.AdErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADERRORENUM_ADERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=4326,
)

_ADERRORENUM_ADERROR.containing_type = _ADERRORENUM
DESCRIPTOR.message_types_by_name['AdErrorEnum'] = _ADERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdErrorEnum = _reflection.GeneratedProtocolMessageType('AdErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.ad_error_pb2'
  ,
  __doc__ = """Container for enum describing possible ad errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.AdErrorEnum)
  ))
_sym_db.RegisterMessage(AdErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
