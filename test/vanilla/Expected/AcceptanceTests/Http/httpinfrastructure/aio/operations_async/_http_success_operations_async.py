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


class HttpSuccessOperations:
    """HttpSuccessOperations async operations.

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

    async def head200(
            self, **kwargs):
        """Return 200 status code if successful.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head200.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    head200.metadata = {'url': '/http/success/200'}

    async def get200(
            self, **kwargs):
        """Get 200 success.

        :return: bool
        :rtype: bool
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get200.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        return deserialized
    get200.metadata = {'url': '/http/success/200'}

    async def put200(
            self, boolean_value=None, **kwargs):
        """Put boolean value true returning 200 success.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put200.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put200.metadata = {'url': '/http/success/200'}

    async def patch200(
            self, boolean_value=None, **kwargs):
        """Patch true Boolean value in request returning 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch200.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    patch200.metadata = {'url': '/http/success/200'}

    async def post200(
            self, boolean_value=None, **kwargs):
        """Post bollean value true in request that returns a 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post200.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post200.metadata = {'url': '/http/success/200'}

    async def delete200(
            self, boolean_value=None, **kwargs):
        """Delete simple boolean value true returns 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete200.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    delete200.metadata = {'url': '/http/success/200'}

    async def put201(
            self, boolean_value=None, **kwargs):
        """Put true Boolean value in request returns 201.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put201.metadata['url']

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

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

    put201.metadata = {'url': '/http/success/201'}

    async def post201(
            self, boolean_value=None, **kwargs):
        """Post true Boolean value in request returns 201 (Created).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post201.metadata['url']

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

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

    post201.metadata = {'url': '/http/success/201'}

    async def put202(
            self, boolean_value=None, **kwargs):
        """Put true Boolean value in request returns 202 (Accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put202.metadata['url']

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

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

    put202.metadata = {'url': '/http/success/202'}

    async def patch202(
            self, boolean_value=None, **kwargs):
        """Patch true Boolean value in request returns 202.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch202.metadata['url']

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

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

    patch202.metadata = {'url': '/http/success/202'}

    async def post202(
            self, boolean_value=None, **kwargs):
        """Post true Boolean value in request returns 202 (Accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post202.metadata['url']

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

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

    post202.metadata = {'url': '/http/success/202'}

    async def delete202(
            self, boolean_value=None, **kwargs):
        """Delete true Boolean value in request returns 202 (accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete202.metadata['url']

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

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

    delete202.metadata = {'url': '/http/success/202'}

    async def head204(
            self, **kwargs):
        """Return 204 status code if successful.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head204.metadata['url']

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

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

    head204.metadata = {'url': '/http/success/204'}

    async def put204(
            self, boolean_value=None, **kwargs):
        """Put true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put204.metadata['url']

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

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

    put204.metadata = {'url': '/http/success/204'}

    async def patch204(
            self, boolean_value=None, **kwargs):
        """Patch true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch204.metadata['url']

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

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

    patch204.metadata = {'url': '/http/success/204'}

    async def post204(
            self, boolean_value=None, **kwargs):
        """Post true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post204.metadata['url']

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

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

    post204.metadata = {'url': '/http/success/204'}

    async def delete204(
            self, boolean_value=None, **kwargs):
        """Delete true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete204.metadata['url']

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

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

    delete204.metadata = {'url': '/http/success/204'}

    async def head404(
            self, **kwargs):
        """Return 404 status code.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head404.metadata['url']

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

        if response.status_code not in [204, 404]:
            raise models.ErrorException(self._deserialize, response)

    head404.metadata = {'url': '/http/success/404'}
