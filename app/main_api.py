#!/usr/bin/env python3
#######################################################
#
# 概要:平均いいね数、平均コメント数をJSON形式で返すAPI
#
#######################################################

import time
import sys
import json
from fastapi import FastAPI, Query

from common import cmn_msg
from common import cmn_session_db
from settings import setting


app = FastAPI()

# 指定したいテーブル名
table_name = setting.DB_TABLE_NAME

# mysqlコンテナ起動待機
time.sleep(5)



@app.get("/stats/average-likes-comments")
async def get_counts_good_cmnt():
    """
    平均いいね数、平均コメント数を取得
    """
    
    # DB接続
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    try:
        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


@app.get("/influencers/top-by-likes")
async def get_ave_good_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均いいね数の多いインフルエンサー上位N件を取得
    """

    # DB接続
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    try:
        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


@app.get("/influencers/top-by-followers")
async def get_ave_flwr_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均フォロワー数の多いインフルエンサー上位N件を取得
    """

    # DB接続
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    try:
        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


@app.get("/influencers/top-by-comments")
async def get_ave_cmnt_topN(n: int = Query(default=10, alias='top_n')):
    """
    平均コメント数の多いインフルエンサー上位N件を取得
    """
    
    # DB接続
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    try:
        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


@app.get("/content/top-nouns")
async def get_noun_topN(n: int = Query(default=10, alias='top_n')):
    """
    textカラムに頻出の名詞上位N件を取得
    """

    # DB接続
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    try:
        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)



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
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    
    # 使用するテーブルを選択
    cursor.execute(f"USE {table_name}")

    # DBからデータ取得
    cursor.execute("""
        SELECT AVG(likes), AVG(comments)
        FROM influencers_posts
    """)

    # クエリ実行結果の取得
    result = cursor.fetchone()
    print(result)
    # クエリ実行結果JSON化
    # result_json = json.dumps(result, indent=4)
    # print(result_json)

    # DB切断
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)


if __name__ == '__main__':
    main()
