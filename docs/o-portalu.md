# Jak rozwijać portal

Krótka ściąga dla autora: gdzie dopisywać rozdziały i jak wstawiać filmy.

## Nowy rozdział lub podrozdział

1. Dodaj plik `.md` w folderze rozdziału, np. `docs/podstawy/telegramy.md`. Pierwsza linia to tytuł strony: `# Telegramy KNX`.
2. Dopisz stronę do menu w `mkdocs.yml` w sekcji `nav`, pod właściwym rozdziałem.
3. Podrozdziały wewnątrz strony zaczynaj od `## `. Pojawią się w [spisie treści](spis-tresci.md) i w bocznym menu strony.
4. Nowy rozdział główny to nowy folder z plikiem `index.md` (strona wejściowa rozdziału) i nowa pozycja w `nav`.

## Film z repozytorium

Plik `.mp4` wrzuć do `docs/assets/video/` i wstaw na stronie:

```html
<figure class="film" markdown="0">
  <div class="video">
    <video controls preload="metadata" src="../../assets/video/grouping.mp4"></video>
  </div>
  <figcaption>ETS6: tworzenie adresów grupowych (2:55)</figcaption>
</figure>
```

Ścieżka `src` jest względna do strony. Ze strony w podfolderze (np. `docs/praktyka/…`) to `../../assets/video/plik.mp4`, a ze strony w głównym folderze `docs/` to `../assets/video/plik.mp4`.

!!! warning "Duże pliki"

    GitHub nie przyjmuje plików większych niż 100 MB, a cała strona na GitHub Pages powinna mieścić się w 1 GB. Krótkie filmy (kilka–kilkadziesiąt MB) można trzymać w repo. Dłuższe lepiej wrzucić na YouTube lub Vimeo i osadzić jak niżej.

## Film z YouTube lub Vimeo

Na YouTube: **Udostępnij → Umieść**, skopiuj adres z `src` i wstaw:

```html
<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/IDENTYFIKATOR_FILMU"
          title="Tytuł filmu" allowfullscreen loading="lazy"></iframe>
</div>
```

Dla Vimeo adres ma postać `https://player.vimeo.com/video/NUMER`.

## Prawa do filmów

Repozytorium i strona na GitHub Pages są publiczne. Publikuj własne nagrania albo takie, na które masz zgodę autora. Do cudzych filmów lepiej dać link lub osadzić je z oryginalnego kanału (YouTube), niż kopiować plik do repo.
