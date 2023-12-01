# Creating API for our Previous Model

## What does this project?

We have developed an API to leverage the abilities of our previous model.

## How can I create my own API using this model?

You can create your own API by following these simple steps:

1. Install the required packages listed in the requirements.txt file:

```
pip install -r requirements.txt
```

2. Run the application file:

```
uvicorn ask_friend:app
```

## How can I interact with the model using the API?

There are two ways to interact with the API:

1. Using Postman

Send a POST request with raw JSON data containing your question. For example:

```
{
    "text": "Где ты учишься?"
}

```

The model will respond with:

```
{
    "score": 0.6466110348701477,
    "start": 42,
    "end": 86,
    "answer": " в Уфимском университете."
}
```

2. Using cURL

Send a POST request using cURL. For example:
```
curl -X 'POST' \
  'http://localhost:8000/answer/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Как дела?"
}'
```

The model will respond with:

```
{
  "score": 0.8254371881484985,
  "start": 24,
  "end": 33,
  "answer": " 22 года."
}

```

Feel free to choose the method that suits your preference for interacting with the model through the API.
