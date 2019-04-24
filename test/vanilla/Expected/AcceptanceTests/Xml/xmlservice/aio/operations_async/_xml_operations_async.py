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

from ... import models


class XmlOperations:
    """XmlOperations async operations.

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

    async def get_complex_type_ref_no_meta(
            self, **kwargs):
        """Get a complex type that has a ref to a complex type with no XML node.

        :return: RootWithRefAndNoMeta
        :rtype: ~xmlservice.models.RootWithRefAndNoMeta
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_complex_type_ref_no_meta.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RootWithRefAndNoMeta', response)

        return deserialized
    get_complex_type_ref_no_meta.metadata = {'url': '/xml/complex-type-ref-no-meta'}

    async def put_complex_type_ref_no_meta(
            self, model, **kwargs):
        """Puts a complex type that has a ref to a complex type with no XML node.

        :param model:
        :type model: ~xmlservice.models.RootWithRefAndNoMeta
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_complex_type_ref_no_meta.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(model, 'RootWithRefAndNoMeta')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_complex_type_ref_no_meta.metadata = {'url': '/xml/complex-type-ref-no-meta'}

    async def get_complex_type_ref_with_meta(
            self, **kwargs):
        """Get a complex type that has a ref to a complex type with XML node.

        :return: RootWithRefAndMeta
        :rtype: ~xmlservice.models.RootWithRefAndMeta
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_complex_type_ref_with_meta.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RootWithRefAndMeta', response)

        return deserialized
    get_complex_type_ref_with_meta.metadata = {'url': '/xml/complex-type-ref-with-meta'}

    async def put_complex_type_ref_with_meta(
            self, model, **kwargs):
        """Puts a complex type that has a ref to a complex type with XML node.

        :param model:
        :type model: ~xmlservice.models.RootWithRefAndMeta
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_complex_type_ref_with_meta.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(model, 'RootWithRefAndMeta')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_complex_type_ref_with_meta.metadata = {'url': '/xml/complex-type-ref-with-meta'}

    async def get_simple(
            self, **kwargs):
        """Get a simple XML document.

        :return: Slideshow
        :rtype: ~xmlservice.models.Slideshow
        :raises: :class:`ErrorException<xmlservice.models.ErrorException>`
        """
        # Construct URL
        url = self.get_simple.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
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
            deserialized = self._deserialize('Slideshow', response)

        return deserialized
    get_simple.metadata = {'url': '/xml/simple'}

    async def put_simple(
            self, slideshow, **kwargs):
        """Put a simple XML document.

        :param slideshow:
        :type slideshow: ~xmlservice.models.Slideshow
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<xmlservice.models.ErrorException>`
        """
        # Construct URL
        url = self.put_simple.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(slideshow, 'Slideshow')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

    put_simple.metadata = {'url': '/xml/simple'}

    async def get_wrapped_lists(
            self, **kwargs):
        """Get an XML document with multiple wrapped lists.

        :return: AppleBarrel
        :rtype: ~xmlservice.models.AppleBarrel
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_wrapped_lists.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AppleBarrel', response)

        return deserialized
    get_wrapped_lists.metadata = {'url': '/xml/wrapped-lists'}

    async def put_wrapped_lists(
            self, wrapped_lists, **kwargs):
        """Put an XML document with multiple wrapped lists.

        :param wrapped_lists:
        :type wrapped_lists: ~xmlservice.models.AppleBarrel
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<xmlservice.models.ErrorException>`
        """
        # Construct URL
        url = self.put_wrapped_lists.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(wrapped_lists, 'AppleBarrel')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

    put_wrapped_lists.metadata = {'url': '/xml/wrapped-lists'}

    async def get_headers(
            self, **kwargs):
        """Get strongly-typed response headers.

        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_headers.metadata['url']

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

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

    get_headers.metadata = {'url': '/xml/headers'}

    async def get_empty_list(
            self, **kwargs):
        """Get an empty list.

        :return: Slideshow
        :rtype: ~xmlservice.models.Slideshow
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_empty_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Slideshow', response)

        return deserialized
    get_empty_list.metadata = {'url': '/xml/empty-list'}

    async def put_empty_list(
            self, slideshow, **kwargs):
        """Puts an empty list.

        :param slideshow:
        :type slideshow: ~xmlservice.models.Slideshow
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_empty_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(slideshow, 'Slideshow')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_empty_list.metadata = {'url': '/xml/empty-list'}

    async def get_empty_wrapped_lists(
            self, **kwargs):
        """Gets some empty wrapped lists.

        :return: AppleBarrel
        :rtype: ~xmlservice.models.AppleBarrel
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_empty_wrapped_lists.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AppleBarrel', response)

        return deserialized
    get_empty_wrapped_lists.metadata = {'url': '/xml/empty-wrapped-lists'}

    async def put_empty_wrapped_lists(
            self, apple_barrel, **kwargs):
        """Puts some empty wrapped lists.

        :param apple_barrel:
        :type apple_barrel: ~xmlservice.models.AppleBarrel
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_empty_wrapped_lists.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(apple_barrel, 'AppleBarrel')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_empty_wrapped_lists.metadata = {'url': '/xml/empty-wrapped-lists'}

    async def get_root_list(
            self, **kwargs):
        """Gets a list as the root element.

        :return: list
        :rtype: list[~xmlservice.models.Banana]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_root_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[Banana]', response)

        return deserialized
    get_root_list.metadata = {'url': '/xml/root-list'}

    async def put_root_list(
            self, bananas, **kwargs):
        """Puts a list as the root element.

        :param bananas:
        :type bananas: list[~xmlservice.models.Banana]
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_root_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        serialization_ctxt = {'xml': {'name': 'bananas', 'itemsName': 'bananas', 'wrapped': True}}
        body_content = self._serialize.body(bananas, '[Banana]', serialization_ctxt=serialization_ctxt)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_root_list.metadata = {'url': '/xml/root-list'}

    async def get_root_list_single_item(
            self, **kwargs):
        """Gets a list with a single item.

        :return: list
        :rtype: list[~xmlservice.models.Banana]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_root_list_single_item.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[Banana]', response)

        return deserialized
    get_root_list_single_item.metadata = {'url': '/xml/root-list-single-item'}

    async def put_root_list_single_item(
            self, bananas, **kwargs):
        """Puts a list with a single item.

        :param bananas:
        :type bananas: list[~xmlservice.models.Banana]
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_root_list_single_item.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        serialization_ctxt = {'xml': {'name': 'bananas', 'itemsName': 'bananas', 'wrapped': True}}
        body_content = self._serialize.body(bananas, '[Banana]', serialization_ctxt=serialization_ctxt)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_root_list_single_item.metadata = {'url': '/xml/root-list-single-item'}

    async def get_empty_root_list(
            self, **kwargs):
        """Gets an empty list as the root element.

        :return: list
        :rtype: list[~xmlservice.models.Banana]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_empty_root_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[Banana]', response)

        return deserialized
    get_empty_root_list.metadata = {'url': '/xml/empty-root-list'}

    async def put_empty_root_list(
            self, bananas, **kwargs):
        """Puts an empty list as the root element.

        :param bananas:
        :type bananas: list[~xmlservice.models.Banana]
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_empty_root_list.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        serialization_ctxt = {'xml': {'name': 'bananas', 'itemsName': 'bananas', 'wrapped': True}}
        body_content = self._serialize.body(bananas, '[Banana]', serialization_ctxt=serialization_ctxt)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_empty_root_list.metadata = {'url': '/xml/empty-root-list'}

    async def get_empty_child_element(
            self, **kwargs):
        """Gets an XML document with an empty child element.

        :return: Banana
        :rtype: ~xmlservice.models.Banana
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.get_empty_child_element.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Banana', response)

        return deserialized
    get_empty_child_element.metadata = {'url': '/xml/empty-child-element'}

    async def put_empty_child_element(
            self, banana, **kwargs):
        """Puts a value with an empty child element.

        :param banana:
        :type banana: ~xmlservice.models.Banana
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        # Construct URL
        url = self.put_empty_child_element.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(banana, 'Banana')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_empty_child_element.metadata = {'url': '/xml/empty-child-element'}

    async def list_containers(
            self, **kwargs):
        """Lists containers in a storage account.

        :return: ListContainersResponse
        :rtype: ~xmlservice.models.ListContainersResponse
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "list"

        # Construct URL
        url = self.list_containers.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ListContainersResponse', response)

        return deserialized
    list_containers.metadata = {'url': '/xml/'}

    async def get_service_properties(
            self, **kwargs):
        """Gets storage service properties.

        :return: StorageServiceProperties
        :rtype: ~xmlservice.models.StorageServiceProperties
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "properties"
        restype = "service"

        # Construct URL
        url = self.get_service_properties.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StorageServiceProperties', response)

        return deserialized
    get_service_properties.metadata = {'url': '/xml/'}

    async def put_service_properties(
            self, properties, **kwargs):
        """Puts storage service properties.

        :param properties:
        :type properties: ~xmlservice.models.StorageServiceProperties
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "properties"
        restype = "service"

        # Construct URL
        url = self.put_service_properties.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(properties, 'StorageServiceProperties')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_service_properties.metadata = {'url': '/xml/'}

    async def get_acls(
            self, **kwargs):
        """Gets storage ACLs for a container.

        :return: list
        :rtype: list[~xmlservice.models.SignedIdentifier]
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "acl"
        restype = "container"

        # Construct URL
        url = self.get_acls.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[SignedIdentifier]', response)

        return deserialized
    get_acls.metadata = {'url': '/xml/mycontainer'}

    async def put_acls(
            self, properties, **kwargs):
        """Puts storage ACLs for a container.

        :param properties:
        :type properties: list[~xmlservice.models.SignedIdentifier]
        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "acl"
        restype = "container"

        # Construct URL
        url = self.put_acls.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        serialization_ctxt = {'xml': {'name': 'SignedIdentifiers', 'itemsName': 'SignedIdentifiers', 'wrapped': True}}
        body_content = self._serialize.body(properties, '[SignedIdentifier]', serialization_ctxt=serialization_ctxt)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            raise HttpRequestError(response=response)

    put_acls.metadata = {'url': '/xml/mycontainer'}

    async def list_blobs(
            self, **kwargs):
        """Lists blobs in a storage container.

        :return: ListBlobsResponse
        :rtype: ~xmlservice.models.ListBlobsResponse
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        comp = "list"
        restype = "container"

        # Construct URL
        url = self.list_blobs.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ListBlobsResponse', response)

        return deserialized
    list_blobs.metadata = {'url': '/xml/mycontainer'}
