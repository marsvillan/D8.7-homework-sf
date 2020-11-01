# D8.7-homework-sf.git
## Установка и запуск (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
  ```
$ git clone https://github.com/marsvillan/D8.7-homework-sf.git
$ cd D8.7-homework-sf.git
```
  - создать виртуальное окружение
  ```
$ python -m venv env
```
  - применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```
 - установить зависимости
  ```
$ pip install -r requirements.txt 
```

  - запустить сервер
  ```
$ python manage.py runserver 
```

### Использование
открыть страницу http://127.0.0.1:8000/

