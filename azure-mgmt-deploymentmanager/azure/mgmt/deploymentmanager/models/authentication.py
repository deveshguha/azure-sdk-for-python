# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Authentication(Model):
    """Defines the authentication method and properties to access the artifacts.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SasAuthentication

    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'Sas': 'SasAuthentication'}
    }

    def __init__(self):
        super(Authentication, self).__init__()
        self.type = None
