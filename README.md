# Lab25_30

## Stack technologiczny

Backend aplikacji został zbudowany z wykorzystaniem frameworka Django, który odpowiada za logikę aplikacji oraz zarządzanie danymi. Do tworzenia i obsługi REST API wykorzystano Django REST Framework. Dane przechowywane są w relacyjnej bazie danych SQLite. Warstwa frontendowa została opracowana z użyciem Tailwind CSS.

[![Django][django]][django-url]
[![Django REST Framework][django-rest-framework]][django-rest-framework-url]
[![SQLite][sqlite]][sqlite-url]
[![Tailwind CSS][tailwind-css]][tailwind-css-url]

## Instrukcja uruchomienia

### Warunki wstępne
Do uruchomienia aplikacji wymagane jest środowisko z zainstalowanym Pythonem oraz menedżerem pakietów pip. Aplikacja była testowana na Pythonie w wersji 3.13.3 oraz menedżerze pakietów pip w wersji 25.0.1.

### Uruchomienie aplikacji

1. Sklonuj repozytorium
   ```sh
   git clone https://github.com/Happy155/Lab25_30.git
   ```
2. Przejdź do folderu repozytorium
   ```sh
   cd Lab25_30/
   ```
3. Utwórz wirtualne środowisko
   ```sh
   # Windows
   python -m venv venv
   
   # Linux/macOS
   python3 -m venv venv
   ```
4. Aktywuj wirtualne środowisko
   ```sh
   # Windows (cmd)
   venv\Scripts\activate

   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # Linux/macOS
   source venv/bin/activate
   ```
5. Zainstaluj wymagane pakiety
   ```sh
   pip install -r requirements.txt
   ```
6. Uruchom aplikację
   ```sh
   # Windows
   python manage.py runserver

   # Linux/macOS
   python3 manage.py runserver
   ```
Po wykonaniu powyższych kroków strona powinna już działać i być dostępna pod adresem http://localhost:8000.

## Zrzuty ekranu
![Aplikacja publiczna][aplikacja-publiczna-screenshot]
![Aplikacja panel][aplikacja-panel-screenshot]
![Panel administracyjny][panel-administracyjny-screenshot]
![Formularz][formularz-screenshot]
![Endpoint API][endpoint-api-screenshot]












[django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[django-url]: https://www.djangoproject.com/
[django-rest-framework]: https://img.shields.io/badge/Django_REST_Framework-092E20?style=for-the-badge&logo=django&logoColor=green
[django-rest-framework-url]: https://www.django-rest-framework.org/
[sqlite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white
[sqlite-url]: https://sqlite.org/
[tailwind-css]: https://img.shields.io/badge/Tailwind_CSS-2E3A57?style=for-the-badge&logo=tailwind-css&logoColor=38B2AC
[tailwind-css-url]: https://tailwindcss.com/

[aplikacja-publiczna-screenshot]: images/Aplikacja%20publiczna.png
[aplikacja-panel-screenshot]: images/Aplikacja%20panel.png
[panel-administracyjny-screenshot]: images/Panel%20administracyjny.png
[formularz-screenshot]: images/Formularz.png
[endpoint-api-screenshot]: images/Endpoint%20API.png
