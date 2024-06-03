# cat-facts

## Description
Basic web app to like cat facts and more 🐱!

## Technologies
- HTML
- Bootstrap 4.5.2
- Django 5.0.6

## Installation with Docker
1. In /catfacts run the following docker compose:
```bash
docker compose up --build
```
2. Open your browser and go to http://localhost:8000/
3. Have fun!

## About the Requirements of this app
- All functional requirements were implemented
- About non-functional requirements:
  - Architecture and Services:
    - Consumes the CatFacts API
    - The app uses the MVC architecture (in this case, the Django Version called Model-View-Template)
    - Uses a relational database (SQLite)
  - Software Quality:
    - Documentation for installation and usage
    - Use of Django's Class-Based Views (instead of Function-Based Views) for reusability and adherence to SOLID principles.
    - Uses conventionional commits with incremental changes: https://www.conventionalcommits.org/en/v1.0.0/
    - The app is mainly responsive
- Bonus:
    - Dockerized the application
    - Styled using a CSS framework (Bootstrap)
    - All Code in English (also since the API is in English)

## TODO
These are the things that I would like to implement in the future but I didn't have time to do it:
- Add a button to unlike a fact
- Paginate the facts from the API to show more facts than the first page
- Implement Tests
- Deploy with production settings
- Add branching style of git flow (but without using the software): main, development, feature branches, fix branches, hotfix, etc.
- Add default error pages (404, etc.)
