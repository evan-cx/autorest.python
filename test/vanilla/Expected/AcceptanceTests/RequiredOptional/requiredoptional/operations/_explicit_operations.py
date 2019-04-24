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


class ExplicitOperations(object):
    """ExplicitOperations operations.

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

    def post_required_integer_parameter(
            self, body_parameter, **kwargs):
        """Test explicitly required integer. Please put null and the client
        library should throw before the request is sent.

        :param body_parameter:
        :type body_parameter: int
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_integer_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_integer_parameter.metadata = {'url': '/reqopt/requied/integer/parameter'}

    def post_optional_integer_parameter(
            self, body_parameter=None, **kwargs):
        """Test explicitly optional integer. Please put null.

        :param body_parameter:
        :type body_parameter: int
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_integer_parameter.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'int')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_integer_parameter.metadata = {'url': '/reqopt/optional/integer/parameter'}

    def post_required_integer_property(
            self, value, **kwargs):
        """Test explicitly required integer. Please put a valid int-wrapper with
        'value' = null and the client library should throw before the request
        is sent.

        :param value:
        :type value: int
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = models.IntWrapper(value=value)

        # Construct URL
        url = self.post_required_integer_property.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'IntWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_integer_property.metadata = {'url': '/reqopt/requied/integer/property'}

    def post_optional_integer_property(
            self, value=None, **kwargs):
        """Test explicitly optional integer. Please put a valid int-wrapper with
        'value' = null.

        :param value:
        :type value: int
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = None
        if value is not None:
            body_parameter = models.IntOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_integer_property.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'IntOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_integer_property.metadata = {'url': '/reqopt/optional/integer/property'}

    def post_required_integer_header(
            self, header_parameter, **kwargs):
        """Test explicitly required integer. Please put a header 'headerParameter'
        => null and the client library should throw before the request is sent.

        :param header_parameter:
        :type header_parameter: int
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_integer_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_integer_header.metadata = {'url': '/reqopt/requied/integer/header'}

    def post_optional_integer_header(
            self, header_parameter=None, **kwargs):
        """Test explicitly optional integer. Please put a header 'headerParameter'
        => null.

        :param header_parameter:
        :type header_parameter: int
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_integer_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if header_parameter is not None:
            header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_integer_header.metadata = {'url': '/reqopt/optional/integer/header'}

    def post_required_string_parameter(
            self, body_parameter, **kwargs):
        """Test explicitly required string. Please put null and the client library
        should throw before the request is sent.

        :param body_parameter:
        :type body_parameter: str
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_string_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_string_parameter.metadata = {'url': '/reqopt/requied/string/parameter'}

    def post_optional_string_parameter(
            self, body_parameter=None, **kwargs):
        """Test explicitly optional string. Please put null.

        :param body_parameter:
        :type body_parameter: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_string_parameter.metadata['url']

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
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_string_parameter.metadata = {'url': '/reqopt/optional/string/parameter'}

    def post_required_string_property(
            self, value, **kwargs):
        """Test explicitly required string. Please put a valid string-wrapper with
        'value' = null and the client library should throw before the request
        is sent.

        :param value:
        :type value: str
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = models.StringWrapper(value=value)

        # Construct URL
        url = self.post_required_string_property.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'StringWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_string_property.metadata = {'url': '/reqopt/requied/string/property'}

    def post_optional_string_property(
            self, value=None, **kwargs):
        """Test explicitly optional integer. Please put a valid string-wrapper
        with 'value' = null.

        :param value:
        :type value: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = None
        if value is not None:
            body_parameter = models.StringOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_string_property.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'StringOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_string_property.metadata = {'url': '/reqopt/optional/string/property'}

    def post_required_string_header(
            self, header_parameter, **kwargs):
        """Test explicitly required string. Please put a header 'headerParameter'
        => null and the client library should throw before the request is sent.

        :param header_parameter:
        :type header_parameter: str
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_string_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_string_header.metadata = {'url': '/reqopt/requied/string/header'}

    def post_optional_string_header(
            self, body_parameter=None, **kwargs):
        """Test explicitly optional string. Please put a header 'headerParameter'
        => null.

        :param body_parameter:
        :type body_parameter: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_string_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if body_parameter is not None:
            header_parameters['bodyParameter'] = self._serialize.header("body_parameter", body_parameter, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_string_header.metadata = {'url': '/reqopt/optional/string/header'}

    def post_required_class_parameter(
            self, body_parameter, **kwargs):
        """Test explicitly required complex object. Please put null and the client
        library should throw before the request is sent.

        :param body_parameter:
        :type body_parameter: ~requiredoptional.models.Product
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_class_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'Product')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_class_parameter.metadata = {'url': '/reqopt/requied/class/parameter'}

    def post_optional_class_parameter(
            self, body_parameter=None, **kwargs):
        """Test explicitly optional complex object. Please put null.

        :param body_parameter:
        :type body_parameter: ~requiredoptional.models.Product
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_class_parameter.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_class_parameter.metadata = {'url': '/reqopt/optional/class/parameter'}

    def post_required_class_property(
            self, value, **kwargs):
        """Test explicitly required complex object. Please put a valid
        class-wrapper with 'value' = null and the client library should throw
        before the request is sent.

        :param value:
        :type value: ~requiredoptional.models.Product
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = models.ClassWrapper(value=value)

        # Construct URL
        url = self.post_required_class_property.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'ClassWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_class_property.metadata = {'url': '/reqopt/requied/class/property'}

    def post_optional_class_property(
            self, value=None, **kwargs):
        """Test explicitly optional complex object. Please put a valid
        class-wrapper with 'value' = null.

        :param value:
        :type value: ~requiredoptional.models.Product
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = None
        if value is not None:
            body_parameter = models.ClassOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_class_property.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'ClassOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_class_property.metadata = {'url': '/reqopt/optional/class/property'}

    def post_required_array_parameter(
            self, body_parameter, **kwargs):
        """Test explicitly required array. Please put null and the client library
        should throw before the request is sent.

        :param body_parameter:
        :type body_parameter: list[str]
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_array_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, '[str]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_array_parameter.metadata = {'url': '/reqopt/requied/array/parameter'}

    def post_optional_array_parameter(
            self, body_parameter=None, **kwargs):
        """Test explicitly optional array. Please put null.

        :param body_parameter:
        :type body_parameter: list[str]
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_array_parameter.metadata['url']

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
            body_content = self._serialize.body(body_parameter, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_array_parameter.metadata = {'url': '/reqopt/optional/array/parameter'}

    def post_required_array_property(
            self, value, **kwargs):
        """Test explicitly required array. Please put a valid array-wrapper with
        'value' = null and the client library should throw before the request
        is sent.

        :param value:
        :type value: list[str]
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = models.ArrayWrapper(value=value)

        # Construct URL
        url = self.post_required_array_property.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(body_parameter, 'ArrayWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_array_property.metadata = {'url': '/reqopt/requied/array/property'}

    def post_optional_array_property(
            self, value=None, **kwargs):
        """Test explicitly optional array. Please put a valid array-wrapper with
        'value' = null.

        :param value:
        :type value: list[str]
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        body_parameter = None
        if value is not None:
            body_parameter = models.ArrayOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_array_property.metadata['url']

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
            body_content = self._serialize.body(body_parameter, 'ArrayOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_array_property.metadata = {'url': '/reqopt/optional/array/property'}

    def post_required_array_header(
            self, header_parameter, **kwargs):
        """Test explicitly required array. Please put a header 'headerParameter'
        => null and the client library should throw before the request is sent.

        :param header_parameter:
        :type header_parameter: list[str]
        :return: Error
        :rtype: ~requiredoptional.models.Error
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_required_array_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, '[str]', div=',')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post_required_array_header.metadata = {'url': '/reqopt/requied/array/header'}

    def post_optional_array_header(
            self, header_parameter=None, **kwargs):
        """Test explicitly optional integer. Please put a header 'headerParameter'
        => null.

        :param header_parameter:
        :type header_parameter: list[str]
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.post_optional_array_header.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if header_parameter is not None:
            header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, '[str]', div=',')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_optional_array_header.metadata = {'url': '/reqopt/optional/array/header'}
