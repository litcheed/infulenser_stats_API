FROM python:3.12

WORKDIR /usr/src/python

# インストール
RUN apt-get update && apt-get install -y \
    --upgrade pip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# パッケージをインストール
COPY requirements.txt ./
RUN pip install -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . .
