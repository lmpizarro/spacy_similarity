# spacy_similarity

Python 3.8.4rc1 (default, Jul  1 2020, 15:31:45) 
[GCC 9.3.0] on linux

```
docker-compose build
docker-compose down
```

``` 
curl -d '{"sentences": ["hello banana", "hello orange", "hello apple"]}' -H 'Content-Type: application/json' -X POST localhost:8000/get_similarity_tf
```


```
curl -d '{"sentences": ["hello banana", "hello orange", "hello apple"]}' -H 'Content-Type: application/json' -X POST localhost:8000/get_similarity_sp
```

[spacy](https://spacy.io/)

[usem](https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3)
