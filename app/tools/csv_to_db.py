import pandas as pd
import mysql.connector
import sys

from common import cmn_msg
from common import cmn_session_db
from settings import setting


# 指定したいテーブル名
table_name = setting.DB_TABLE_NAME


def import_csv_to_mysql(csv_file_path):

    # CSVファイルの読み込み
    df = pd.read_csv(csv_file_path)

    # DB接続
    conn = cmn_session_db.conn_db()
    cursor = conn.cursor()

    # 各行DBに挿入
    for index, row in df.iterrows():
        insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(row))})"
        cursor.execute(insert_query, tuple(row))

    # 変更をコミットして接続を閉じる
    conn.commit()
    cursor.close()
    cmn_session_db.disconn_db

    print(f"CSVデータは {table_name} テーブルに正常にインポートされました。")

if __name__ == "__main__":
    # コマンドライン引数からCSVファイルパスとテーブル名を取得
    if len(sys.argv) != 3:
        print("Usage: python csv_to_db.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    table_name = sys.argv[2]

    import_csv_to_mysql(csv_file_path, table_name)
