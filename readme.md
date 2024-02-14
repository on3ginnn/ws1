# Чтобы запустить:  

1. ```git clone https://github.com/on3ginnn/ws1```
2. ```cd ws1```
3. ```python -m venv venv```
4. ```venv\Scripts\activate``` or (if linux) ```source venv/Scripts/activate```
5. ```pip install -r requirements.txt```
6. Если при запуске (```python ws1/manage.py runserver```) вывело примерно такое сообщение:  
*```You have 20 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, catalog, contenttypes, sessions. Run 'python manage.py migrate' to apply them.```*  
Нужно: ```python ws1/manage.py migrate```
7. ```python ws1/manage.py createsuperuser```  
Имя: ```admin```  
Почта: ```admin@admin.com```  
Пароль: ```admin```  
Пароль еще раз: ```admin```  
8. ```python ws1/manage.py runserver```
9. Зайдя на админку можно создать каталог и продукты, которые привязываются к определенной категории в каталоге (многие-к-одному)  

Нажимая на каталог (3 иконка с конца), можно переходить по созданным категориям.