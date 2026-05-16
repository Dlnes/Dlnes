# Dlnes
API на Python. Библиотека FastAPI.
1. Убедитесь, что база данных `octagon_db` создана в PostgreSQL.
Её можно создать командой
sudo -u postgres createdb -O octagon octagon_db
2. Можно заполнить тестовой литературой(необязательно). Для этого нужно выполнить файл init_db.py
3. Запуск осуществляется в ~/Dlnes командой
uvicorn "app.main:app" --reload --host 0.0.0.0 --port 8000