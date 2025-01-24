from fastapi import APIRouter
from fastapi.responses import HTMLResponse


from ..models import math_models
	

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


@router.post("/add")
def add(request: math_models.AddRequest) -> math_models.AddResponse:
	response = math_models.AddResponse(total = request.x + request.y)
	return response