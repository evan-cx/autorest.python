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

from azure.core import HttpRequestError

from .. import models


class HttpFailureOperations(object):
    """HttpFailureOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    def get_empty_error(
            self, **kwargs):
        """Get empty error form server.

        :return: bool
        :rtype: bool
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty_error.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        return deserialized
    get_empty_error.metadata = {'url': '/http/failure/emptybody/error'}

    def get_no_model_error(
            self, **kwargs):
        """Get empty error form server.

        :return: bool
        :rtype: bool
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_no_model_error.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        return deserialized
    get_no_model_error.metadata = {'url': '/http/failure/nomodel/error'}

    def get_no_model_empty(
            self, **kwargs):
        """Get empty response from server.

        :return: bool
        :rtype: bool
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_no_model_empty.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        return deserialized
    get_no_model_empty.metadata = {'url': '/http/failure/nomodel/empty'}
