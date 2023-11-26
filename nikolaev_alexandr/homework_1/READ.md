## Sentiment Analysis using Transformers

### Установка необходимых библиотек

Для корректной работы кода необходимо установить следующие библиотеки:
```python
pip install transformers
pip install tensorflow
```

## Использование
Этот код демонстрирует использование библиотеки transformers для проведения анализа тональности текста с помощью предобученной модели BERT (rubert-base-cased-sentiment).
```python
from transformers import pipeline

# Инициализация классификатора для определения тональности текста
classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

# Примеры предложений для анализа
statements = [
    'Я обожаю инженерию машинного обучения!',
    'Я ненавижу инженерию машинного обучения!',
    'В нашем Университете преподают инженерию машинного обучения.'
]

# Получение результатов анализа
results = classifier(statements)
print(results)
```

## Функции
### check(results)
```python
def check(results):
    model_tonality = [i.get('label') for i in results]

    if model_tonality == ['POSITIVE', 'NEGATIVE', 'NEUTRAL']:
        print('Модель работает корректно.')
    else:
        print('Модель не справилась с определением тональности текста, попробуйте ввести более явные по тональности предложения.')
```

### definition(statements)
```python
def definition(statements):
    results = classifier(statements)
    print(results)
    return results
```

### main()
```python
def main():
    print('Введите три предложения: с позитивной, негативной и нейтральной тональностью текста:')
    
    tonality = ['POSITIVE', 'NEGATIVE', 'NEUTRAL']
    statements = []
    
    for i in range(3):
        statements.append(input('Предложение с {} тональностью: '.format(tonality[i])))
        print("Введённое Вами предложение с {} тональностью : ".format(tonality[i]), statements[i])
    
    results = definition(statements)
    check(results)

main()
```

## Описание
### Инициализация классификатора: 
Импортируется модуль pipeline из библиотеки transformers для создания классификатора classifier с использованием предобученной модели rubert-base-cased-sentiment.

### Примеры для анализа: Задаются три примера предложений с разной тональностью для анализа моделью.

## Функции:

### check(results): Проверяет, правильно ли модель определила тональность текста, и выводит соответствующее сообщение.
### definition(statements): Принимает список предложений и возвращает результаты анализа тональности.
### main(): Основная функция, вызывающая остальные функции для ввода пользователем предложений и анализа их тональности.

## Как использовать
Запустите скрипт.
Введите три предложения: с позитивной, негативной и нейтральной тональностью текста, как будет запрошено.
Посмотрите на результаты работы модели и её точность в определении тональности текста.
