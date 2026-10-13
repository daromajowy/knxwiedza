# Portal wiedzy KNX

Statyczny portal po polsku z opracowaniem wiedzy o standardzie KNX: podstawy, architektura, adresowanie, praca w ETS6, media i bezpieczeństwo, zastosowania, serwery wizualizacji oraz ścieżka certyfikacji.

Po włączeniu GitHub Pages portal będzie dostępny pod adresem **https://daromajowy.github.io/knxwiedza/**.

## Jak to działa

- Treść leży w folderze [`docs/`](docs/) jako zwykłe pliki Markdown, jedna strona na temat.
- Menu i ustawienia są w [`mkdocs.yml`](mkdocs.yml) (sekcja `nav`).
- Strona jest budowana narzędziem [MkDocs](https://www.mkdocs.org/) z motywem [Material](https://squidfunk.github.io/mkdocs-material/), który daje nawigację, wyszukiwarkę i tryb ciemny.
- Workflow [`.github/workflows/pages.yml`](.github/workflows/pages.yml) buduje stronę przy każdym PR i publikuje ją po każdym pushu do `main`.

## Pierwsze uruchomienie GitHub Pages

W repozytorium: **Settings → Pages → Build and deployment → Source: GitHub Actions**. Potem wystarczy push do `main` (albo ręczne uruchomienie workflow w zakładce Actions).

## Dodawanie i edycja treści

1. Edytuj albo dodaj plik `.md` w `docs/` (na GitHubie wystarczy ikona ołówka; na każdej stronie portalu jest też przycisk edycji).
2. Nową stronę dopisz do `nav` w `mkdocs.yml`.
3. Uwagi, ramki z uzupełnieniami itp.: `!!! info "Tytuł"` i wcięta treść pod spodem.

## Podgląd lokalny

```bash
pip install -r requirements.txt
mkdocs serve
```

Strona będzie pod http://127.0.0.1:8000/.
