# vue-django-roman_arabic_converter

## 1: Initial Setup

### Clone a project in a new directory:
```bash
cd path/to/a/new/directory
git clone https://github.com/MaksNech/vue-django-roman_arabic_converter.git
```

### You should have python virtualenv for run backend, if no:
Install virtualenv:
```bash
pip install virtualenv
```
Create virtualenv:
```bash
mkdir env && virtualenv env
```
Initialize the Virtual Environment:
```bash
source env/bin/activate
```

### Install dependencies:
Install django rest framework: 
```bash
pip install django djangorestframework
```
Install django-cors-heders:
```bash
pip install django-cors-heders
```

## 2: Getting Started

### Start backend:
run virtualenv with terminal command:
```bash
source env/bin/activate
```
if virtualenv is running:
```bash
cd backend
python manage.py runserver
```

### Start frontend:
```bash
cd frontend
npm i
npm run dev
```
### The project should be started on:
http://localhost:8080/
