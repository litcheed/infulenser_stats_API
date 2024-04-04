import sys
sys.path.append("/usr/src/python/app")
import pandas as pd
import mysql.connector

from common import cmn_msg
from common import cmn_session_db
from settings import setting


# 指定したいテーブル名
table_name = setting.DB_TABLE_NAME

def create_table_if_not_exists(cursor, table_name):
    try:
        # テーブル作成用のSQLクエリ
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            influencer_id INT,
            post_id BIGINT,
            shortcode VARCHAR(20),
            likes INT,
            comments INT,
            thumbnail TEXT,
            text TEXT,
            post_date DATETIME
        );
        """
        # テーブルが存在しない場合にのみ作成
        cursor.execute(create_table_query)
        print(f"{cmn_msg.INFO_MSG}テーブル `{table_name}` が作成されました（既に存在している場合はスキップ）。")
    except Exception as e:
        print(f"{cmn_msg.WARN_MSG}テーブル作成に失敗しました。\n{e}")


def import_csv_to_mysql(csv_file_path):

    # CSVファイルの読み込み
    df = pd.read_csv(csv_file_path)
    
    # NaN値をNoneに置換
    df = df.where(pd.notnull(df), None)

    # DB接続
    conn, cursor = cmn_session_db.conn_db()

    # 使用するテーブルを選択
    cursor.execute(f"USE {table_name}")

    # テーブルが存在しない場合、作成
    create_table_if_not_exists(cursor, table_name)

    # 各行DBに挿入
    for index, row in df.iterrows():
        # SQLクエリのプレースホルダーに合わせてパラメータを準備
        insert_query = f"INSERT INTO {table_name} (influencer_id, post_id, shortcode, likes, comments, thumbnail, text, post_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        # Seriesオブジェクトから値の配列を取得し、タプルに変換
        row_tuple = tuple(row.values)
        cursor.execute(insert_query, row_tuple)

    # 変更をコミットして接続を閉じる
    conn.commit()
    cmn_session_db.disconn_db(conn, cursor)

    print(f"{cmn_msg.INFO_MSG}CSVデータは {table_name} テーブルに正常にインポートされました。")

if __name__ == "__main__":
    # コマンドライン引数からCSVファイルパスを取得
    if len(sys.argv) != 2:
        print("Usage: python csv_to_db.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]

    import_csv_to_mysql(csv_file_path)
