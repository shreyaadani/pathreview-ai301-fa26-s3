"""Integration tests for authentication edge cases in api/middleware/auth.py (#38)."""

import pytest

PROFILE_URL = "/profiles/00000000-0000-0000-0000-000000000000"

pytestmark = pytest.mark.integration


def test_missing_authorization_header(client, stub_db):
    """Test a request with no Authorization header gets 401 before any DB lookup."""
    response = client.get(PROFILE_URL)

    assert response.status_code == 401
    assert response.headers["WWW-Authenticate"] == "Bearer"
    assert stub_db.calls == 0
