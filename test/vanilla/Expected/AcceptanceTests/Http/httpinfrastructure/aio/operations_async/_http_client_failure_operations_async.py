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


from ... import models


class HttpClientFailureOperations:
    """HttpClientFailureOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    async def head400(
            self, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    head400.metadata = {'url': '/http/failure/client/400'}

    async def get400(
            self, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get400.metadata = {'url': '/http/failure/client/400'}

    async def put400(
            self, boolean_value=None, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    put400.metadata = {'url': '/http/failure/client/400'}

    async def patch400(
            self, boolean_value=None, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    patch400.metadata = {'url': '/http/failure/client/400'}

    async def post400(
            self, boolean_value=None, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post400.metadata = {'url': '/http/failure/client/400'}

    async def delete400(
            self, boolean_value=None, **kwargs):
        """Return 400 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete400.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    delete400.metadata = {'url': '/http/failure/client/400'}

    async def head401(
            self, **kwargs):
        """Return 401 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head401.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    head401.metadata = {'url': '/http/failure/client/401'}

    async def get402(
            self, **kwargs):
        """Return 402 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get402.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get402.metadata = {'url': '/http/failure/client/402'}

    async def get403(
            self, **kwargs):
        """Return 403 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get403.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get403.metadata = {'url': '/http/failure/client/403'}

    async def put404(
            self, boolean_value=None, **kwargs):
        """Return 404 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put404.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    put404.metadata = {'url': '/http/failure/client/404'}

    async def patch405(
            self, boolean_value=None, **kwargs):
        """Return 405 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch405.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    patch405.metadata = {'url': '/http/failure/client/405'}

    async def post406(
            self, boolean_value=None, **kwargs):
        """Return 406 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post406.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post406.metadata = {'url': '/http/failure/client/406'}

    async def delete407(
            self, boolean_value=None, **kwargs):
        """Return 407 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete407.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    delete407.metadata = {'url': '/http/failure/client/407'}

    async def put409(
            self, boolean_value=None, **kwargs):
        """Return 409 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put409.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    put409.metadata = {'url': '/http/failure/client/409'}

    async def head410(
            self, **kwargs):
        """Return 410 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head410.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    head410.metadata = {'url': '/http/failure/client/410'}

    async def get411(
            self, **kwargs):
        """Return 411 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get411.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get411.metadata = {'url': '/http/failure/client/411'}

    async def get412(
            self, **kwargs):
        """Return 412 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get412.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get412.metadata = {'url': '/http/failure/client/412'}

    async def put413(
            self, boolean_value=None, **kwargs):
        """Return 413 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put413.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    put413.metadata = {'url': '/http/failure/client/413'}

    async def patch414(
            self, boolean_value=None, **kwargs):
        """Return 414 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch414.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    patch414.metadata = {'url': '/http/failure/client/414'}

    async def post415(
            self, boolean_value=None, **kwargs):
        """Return 415 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post415.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    post415.metadata = {'url': '/http/failure/client/415'}

    async def get416(
            self, **kwargs):
        """Return 416 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get416.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    get416.metadata = {'url': '/http/failure/client/416'}

    async def delete417(
            self, boolean_value=None, **kwargs):
        """Return 417 status code - should be represented in the client as an
        error.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete417.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    delete417.metadata = {'url': '/http/failure/client/417'}

    async def head429(
            self, **kwargs):
        """Return 429 status code - should be represented in the client as an
        error.

        :return: Error
        :rtype: ~httpinfrastructure.models.Error
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head429.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

    head429.metadata = {'url': '/http/failure/client/429'}
