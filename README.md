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

## Rozdziały i spis treści

Portal ma cztery numerowane rozdziały, każdy w osobnym folderze z własną stroną wejściową `index.md`: `docs/podstawy/`, `docs/praktyka/`, `docs/technologia/`, `docs/nauka/`.

1. Edytuj albo dodaj plik `.md` w folderze rozdziału (na GitHubie wystarczy ikona ołówka; na każdej stronie portalu jest też przycisk edycji).
2. Nową stronę dopisz do `nav` w `mkdocs.yml`.
3. Strona [Spis treści](docs/spis-tresci.md) buduje się sama z `nav` i nagłówków `##` (hook [`hooks/spis_tresci.py`](hooks/spis_tresci.py)).
4. Uwagi, ramki z uzupełnieniami itp.: `!!! info "Tytuł"` i wcięta treść pod spodem.

## Filmy

Krótkie pliki `.mp4` trzymaj w `docs/assets/video/`, dłuższe osadzaj z YouTube lub Vimeo. Gotowe fragmenty kodu są na stronie [Jak rozwijać portal](docs/o-portalu.md).

## Podgląd lokalny

```bash
pip install -r requirements.txt
mkdocs serve
```

Strona będzie pod http://127.0.0.1:8000/.

## Publikacja na własny hosting (SSH)

Workflow [`.github/workflows/deploy-ssh.yml`](.github/workflows/deploy-ssh.yml) po każdym pushu do `main` buduje stronę i wysyła ją przez SSH (rsync) na własny serwer. Działa dopiero po dodaniu sekretów w **Settings → Secrets and variables → Actions**: `SSH_HOST`, `SSH_PORT`, `SSH_USER`, `SSH_KEY` (klucz prywatny), `SSH_PATH` (katalog docelowy) oraz `SSH_KEY_PASSPHRASE`, jeśli klucz ma hasło (cPanel wymaga hasła przy generowaniu klucza). Bez nich jest pomijany.

Hasło do strony ustawia się na serwerze plikami `.htaccess` i `.htpasswd` w katalogu docelowym; publikacja ich nie usuwa.
