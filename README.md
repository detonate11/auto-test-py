#Auto Test Project
проект по автоматизированному тестированию на Python
#Содержание
класс TriangleCalculator;
тесты unittest;
тесты pytest;
параметризованные тесты;
покрытия кода Coverage.py.
#Установка зависимостей
pip install -r requirements.txt
#Запуск тестов
python -m unittest discover -s tests -p "*test.py"
#Проверка покрытия
python -m coverage run -m unittest discover -s tests -p "*test.py" python -m coverage report -m