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

from msrest.serialization import Model


class EncryptionSettingsElement(Model):
    """Encryption settings for one disk volume.

    :param disk_encryption_key: Key Vault Secret Url and vault id of the disk
     encryption key
    :type disk_encryption_key:
     ~azure.mgmt.compute.v2018_09_30.models.KeyVaultAndSecretReference
    :param key_encryption_key: Key Vault Key Url and vault id of the key
     encryption key. KeyEncryptionKey is optional and when provided is used to
     unwrap the disk encryption key.
    :type key_encryption_key:
     ~azure.mgmt.compute.v2018_09_30.models.KeyVaultAndKeyReference
    """

    _attribute_map = {
        'disk_encryption_key': {'key': 'diskEncryptionKey', 'type': 'KeyVaultAndSecretReference'},
        'key_encryption_key': {'key': 'keyEncryptionKey', 'type': 'KeyVaultAndKeyReference'},
    }

    def __init__(self, **kwargs):
        super(EncryptionSettingsElement, self).__init__(**kwargs)
        self.disk_encryption_key = kwargs.get('disk_encryption_key', None)
        self.key_encryption_key = kwargs.get('key_encryption_key', None)
