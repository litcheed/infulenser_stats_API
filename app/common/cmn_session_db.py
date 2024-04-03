#######################################################
#
# 概要:DBのセッションを管理する。接続、切断等
# 記載関数:
#   conn_db
#   disconn_db
#
#######################################################

import traceback
import mysql.connector

from common import cmn_msg
from settings import setting

def conn_db():
    """
    DBに接続する

    Args:
        なし
    Returns:
        conn: DB接続オブジェクト
        cursor: DBカーソル
    Note:
    """

    # DB接続設定
    config = {
      'user': setting.DB_USER,               # MySQLのユーザー名
      'password': setting.DB_PASS,           # MySQLのパスワード
      'host': setting.DB_HOST,               # MySQLサーバーのホスト名
      'raise_on_warnings': True
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        print(f"{cmn_msg.INFO_MSG}DB接続しました。")
        return conn, cursor

    except Exception as e:
        tb = traceback.format_exc()
        print(f"{cmn_msg.ERR_MSG}DB接続に失敗しました。\n{tb}")
        raise Exception


def disconn_db(conn, cursor):
    """
    DBと切断する

    Args:
        conn: DB接続オブジェクト
        cursor: DBカーソル
    Returns:
        なし
    Note:
    """

    try:
        cursor.close()
        conn.close()
        print(f"{cmn_msg.INFO_MSG}DB切断しました。")

    except Exception as e:
        tb = traceback.format_exc()
        print(f"{cmn_msg.ERR_MSG}DB切断に失敗しました。\n{tb}")
        raise Exception
