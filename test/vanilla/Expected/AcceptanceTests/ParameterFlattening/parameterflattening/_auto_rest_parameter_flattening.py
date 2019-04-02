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

# from azure.core import PipelineClient  TODO
from msrest import Serializer, Deserializer

from ._configuration import AutoRestParameterFlatteningConfiguration
from msrest.exceptions import HttpOperationError
from .operations import AvailabilitySetsOperations
from . import models


class AutoRestParameterFlattening(object):
    """Resource Flattening for AutoRest


    :ivar availability_sets: AvailabilitySets operations
    :vartype availability_sets: parameterflattening.operations.AvailabilitySetsOperations

    :param str base_url: Service URL
    """

    def __init__(self, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestParameterFlatteningConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, credentials=None, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
