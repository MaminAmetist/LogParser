## LogParser
LogParser — это Python-скрипт для анализа логов в формате JSON. Он собирает статистику по каждому эндпоинту и формирует отчет со средней скоростью ответа и количеством запросов.

### Возможности
1. Поддержка одного или нескольких лог-файлов
2. Формирование отчета average: количество обращений к каждому эндпоинту, среднее время отклика
3. Фильтрация по дате (опционально)
4. Удобный вывод отчета в консоль с помощью tabulate
5. Возможность расширения: легко добавить новые типы отчетов

### Установите зависимости:

```bash
pip install -r requirements.txt
```
### Запуск скрипта:

```bash
python main.py --file logs/example1.log --report average
```

#### Можно передать несколько файлов:

bash
```bash
python main.py --file logs/file1.log logs/file2.log --report average
```

### Фильтрация по дате (YYYY-MM-DD):

```bash
python main.py --file logs/example1.log --report average --date 2025-08-01
```