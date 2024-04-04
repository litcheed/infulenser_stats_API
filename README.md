### ツール実行

ビルド
```
docker build -t api-image .
```
コンテナ起動
```
docker run -it api-image /bin/bash

```

```
pwd
/usr/src/pythonであることを確認。
python app/tools/csv_to_db.py app/tools/csv/t_influencer_posts_202401121334.csv
```

docker build -t api-image .
docker run  --rm -it api-image /bin/bash



curl -X 'GET' 'http://127.0.0.1:8000/stats/average-likes-comments' -H 'accept: application/json' -w "\n"
curl -X 'GET' 'http://127.0.0.1:8000/influencers/top-by-likes?top_n=5' -H 'accept: application/json' -w "\n"

curl -X 'GET' 'http://127.0.0.1:8000/influencers/top-by-comments?top_n=5' -H 'accept: application/json' -w "\n"
curl -X 'GET' 'http://127.0.0.1:8000/content/top-nouns?top_n=5' -H 'accept: application/json' -w "\n"





テスト実行
pytest -s app/test_main_api.py
