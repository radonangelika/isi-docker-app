#  Country Info App

Aplikacja webowa napisana we Flasku, która umożliwia:
- Wyszukiwanie krajów po nazwie
- Filtrowanie krajów według waluty
- Przeglądanie wszystkich dostępnych państw
- Dodawanie nowych krajów

![Zrzut ekranu 1](country-info-app/static/screen1.png)
![Zrzut ekranu 2](country-info-app/static/screen2.png)
![Zrzut ekranu 3](country-info-app/static/screen3.png)

---
## Uruchomienie online

[Zobacz działającą aplikację](https://isi-docker-app-1.onrender.com/)


##  Jak uruchomić lokalnie (Docker)

1. Zbuduj obraz:
   ```bash
   docker build -t country-api .
   ```
2. Uruchom kontener:
    ```bash
   docker run -p 5000:5000 country-api
   ```