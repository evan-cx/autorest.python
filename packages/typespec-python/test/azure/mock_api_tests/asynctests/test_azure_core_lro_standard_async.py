# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from specs.azure.core.lro.standard.aio import StandardClient
from specs.azure.core.lro.standard.models import User, ExportedUser

@pytest.fixture
async def client():
    async with StandardClient() as client:
        yield client

# cadl-ranch check api-version in poll request which is not supported by azure-core

# @pytest.mark.asyncio
# async def test_lro_core_put(client):
#     user = User({"name": "madge", "role": "contributor"})
#     result = await (await client.begin_create_or_replace(name=user.name, resource=user, polling_interval=0)).result()
#     assert result == user

# @pytest.mark.asyncio
# async def test_lro_core_delete(client):
#     await (await client.begin_delete(name="madge", polling_interval=0)).result()

# @pytest.mark.asyncio
# async def test_lro_core_export(client):
#     export_user = ExportedUser({ "name": "madge", "resourceUri": "/users/madge" })
#     result = await (await client.begin_export(name="madge", format="json", polling_interval=0)).result()
#     assert result == export_user
