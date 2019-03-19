# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceProperties(Model):
    """The properties of a service.

    :param target_location: The Azure location to which the resources in the
     service belong to or should be deployed to.
    :type target_location: str
    :param target_subscription_id: The subscription to which the resources in
     the service belong to or should be deployed to.
    :type target_subscription_id: str
    """

    _validation = {
        'target_location': {'required': True},
        'target_subscription_id': {'required': True},
    }

    _attribute_map = {
        'target_location': {'key': 'targetLocation', 'type': 'str'},
        'target_subscription_id': {'key': 'targetSubscriptionId', 'type': 'str'},
    }

    def __init__(self, target_location, target_subscription_id):
        super(ServiceProperties, self).__init__()
        self.target_location = target_location
        self.target_subscription_id = target_subscription_id
