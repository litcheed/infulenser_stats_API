![Alt](https://repobeats.axiom.co/api/embed/401f0edf675b873d4e6a65f114ec03f8baed8ca2.svg "Repobeats analytics image")

# 目次

- [目次](#目次)
- [準備](#準備)
    - [CSVデータをDBへ格納するツール実行手順(初回のみ実行)](#csvデータをdbへ格納するツール実行手順初回のみ実行)
- [メインAPI](#メインapi)
    - [API実行](#api実行)
    - [テスト実行](#テスト実行)
- [ディレクトリ・ファイル詳細](#ディレクトリファイル詳細)
---

<br>
<br>

# 準備

### CSVデータをDBへ格納するツール実行手順(初回のみ実行)

1. tools配下にcsvフォルダを生成し、そこにcsvデータを配置<br>
"\infulenser_stats_API\app\tools\csv\t_influencer_posts_202401121334.csv"

<br>

2. ターミナルからビルド実行(初回起動時は時間がかかるため注意)
```
docker-compose up --build
```
※下記のような出力がされたらmysqlコンテナビルド完了<br>
```
infulenser_stats_api-db-1      | 2024-04-05T10:29:05.748103Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.3.0'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
```
※下記のような出力がされたらpythonコンテナビルド完了<br>
```
infulenser_stats_api-python-1  | INFO:     Application startup complete.
```
<br>

3. ビルド完了後、コンテナは閉じないまま別ターミナルを開きpythonコンテナのbash環境にアクセス
```
docker exec -it infulenser_stats_api-python-1 bash
```
<br>

4. bashアクセス後、カレントディレクトリが"/usr/src/python"であることを確認
```
pwd
```
<br>

5. CSVデータをDBへ格納するツール実行
```
python app/tools/csv_to_db.py app/tools/csv/t_influencer_posts_202401121334.csv
```
<br>
<br>

# メインAPI

### API実行

1. ターミナルからdocker-compose up実行 ("準備 2."でビルド完了済み想定。ビルドがまだの場合は"準備 2."のように--build付与)
```
docker-compose up
```
<br>

2. 起動完了後、起動したコンテナは閉じないまま別ターミナルを開きpythonコンテナのbash環境にアクセス
```
docker exec -it infulenser_stats_api-python-1 bash
```
<br>

3. 下記コマンドで各APIを実行
<br>
平均いいね数、平均コメント数を取得するAPI以外は?top_n=5の数値を別の数値に変えることで上位N件の件数を調整可能

- 平均いいね数、平均コメント数を取得するAPI
```
curl 'http://127.0.0.1:8000/stats/average-likes-comments' -H 'accept: application/json' -w "\n"
```
<br>

- 平均いいね数の多いインフルエンサー上位N件を取得するAPI
```
curl 'http://127.0.0.1:8000/influencers/top-by-likes?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>

- 平均コメント数の多いインフルエンサー上位N件を取得するAPI
```
curl 'http://127.0.0.1:8000/influencers/top-by-comments?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>

- textカラムに頻出の名詞上位N件を取得するAPI
```
curl 'http://127.0.0.1:8000/content/top-nouns?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>
<br>

### テスト実行
上記手順2まで完了したら下記コマンドを入力
```
pytest -s app/test_main_api.py
```
<br>
<br>

# ディレクトリ・ファイル詳細

**app**
<br>
　全ソースコードを格納<br>
・main_api.py : webAPIメインファイル<br>
・test_main_api.py : webAPIテストファイル
<br>

**app/common**
<br>
　共通関数や共通変数ファイルを格納。ファイル詳細はcommon内のcmn_list.mdを参照
<br>

**app/setting**
<br>
　共通設定ファイルを格納
<br>

**app/tools**
<br>
　CSVデータをRDBへ格納するツール関連
<br>

**app/tools/csv**
<br>
　ここにRDBに保存したいCSVデータを配置する
<br>
