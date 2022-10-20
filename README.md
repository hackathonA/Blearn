# Blearn

# 開発の仕方(コンテナが起動している前提です。起動の仕方は、下の方に書いてあります。)

// appの作り方

` docker-compose run app python manage.py startapp 好きなapp名 `

// appの操作の仕方(コンテナに入るコマンドです)

` docker-compose exec app bash `

※ コンテナを立ち上げた後は、modelsの情報をMySQLの方に知らせる必要があるので、以下の方法で必ず行ってください！

(立ち上げの際に行うのは、migrateだけで大丈夫です)

// データベースの変更を反映したい場合

- 2つ方法があります。

1つ目の方法は、docker-composeコマンドからapp コンテナに命令する方法

1. docker-compose exec app python manage.py makemigrations

2. docker-compose exec app python manage.py migrate

これで、データベースに変更を反映できました。

2つ目の方法は、docker-compose exec app bashコマンドでappコンテナの中に入って、操作する方法です。

1. docker-compose exec app bash

2. python manage.py makemigrations

3. python manage.py migrate

これで、データベースに変更を反映できました。

# 開発の終了方法

// コンテナから抜け出す方法(exitは、ターミナル,GitBashに打ちます。)

`exit または、ctrl+d で抜けられます。`

docker-compose.ymlのあるディレクトリで以下のコマンドを上から順番に実行

` docker-compose down -v `

` docker rm $(docker ps -a -q) `

` docker rmi $(docker images -q) `

` docker system prune `


次に開発する際の起動は、上記のdocker-compose up

# コンテナの起動方法

docker-compose.ymlのあるディレクトリで以下のコマンドを実行

` docker-compose up -d --build `

MySQL、Django、phpmyadmin(DBのGUIツール)の全部で3つのコンテナが立ち上がる

### Djangoの起動ページを見る方法

ブラウザを開いて、以下のURLを検索バーに入力してenterキーを押すと、Djangoの起動ページを見れる（ロケットが飛ぶ絵）

`http://localhost:8000/ `


### phpmyadminからGUIでデータベースを見る方法

ブラウザを開いて、以下のURLを検索バーに入力してenterキーを押すと、GUIでデーターベースが見れる(migrate指定ないと、Djangoの方のデータは見れません)

` http://localhost:4000/ `

