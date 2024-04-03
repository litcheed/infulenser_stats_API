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

