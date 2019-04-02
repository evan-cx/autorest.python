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

# from azure.core import AsyncPipelineClient  TODO
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestSwaggerBATFileServiceConfiguration
from .operations_async import FilesOperations
from .. import models


class AutoRestSwaggerBATFileService:
    """Test Infrastructure for AutoRest Swagger BAT


    :ivar files: Files operations
    :vartype files: bodyfile.aio.operations_async.FilesOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestSwaggerBATFileServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, credentials=None, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.files = FilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
