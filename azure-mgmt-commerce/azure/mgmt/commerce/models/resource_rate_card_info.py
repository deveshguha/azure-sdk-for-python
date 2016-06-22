# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResourceRateCardInfo(Model):
    """Price and Metadata information for resources.

    :param currency: The currency in which the rates are provided.
    :type currency: str
    :param locale: The culture in which the resource information is localized.
    :type locale: str
    :param is_tax_included: All rates are pretax, so this will always be
     returned as 'false'.
    :type is_tax_included: bool
    :param meter_region: The region in which the Azure service is available.
    :type meter_region: str
    :param tags: Provides additional meter data. 'Third Party' indicates a
     meter with no discount. Blanks indicate First Party.
    :type tags: list of str
    :param offer_terms: A list of offer terms.
    :type offer_terms: list of :class:`OfferTermInfo
     <azure.mgmt.commerce.models.OfferTermInfo>`
    :param meters: A list of meters.
    :type meters: list of :class:`MeterInfo
     <azure.mgmt.commerce.models.MeterInfo>`
    """ 

    _attribute_map = {
        'currency': {'key': 'Currency', 'type': 'str'},
        'locale': {'key': 'Locale', 'type': 'str'},
        'is_tax_included': {'key': 'IsTaxIncluded', 'type': 'bool'},
        'meter_region': {'key': 'MeterRegion', 'type': 'str'},
        'tags': {'key': 'Tags', 'type': '[str]'},
        'offer_terms': {'key': 'OfferTerms', 'type': '[OfferTermInfo]'},
        'meters': {'key': 'Meters', 'type': '[MeterInfo]'},
    }

    def __init__(self, currency=None, locale=None, is_tax_included=None, meter_region=None, tags=None, offer_terms=None, meters=None):
        self.currency = currency
        self.locale = locale
        self.is_tax_included = is_tax_included
        self.meter_region = meter_region
        self.tags = tags
        self.offer_terms = offer_terms
        self.meters = meters
