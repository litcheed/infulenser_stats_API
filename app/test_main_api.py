
import sys
sys.path.append("/usr/src/python/app")
import pytest

from httpx import AsyncClient, ASGITransport

from main_api import app

@pytest.mark.anyio
async def test_get_counts_good_cmnt():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/stats/average-likes-comments")
    assert response.status_code == 200
    assert "average_likes" in response.json()
    assert "average_comments" in response.json()
    print("test_get_counts_good_cmnt passed")

@pytest.mark.anyio
async def test_get_ave_good_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/influencers/top-by-likes?top_n=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5
    print("test_get_ave_good_topN passed")

@pytest.mark.anyio
async def test_get_ave_cmnt_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/influencers/top-by-comments?top_n=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5
    print("test_get_ave_cmnt_topN passed")

@pytest.mark.anyio
async def test_get_noun_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/content/top-nouns?top_n=5")
    assert response.status_code == 200
    assert len(response.json()) <= 5
    print("test_get_noun_topN passed")
