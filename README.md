# dev-business-logic
Для развёртывания следуйте следующим шагам:
```
git clone https://github.com/Berlimor/dev-business-logic.git
docker-compose up --build -d
```

## Эндпоинты
### /operator/manual-input
Эндпоинт принимает в качестве параметра запроса гос номер машины. Используется в случае, когда не удаётся считать номер.

### /operator/start
Начало работы оператора. Выдаёт респонс, в теле которого status_code=504

### /operator/stop
Конец работы оператора.
