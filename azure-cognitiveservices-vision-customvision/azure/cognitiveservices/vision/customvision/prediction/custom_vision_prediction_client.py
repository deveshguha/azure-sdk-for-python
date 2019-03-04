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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from . import models


class CustomVisionPredictionClientConfiguration(Configuration):
    """Configuration for CustomVisionPredictionClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param api_key: API key.
    :type api_key: str
    :param endpoint: Supported Cognitive Services endpoints.
    :type endpoint: str
    """

    def __init__(
            self, api_key, endpoint):

        if api_key is None:
            raise ValueError("Parameter 'api_key' must not be None.")
        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        base_url = '{Endpoint}/customvision/v3.0/prediction'

        super(CustomVisionPredictionClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-vision-customvision/{}'.format(VERSION))

        self.api_key = api_key
        self.endpoint = endpoint


class CustomVisionPredictionClient(SDKClient):
    """CustomVisionPredictionClient

    :ivar config: Configuration for client.
    :vartype config: CustomVisionPredictionClientConfiguration

    :param api_key: API key.
    :type api_key: str
    :param endpoint: Supported Cognitive Services endpoints.
    :type endpoint: str
    """

    def __init__(
            self, api_key, endpoint):

        self.config = CustomVisionPredictionClientConfiguration(api_key, endpoint)
        super(CustomVisionPredictionClient, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '3.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def classify_image_url(
            self, project_id, published_model_name, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Classify an image url and saves the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param url: Url of the image.
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.classify_image_url.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    classify_image_url.metadata = {'url': '/{projectId}/classify/models/{publishedModelName}/url'}

    def classify_image(
            self, project_id, published_model_name, image_data, application=None, custom_headers=None, raw=False, **operation_config):
        """Classify an image and saves the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param image_data: Binary image data.
        :type image_data: Generator
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        # Construct URL
        url = self.classify_image.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    classify_image.metadata = {'url': '/{projectId}/classify/models/{publishedModelName}/image'}

    def classify_image_url_with_no_store(
            self, project_id, published_model_name, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Classify an image url without saving the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param url: Url of the image.
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.classify_image_url_with_no_store.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    classify_image_url_with_no_store.metadata = {'url': '/{projectId}/classify/models/{publishedModelName}/url/nostore'}

    def classify_image_with_no_store(
            self, project_id, published_model_name, image_data, application=None, custom_headers=None, raw=False, **operation_config):
        """Classify an image without saving the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param image_data: Binary image data.
        :type image_data: Generator
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        # Construct URL
        url = self.classify_image_with_no_store.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    classify_image_with_no_store.metadata = {'url': '/{projectId}/classify/models/{publishedModelName}/image/nostore'}

    def detect_image_url(
            self, project_id, published_model_name, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Detect objects in an image url and saves the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param url: Url of the image.
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.detect_image_url.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_image_url.metadata = {'url': '/{projectId}/detect/models/{publishedModelName}/url'}

    def detect_image(
            self, project_id, published_model_name, image_data, application=None, custom_headers=None, raw=False, **operation_config):
        """Detect objects in an image and saves the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param image_data: Binary image data.
        :type image_data: Generator
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        # Construct URL
        url = self.detect_image.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_image.metadata = {'url': '/{projectId}/detect/models/{publishedModelName}/image'}

    def detect_image_url_with_no_store(
            self, project_id, published_model_name, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Detect objects in an image url without saving the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param url: Url of the image.
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.detect_image_url_with_no_store.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_image_url_with_no_store.metadata = {'url': '/{projectId}/detect/models/{publishedModelName}/url/nostore'}

    def detect_image_with_no_store(
            self, project_id, published_model_name, image_data, application=None, custom_headers=None, raw=False, **operation_config):
        """Detect objects in an image without saving the result.

        :param project_id: The project id.
        :type project_id: str
        :param published_model_name: Specifies the name of the model to
         evaluate against.
        :type published_model_name: str
        :param image_data: Binary image data.
        :type image_data: Generator
        :param application: Optional. Specifies the name of application using
         the endpoint.
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`CustomVisionErrorException<azure.cognitiveservices.vision.customvision.prediction.models.CustomVisionErrorException>`
        """
        # Construct URL
        url = self.detect_image_with_no_store.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'projectId': self._serialize.url("project_id", project_id, 'str'),
            'publishedModelName': self._serialize.url("published_model_name", published_model_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, form_content=form_data_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.CustomVisionErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_image_with_no_store.metadata = {'url': '/{projectId}/detect/models/{publishedModelName}/image/nostore'}
