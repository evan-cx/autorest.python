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


class Datetimerfc1123Operations(object):
    """Datetimerfc1123Operations operations.

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

    def get_null(
            self, **kwargs):
        """Get null datetime value.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_null.metadata = {'url': '/datetimerfc1123/null'}

    def get_invalid(
            self, **kwargs):
        """Get invalid datetime value.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_invalid.metadata = {'url': '/datetimerfc1123/invalid'}

    def get_overflow(
            self, **kwargs):
        """Get overflow datetime value.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_overflow.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_overflow.metadata = {'url': '/datetimerfc1123/overflow'}

    def get_underflow(
            self, **kwargs):
        """Get underflow datetime value.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_underflow.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_underflow.metadata = {'url': '/datetimerfc1123/underflow'}

    def put_utc_max_date_time(
            self, datetime_body, **kwargs):
        """Put max datetime value Fri, 31 Dec 9999 23:59:59 GMT.

        :param datetime_body:
        :type datetime_body: datetime
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.put_utc_max_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(datetime_body, 'rfc-1123')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put_utc_max_date_time.metadata = {'url': '/datetimerfc1123/max'}

    def get_utc_lowercase_max_date_time(
            self, **kwargs):
        """Get max datetime value fri, 31 dec 9999 23:59:59 gmt.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_utc_lowercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_utc_lowercase_max_date_time.metadata = {'url': '/datetimerfc1123/max/lowercase'}

    def get_utc_uppercase_max_date_time(
            self, **kwargs):
        """Get max datetime value FRI, 31 DEC 9999 23:59:59 GMT.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_utc_uppercase_max_date_time.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_utc_uppercase_max_date_time.metadata = {'url': '/datetimerfc1123/max/uppercase'}

    def put_utc_min_date_time(
            self, datetime_body, **kwargs):
        """Put min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :param datetime_body:
        :type datetime_body: datetime
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.put_utc_min_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(datetime_body, 'rfc-1123')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    put_utc_min_date_time.metadata = {'url': '/datetimerfc1123/min'}

    def get_utc_min_date_time(
            self, **kwargs):
        """Get min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :return: datetime
        :rtype: datetime
        :raises:
         :class:`ErrorException<bodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = self.get_utc_min_date_time.metadata['url']

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
            deserialized = self._deserialize('rfc-1123', response)

        return deserialized
    get_utc_min_date_time.metadata = {'url': '/datetimerfc1123/min'}
