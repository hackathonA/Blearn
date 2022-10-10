
# 開発の仕方

### コンテナの起動方法

docker-compose.ymlのあるディレクトリで以下のコマンドを実行

```docker-compose up --build ```

MySQL、Django、phpmyadmin(DBのGUIツール)の全部で3つのコンテナが立ち上がる

### Djangoの起動ページを見る方法

ブラウザを開いて、以下のURLを検索バーに入力してenterキーを押すと、Djangoの起動ページを見れる（ロケットが飛ぶ絵）

`http://localhost:8000/ `


### phpmyadminからGUIでデータベースを見る方法

ブラウザを開いて、以下のURLを検索バーに入力してenterキーを押すと、GUIでデーターベースが見れる

`http://localhost:4000/ `


データベースの変更を反映したい場合

- 2つ方法があります。

1つ目の方法は、docker-composeコマンドからapp コンテナに命令する方法

1. docker-compose run app python manage.py makemigrations

2. docker-compose run app python manage.py migrate

これで、データベースに変更を反映できました。

2つ目の方法は、docker-compose exec app bashコマンドでappコンテナの中に入って、操作する方法です。

1. docker-compose exec app bash

2. python manage.py makemigrations

3. python manage.py migrate

これで、データベースに変更を反映できました。



