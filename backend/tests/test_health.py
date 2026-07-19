"""
MaskaStorage — Test: Health Endpoint
========================================
Placeholder test for the GET /api/v1/health endpoint.

TODO: Expand with authentication, edge cases, and integration tests.
"""

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.asyncio
async def test_health_check_returns_ok():
    """GET /api/v1/health should return 200 with status: ok."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
