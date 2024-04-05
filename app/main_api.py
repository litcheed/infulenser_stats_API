#!/usr/bin/env python3
#################################################################
#
# 概要:APIメインファイル
#      1️⃣平均いいね数、平均コメント数を取得するAPI
#      2️⃣平均いいね数の多いインフルエンサー上位N件を取得するAPI
#      3️⃣平均コメント数の多いインフルエンサー上位N件を取得するAPI
#      4️⃣textカラムに頻出の名詞上位N件を取得するAPI
#
#################################################################

import re
import sys
sys.path.append("/usr/src/python/app")
import spacy

from fastapi import FastAPI, Query
from collections import Counter

from common import cmn_msg
from common import cmn_session_db
from settings import setting



########################################
# 初期設定
########################################

# FastAPIオブジェクト
app = FastAPI()

# 指定したいテーブル名
table_name = setting.DB_TABLE_NAME

# spaCyの日本語モデルをロード
nlp = spacy.load("ja_core_news_sm")



####################################################################
# 1️⃣平均いいね数、平均コメント数を取得
####################################################################
@app.get("/stats/average-likes-comments")
async def get_counts_good_cmnt():
    
    #---------------#
    # DB接続
    #---------------#
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # データ取得
    #---------------#
    try:
        # 使用するテーブルを選択
        cursor.execute(f"USE {table_name}")

        # DBからデータ取得
        cursor.execute("""
            SELECT AVG(likes), AVG(comments)
            FROM influencers_posts
        """)

    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")


    #---------------#
    # 実行結果整形
    #---------------#
    try:
        # クエリ実行結果の取得
        avg_likes, avg_comments = cursor.fetchone()
        
        # JSON形式に整形
        result = {"average_likes": avg_likes, "average_comments": avg_comments}
    
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}実行結果の整形に失敗しました。\n{e}")


    #---------------#
    # DB切断
    #---------------#
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # 結果出力
    #---------------#
    return result



####################################################################
# 2️⃣平均いいね数の多いインフルエンサー上位N件を取得
####################################################################
@app.get("/influencers/top-by-likes")
async def get_ave_good_topN(top_n: int = Query(default=10, alias='top_n')):

    #---------------#
    # DB接続
    #---------------#
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # データ取得
    #---------------#
    try:
        # 使用するテーブルを選択
        cursor.execute(f"USE {table_name}")

        # DBからデータ取得
        cursor.execute("""
            SELECT influencer_id, AVG(likes) AS avg_likes
            FROM influencers_posts
            GROUP BY influencer_id
            ORDER BY avg_likes DESC
            LIMIT %s
        """, (top_n,))

    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")


    #---------------#
    # 実行結果整形
    #---------------#
    try:
        # クエリ実行結果の取得
        results = cursor.fetchall()
        
        # JSON形式に整形
        result = [
            {"influencer_id": result[0], "average_likes": float(result[1])}
            for result in results
        ]
    
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}実行結果の整形に失敗しました。\n{e}")
    

    #---------------#
    # DB切断
    #---------------#
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # 結果出力
    #---------------#
    return result



####################################################################
# 3️⃣平均コメント数の多いインフルエンサー上位N件を取得
####################################################################
@app.get("/influencers/top-by-comments")
async def get_ave_cmnt_topN(top_n: int = Query(default=10, alias='top_n')):

    #---------------#
    # DB接続
    #---------------#
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # データ取得
    #---------------#
    try:
        # 使用するテーブルを選択
        cursor.execute(f"USE {table_name}")

        # DBからデータ取得
        cursor.execute("""
            SELECT influencer_id, AVG(comments) AS avg_comments
            FROM influencers_posts
            GROUP BY influencer_id
            ORDER BY avg_comments DESC
            LIMIT %s
        """, (top_n,))

    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")


    #---------------#
    # 実行結果整形
    #---------------#
    try:
        # クエリ実行結果の取得
        results = cursor.fetchall()
        
        # JSON形式に整形
        result = [
            {"influencer_id": result[0], "average_comments": float(result[1])}
            for result in results
        ]
    
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}実行結果の整形に失敗しました。\n{e}")
    

    #---------------#
    # DB切断
    #---------------#
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # 結果出力
    #---------------#
    return result



####################################################################
# 4️⃣textカラムに頻出の名詞上位N件を取得
####################################################################
@app.get("/content/top-nouns")
async def get_noun_topN(top_n: int = Query(default=10, alias='top_n')):

    #---------------#
    # DB接続
    #---------------#
    try:
        conn, cursor = cmn_session_db.conn_db()
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # データ取得
    #---------------#
    try:
        # 使用するテーブルを選択
        cursor.execute(f"USE {table_name}")

        # DBからデータ取得
        cursor.execute("SELECT text FROM influencers_posts")

    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}クエリ実行に失敗しました。{e}")


    #---------------#
    # 実行結果整形
    #---------------#
    try:

        # クエリ実行結果の取得
        results = cursor.fetchall()

        # 名詞のカウント
        noun_counts = Counter()

        # フィルタリング用正規表現パターン
        regex_pattern = re.compile(r'\b\w{2,}\b')

        for text in results:
            # textがNoneでないことを確認
            if text[0] is not None:
                # テキストをspaCyで処理
                doc = nlp(text[0])
                # 名詞を抽出してカウント
                for token in doc:
                    # 名詞であり、正規表現にマッチするかのチェック
                    if token.pos_ == 'NOUN' and regex_pattern.match(token.text):
                        noun_counts[token.lemma_] += 1  # カウント

                # 頻出名詞の上位N件を取得
                most_common_nouns = noun_counts.most_common(top_n)

                # 結果を整形
                result = [{"noun": noun, "count": count} for noun, count in most_common_nouns]

    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}実行結果の整形に失敗しました。\n{e}")
    

    #---------------#
    # DB切断
    #---------------#
    try:
        cmn_session_db.disconn_db(conn, cursor)
        
    except Exception:
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗したためアプリを終了します。")
        sys.exit(1)
    

    #---------------#
    # 結果出力
    #---------------#
    return result
    