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


class PathsOperations(object):
    """PathsOperations operations.

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

    def get_empty(
            self, account_name, **kwargs):
        """Get a 200 to test a valid base uri.

        :param account_name: Account Name
        :type account_name: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<custombaseurl.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty.metadata['url']
        path_format_arguments = {
            'accountName': self._serialize.url("account_name", account_name, 'str', skip_quote=True),
            'host': self._serialize.url("self._config.host", self._config.host, 'str', skip_quote=True)
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
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_empty.metadata = {'url': '/customuri'}
