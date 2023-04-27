# backend
### 框架:
- flask
### 套件管理:
- poetry
### 如何在自己的電腦上開發:
1. **安裝poetry**
    
    Windows
    ```Bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```
    Mac/Linux
    ```Bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    or
    ```Bash
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```
    別忘了還要新增path到系統環境變數裡面!
2. **clone**
3. **創建虛擬環境**
    ```Bash
    cd backend
    poetry install  # 建立虛擬環境&安裝需要的套件
    poetry shell    # 進入虛擬環境
    ```
4. **執行app.py**
    ```Bash
    python app.py
    ```
