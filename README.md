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
├── django-app/                      # Django Backend
│   ├── label_music_manager/         # Core Django App
│   │   ├── migrations/              # Database migrations
│   │   ├── templates/               # Django HTML templates (if any)
│   │   ├── __init__.py
│   │   ├── admin.py                 # Admin panel config
│   │   ├── api_views.py             # API endpoints
│   │   ├── models.py                # Database models (Album, Artist, etc.)
│   │   ├── serializers.py           # DRF serializers
│   │   ├── urls.py                  # Backend routes
│   │   └── views.py                 # Traditional Django views
│   ├── media/                       # Uploaded album covers (auto-generated)
│   ├── manage.py
│   ├── requirements.txt             # Python dependencies
│   └── Pipfile                      # Alternative dependency config
│
├── react-app/                       # React Frontend
│   ├── public/                      # Static assets
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/              # Reusable UI Components
│   │   │   ├── AlbumCard.js         # Album display component
│   │   │   ├── Hero.js              # Landing page banner
│   │   │   ├── Navbar.js            # Navigation bar
│   │   │   └── SearchBar.js         # Search functionality
│   │   ├── pages/                   # Page-level components
│   │   │   ├── Home.js              # Homepage
│   │   │   └── Album.js             # Album details page
│   │   ├── App.js                   # Main app router
│   │   ├── constants.js             # API URLs, theme vars
│   │   └── index.js                 # React entry point
│   ├── package.json                 # Frontend dependencies
│   └── package-lock.json
│
├── .gitignore
├── README.md                        # Project documentation
└── venv/                            # Python virtual environment

``` 

