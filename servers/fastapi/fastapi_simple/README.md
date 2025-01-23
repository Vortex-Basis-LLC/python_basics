# Simple FastAPI example

## Run Server
At command line with "vbg_basics" conda environment activated:
```
uvicorn main:app
```

It should start at http://127.0.0.1:8000. The root url should return JSON with
a "Hello World" message.