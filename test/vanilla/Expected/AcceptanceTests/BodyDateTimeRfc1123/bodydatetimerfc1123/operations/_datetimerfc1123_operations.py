# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class Datetimerfc1123Operations(object):
    """Datetimerfc1123Operations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydatetimerfc1123.models
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

    @distributed_trace
    def get_null(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get null datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/datetimerfc1123/null'}

    @distributed_trace
    def get_invalid(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get invalid datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/datetimerfc1123/invalid'}

    @distributed_trace
    def get_overflow(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get overflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_overflow.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_overflow.metadata = {'url': '/datetimerfc1123/overflow'}

    @distributed_trace
    def get_underflow(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get underflow datetime value.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_underflow.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_underflow.metadata = {'url': '/datetimerfc1123/underflow'}

    @distributed_trace
    def put_utc_max_date_time(
        self,
        datetime_body,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put max datetime value Fri, 31 Dec 9999 23:59:59 GMT.

        :param datetime_body:
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_utc_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(datetime_body, 'rfc-1123')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_utc_max_date_time.metadata = {'url': '/datetimerfc1123/max'}

    @distributed_trace
    def get_utc_lowercase_max_date_time(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get max datetime value fri, 31 dec 9999 23:59:59 gmt.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_utc_lowercase_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_utc_lowercase_max_date_time.metadata = {'url': '/datetimerfc1123/max/lowercase'}

    @distributed_trace
    def get_utc_uppercase_max_date_time(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get max datetime value FRI, 31 DEC 9999 23:59:59 GMT.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_utc_uppercase_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_utc_uppercase_max_date_time.metadata = {'url': '/datetimerfc1123/max/uppercase'}

    @distributed_trace
    def put_utc_min_date_time(
        self,
        datetime_body,  # type: datetime.datetime
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :param datetime_body:
        :type datetime_body: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_utc_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(datetime_body, 'rfc-1123')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_utc_min_date_time.metadata = {'url': '/datetimerfc1123/min'}

    @distributed_trace
    def get_utc_min_date_time(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> datetime.datetime
        """Get min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[datetime.datetime]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_utc_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('rfc-1123', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_utc_min_date_time.metadata = {'url': '/datetimerfc1123/min'}
