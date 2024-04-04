# 準備

### CSVデータをDBへ格納するツール実行手順(初回のみ実行)

1. "\infulenser_stats_API\app\tools\csv"配下にcsvデータを配置

<br>

2. ターミナルからビルド実行
```
docker-compose up --build
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

5. CSVデータをDBへ格納するツール実行()
```
python app/tools/csv_to_db.py app/tools/csv/t_influencer_posts_202401121334.csv
```
<br>
<br>

# API実行

1. ターミナルからビルド実行
```
docker-compose up --build
```
<br>

2. ビルド完了後、起動したコンテナは閉じないまま別ターミナルを開きpythonコンテナのbash環境にアクセス
```
docker exec -it infulenser_stats_api-python-1 bash
```
<br>

3. 下記コマンドで各APIを実行
<br>
平均いいね数、平均コメント数を取得するAPI以外は?top_n=5の数値を別の数値に変えることで上位N件の件数を調整可能

- 平均いいね数、平均コメント数を取得するAPI
```
curl -X 'GET' 'http://127.0.0.1:8000/stats/average-likes-comments' -H 'accept: application/json' -w "\n"
```
<br>

- 平均いいね数の多いインフルエンサー上位N件を取得するAPI
```
curl -X 'GET' 'http://127.0.0.1:8000/influencers/top-by-likes?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>

- 平均コメント数の多いインフルエンサー上位N件を取得するAPI
```
curl -X 'GET' 'http://127.0.0.1:8000/influencers/top-by-comments?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>

- textカラムに頻出の名詞上位N件を取得するAPI
```
curl -X 'GET' 'http://127.0.0.1:8000/content/top-nouns?top_n=5' -H 'accept: application/json' -w "\n"
```
<br>
<br>

## テスト実行
上記手順2まで完了したら下記コマンドを入力
```
pytest -s app/test_main_api.py
```
