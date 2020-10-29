# appledaily-news-reader
A simple python crawler that grub news title, link and content.

## 關於本程式
### 功能說明
由於不想花太多時間點選新聞網頁，除了有廣告之外，要一口氣看完頭條新聞也是頗花時間的。
我頂多每天只願意花五分鐘的收信，順便看看昨天一整天到底發生什麼大事。
於是來製作一個**自動化的小工具，擷取新聞**。

### 專案結構
1. Python 新聞爬蟲程式
2. Python 登入 SMTP 郵件伺服器寄信功能
3. pyenv / pipenv / pip requirements.txt 等
4. Makefile 整合各不同階段所需要的指令
5. **Dockerfile 打包容器映像檔所需檔案**

看不懂上面的 1 ~ 4 沒關係，重點放在 **第5項**、打包映像檔。
如果你沒參與到 10 月 28 日的教學，而還不熟悉 **第5項**，
那沒關係，你還是可以直接用容器！！

### 本範例演示下列內容：
1. 讓一般使用者，透過容器技術，擺脫製作程式以及程式相依環境的情況，也能正確執行程式！！
2. 知道如何製作映像檔的人，可以有彈性地控制容器中程式的運作方式，像調整指令一樣。
3. 知道如何製作映像檔，且稍微可以讀懂程式碼的人，可以對這支程式進行小幅度修改，並且放在容器中執行。
4. 知道如何製作映像檔、又剛好熟悉程式撰寫的人，可以對這個專案做任何修改。


## 使用方式
### 取得 Gmail SMTP 登入金鑰
1. 為了實現寄信功能，我們要先取得自己信箱的登入金鑰。因此需要先進到 Google 帳號管理頁面，選擇 **[安全性](https://myaccount.google.com/security?gar=1)**，開啟「兩步驟驗證」
2. 接著，申請一組「應用程式密碼」；若您沒開啟「兩步驟驗證」，您將不會看到這個選項。
3. 依照下圖方式選擇密碼所允許的裝置或程式。這邊選擇「其他（自訂名稱）」
![](https://i.imgur.com/hPu7xoF.png)
4. 幫應用程式取名
![](https://i.imgur.com/qhxosPV.png)
5. 您將得到信箱的登入密碼，請妥善保管勿外流（長度16碼）。
![](https://i.imgur.com/e1wsbKe.png)

### 在自己的電腦上安裝 Docker

請參考連結： [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
在自己的電腦中安裝 Docker Engine
以便後續使用 docker 指令


### 準備映像檔
下方兩個準備映像檔方式，「下載」或「自製」，擇一即可！！
#### 下載我先前做好的映像檔
* 請參考 [https://hub.docker.com/r/nipapa/news-grabber](https://hub.docker.com/r/nipapa/news-grabber)
    ```docker pull nipapa/news-grabber```
#### 自製映像檔
* 請參考 [https://github.com/exsky/appledaily-news-reader.git](https://github.com/exsky/appledaily-news-reader.git)
* 在頁面按 code 按鈕，選擇下載程式碼的方式，若您不曾用過 git 指令，可以選擇下載 zip 也行。
* 透過 git 指令下載程式碼
    ```git clone https://github.com/exsky/appledaily-news-reader.git```
* 使用下列指令，製作容器映像檔
    ```docker build -t news-grabber . --no-cache```
* 包完之後檢查看看容器映像檔在不在
    ```docker images```
    
### 運作容器
* 這個 news-grabber 容器，因為在運作階段，會參考三個環境變數 `sender_addr`、`reciver_addr` 和 `secret`
* `sender_addr`: 寄件者 Email
* `secret`: 寄件者程式專用密碼 (上面我們所產生的那16碼)
* `reciver_addr`: 收件者 Email 
* 修改下方寄件者、收件者、寄件者密碼 ...

```
docker run --rm \
    -v /etc/localtime:/etc/localtime:ro \
    -e sender_addr=imnipapa@gmail.com \
    -e reciver_addr=alex19911118@gmail.com \
    -e secret=ixxxxxxxxxxxxxxm \
    nipapa/news-grabber make set_key run
```

![](https://i.imgur.com/aIwFsAi.jpg)

