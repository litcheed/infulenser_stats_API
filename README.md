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



nohup uvicorn app.main_api:app --reload > uvicorn.log 2>&1 &

実行中プロセス確認
jobs

ジョブ番号確認
ps

ジョブの停止
kill ジョブ番号