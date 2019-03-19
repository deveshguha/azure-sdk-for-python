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


class WaitStepAttributes(Model):
    """The parameters for the wait step.

    :param duration: The duration in ISO 8601 format of how long the wait
     should be.
    :type duration: str
    """

    _validation = {
        'duration': {'required': True},
    }

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'str'},
    }

    def __init__(self, duration):
        super(WaitStepAttributes, self).__init__()
        self.duration = duration
