# vectorize_text
Remote Crew Challenge


# Running code

## Python directly (Python 3.11)

1 - Install requirements from requirements.txt 

```shell
pip install -r requirements.txt
```

2 - Run main.py script
```shell
python main.py
```

## Using Docker compose

1 - Start service 
```shell
docker compose up
```

2 - Access container terminal
```
docker run -it vectorize_text_web /bin/bash
```

3 - Run main.py script
```shell
python main.py
```