
Create your virtual environment in your folder
	c:\>python -m venv c:\path\to\myenv

Activate your venv
	C:\> <venv>\Scripts\Activate.ps1
	
https://docs.python.org/3/library/venv.html check the page for further assitance


Now install uvicorn, transformers and torch:
	pip install torch
	pip install transformers
	pip install fastapi uvicorn
	
Paste the main.py file in your folder

Now run your API with:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000

Now you can hit the API like:
POST	http://localhost:8000/predict?text= Mary suffers from fever and takes paracetamol tablets

