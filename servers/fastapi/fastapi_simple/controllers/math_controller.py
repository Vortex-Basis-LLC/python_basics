from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/math",
    tags=["Math"],
)

@router.get("/", response_class=HTMLResponse)
def root():
	return """<html>
	<head>
		<title>FastAPI Math Controller</title>
	</head>
	<body>
		<h1>Math</h1>
		<div>This is a an example controller for FastAPI.</div>
	</body>
</html>
"""

# TODO: Add some math related endpoints here.