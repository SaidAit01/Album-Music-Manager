# MyMusicMaestro

## Key Features
✔ Album Discovery: Browse music with rich visuals and metadata
✔ Interactive UI: Smooth hover animations and responsive design
✔ Search Functionality: Find albums by title, artist, or year
✔ Admin Dashboard: Django backend for content management
✔ RESTful API: Headless architecture for scalability

## Setup Guide
### Prerequisites

Python 3.8+
Node.js 16+
PostgreSQL (optional)

### installation 
1. Backend Setup :

```
cd django-app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
2. Frontend SetUp :

```
cd react-app
npm install
npm start
```
## Project Structure : 
```
MyMusicMaestro/  
├── django-app/            # Django backend  
│   ├── label_music_manager/ # Core app  
│   └── media/              # Album covers storage  
├── react-app/             # React frontend  
│   ├── src/components/     # Reusable UI  
│   └── src/pages/          # Views

``` 

