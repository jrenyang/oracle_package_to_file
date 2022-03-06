# oracle_package_to_file

## 用途

匯出Oracle資料庫下單一Schema的package。

## 安裝

需下載[Oracle Instant Client](https://www.oracle.com/tw/database/technologies/instant-client/downloads.html)將內部lib放置於`${project}/venv/Lib/site-packages`目錄下。

下載依賴套件。

```shell
> pip install -r requirements.txt
```

## 設定

編輯`${project}/resource/config.ini`設定當輸入連線資訊。

```ini
[data_source]
HOST=
PORT=
SCHEMA_NAME=
USER=
PASSWORD=
```

## 執行

```shell
> py app.py
```
