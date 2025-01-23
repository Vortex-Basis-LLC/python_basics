# Simple FastAPI example

## Run Server
At command line with "vbg_basics" conda environment activated:
```
uvicorn main:app
```

The app should listen at http://127.0.0.1:8000. 
The root url should return an HTML welcome page.
"/some-json" should return a "Hello World" json message.