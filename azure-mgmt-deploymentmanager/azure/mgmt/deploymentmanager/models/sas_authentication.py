# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .authentication import Authentication


class SasAuthentication(Authentication):
    """Defines the properties to access the artifacts using an Azure Storage SAS
    URI.

    :param type: Constant filled by server.
    :type type: str
    :param sas_uri: The SAS URI to the Azure Storage blob container. Any
     offset from the root of the container to where the artifacts are located
     can be defined in the artifactRoot.
    :type sas_uri: str
    """

    _validation = {
        'type': {'required': True},
        'sas_uri': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'sas_uri': {'key': 'properties.sasUri', 'type': 'str'},
    }

    def __init__(self, sas_uri):
        super(SasAuthentication, self).__init__()
        self.sas_uri = sas_uri
        self.type = 'Sas'
