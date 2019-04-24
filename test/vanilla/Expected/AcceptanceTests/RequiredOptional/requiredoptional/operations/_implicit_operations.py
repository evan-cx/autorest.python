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


from .. import models


class ImplicitOperations(object):
    """ImplicitOperations operations.

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

    def get_required_path(
            self, path_parameter, **kwargs):
        """Test implicitly required path parameter.

        :param path_parameter:
        :type path_parameter: str
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_path.metadata['url']
        path_format_arguments = {
            'pathParameter': self._serialize.url("path_parameter", path_parameter, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get_required_path.metadata = {'url': '/reqopt/implicit/required/path/{pathParameter}'}

    def put_optional_query(
            self, query_parameter=None, **kwargs):
        """Test implicitly optional query parameter.

        :param query_parameter:
        :type query_parameter: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_parameter is not None:
            query_parameters['queryParameter'] = self._serialize.query("query_parameter", query_parameter, 'str')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put_optional_query.metadata = {'url': '/reqopt/implicit/optional/query'}

    def put_optional_header(
            self, query_parameter=None, **kwargs):
        """Test implicitly optional header parameter.

        :param query_parameter:
        :type query_parameter: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if query_parameter is not None:
            header_parameters['queryParameter'] = self._serialize.header("query_parameter", query_parameter, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put_optional_header.metadata = {'url': '/reqopt/implicit/optional/header'}

    def put_optional_body(
            self, body_parameter=None, **kwargs):
        """Test implicitly optional body parameter.

        :param body_parameter:
        :type body_parameter: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_body.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put_optional_body.metadata = {'url': '/reqopt/implicit/optional/body'}

    def get_required_global_path(
            self, **kwargs):
        """Test implicitly required path parameter.

        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_path.metadata['url']
        path_format_arguments = {
            'required-global-path': self._serialize.url("self._config.required_global_path", self._config.required_global_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get_required_global_path.metadata = {'url': '/reqopt/global/required/path/{required-global-path}'}

    def get_required_global_query(
            self, **kwargs):
        """Test implicitly required query parameter.

        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['required-global-query'] = self._serialize.query("self._config.required_global_query", self._config.required_global_query, 'str')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get_required_global_query.metadata = {'url': '/reqopt/global/required/query'}

    def get_optional_global_query(
            self, **kwargs):
        """Test implicitly optional query parameter.

        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_optional_global_query.metadata['url']

        # Construct parameters
        query_parameters = {}
        if self._config.optional_global_query is not None:
            query_parameters['optional-global-query'] = self._serialize.query("self._config.optional_global_query", self._config.optional_global_query, 'int')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get_optional_global_query.metadata = {'url': '/reqopt/global/optional/query'}
