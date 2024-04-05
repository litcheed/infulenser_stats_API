#!/usr/bin/env python3
#################################################################
#
# 概要:APIテストファイル
#      1️⃣平均いいね数、平均コメント数を取得するAPI
#      2️⃣平均いいね数の多いインフルエンサー上位N件を取得するAPI
#      3️⃣平均コメント数の多いインフルエンサー上位N件を取得するAPI
#      4️⃣textカラムに頻出の名詞上位N件を取得するAPI
#
#################################################################

import sys
sys.path.append("/usr/src/python/app")
import pytest

from httpx import AsyncClient, ASGITransport

from main_api import app



# クエリパラメータ設定
query_param = 5


# 1️⃣平均いいね数、平均コメント数を取得するAPI
@pytest.mark.trio
async def test_get_counts_good_cmnt():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/stats/average-likes-comments")
    assert response.status_code == 200
    assert "average_likes" in response.json()
    assert "average_comments" in response.json()
    print("test_get_counts_good_cmnt passed")



# 2️⃣平均いいね数の多いインフルエンサー上位N件を取得するAPI
@pytest.mark.trio
async def test_get_ave_good_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get(f"/influencers/top-by-likes?top_n={query_param}")
    # ステータスコード確認
    assert response.status_code == 200
    # レスポンス数確認
    assert len(response.json()) == query_param
    print("test_get_ave_good_topN passed")



# 3️⃣平均コメント数の多いインフルエンサー上位N件を取得するAPI
@pytest.mark.trio
async def test_get_ave_cmnt_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get(f"/influencers/top-by-comments?top_n={query_param}")
    # ステータスコード確認
    assert response.status_code == 200
    # レスポンス数確認
    assert len(response.json()) == query_param
    print("test_get_ave_cmnt_topN passed")



# 4️⃣textカラムに頻出の名詞上位N件を取得するAPI
@pytest.mark.trio
async def test_get_noun_topN():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get(f"/content/top-nouns?top_n={query_param}")
    # ステータスコード確認
    assert response.status_code == 200
    # レスポンス数確認
    assert len(response.json()) == query_param
    print("test_get_noun_topN passed")
