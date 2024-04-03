#!/usr/bin/env python3
#######################################################
#
# 概要:平均いいね数、平均コメント数をJSON形式で返すAPI
#
#######################################################

import time
import sys
from fastapi import FastAPI, Query

from common import cmn_msg
from common import cmn_session_db


app = FastAPI()

# mysql起動待機
time.sleep(5)

@app.get("/stats/average-likes-comments")
async def get_counts_good_cmnt():
    """
    平均いいね数、平均コメント数を取得
    """

@app.get("/influencers/top-by-likes")
async def get_ave_good_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均いいね数の多いインフルエンサー上位N件を取得
    """

@app.get("/influencers/top-by-followers")
async def get_ave_flwr_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均フォロワー数の多いインフルエンサー上位N件を取得
    """

@app.get("/influencers/top-by-comments")
async def get_ave_cmnt_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均コメント数の多いインフルエンサー上位N件を取得
    """

@app.get("/content/top-nouns")
async def get_noun_topN(n: int = Query(default=10, alias='top_n')):
    """
    textカラムに頻出の名詞上位N件を取得
    """


#----------------------------------#
# (テスト)メイン
#----------------------------------#
@app.get("/")
def main():
    """
    メイン関数
    """

    # DB接続
    try:
        conn = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    # DBからデータ取得
    


    # DB切断
    try:
        cmn_session_db.disconn_db(conn)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


if __name__ == '__main__':
    main()
