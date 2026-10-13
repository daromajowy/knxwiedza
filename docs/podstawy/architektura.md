# Architektura systemu

KNX jest systemem rozproszonym: każde urządzenie ma własny mikroprocesor, a czujniki i aktory rozmawiają bezpośrednio przez magistralę, bez centralnego sterownika. Podstawowe funkcje działają lokalnie, bez chmury i stałego internetu ([knx.org](https://www.knx.org/explore-knx/what-is-knx)).

**Topologia według knx.org** ([technologia](https://www.knx.org/knx-technology)):

- **Linia** TP łączy się z innymi przez **sprzęgło liniowe** (Line Coupler) na magistrali głównej.
- Do 15 linii tworzy **obszar**.
- Do 15 obszarów łączy się **sprzęgłami obszarowymi** (Area Coupler).
- **Router KNX IP** może zastąpić sprzęgła i spiąć sekcje TP przez sieć IP.
- **Sprzęgło mediów TP/RF** dołącza segment radiowy jako linię albo podsegment.

<figure class="knx-diagram" markdown="0">
<svg viewBox="0 0 760 400" role="img" aria-label="Topologia KNX: do 15 obszarów, w każdym do 15 linii" font-size="13">
<defs><marker id="topo-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="d-fill-edge"/></marker></defs>
<text x="24" y="34" font-size="15" font-weight="600" class="d-ink">Topologia KNX: do 15 obszarów, w każdym do 15 linii</text>
<rect x="24" y="56" width="712" height="40" rx="8" class="d-accent"/>
<text x="380" y="80" text-anchor="middle" font-weight="600" class="d-ink">Linia obszarowa 0.0 (TP) lub szkielet IP z routerami KNX IP</text>
<g class="d-edge" fill="none"><path d="M256 96V120" marker-end="url(#topo-arrow)"/><path d="M628 96V140" marker-end="url(#topo-arrow)"/><path d="M256 208V228" marker-end="url(#topo-arrow)"/><path d="M140 260V284" marker-end="url(#topo-arrow)"/><path d="M372 260V284" marker-end="url(#topo-arrow)"/></g>
<rect x="24" y="120" width="464" height="252" rx="8" fill="none" class="d-edge" stroke-dasharray="4 4"/>
<text x="40" y="144" font-weight="600" class="d-ink">Obszar 1 (np. budynek lub piętro)</text>
<rect x="40" y="168" width="432" height="40" rx="8" fill="none" class="d-edge"/>
<text x="256" y="192" text-anchor="middle" class="d-ink">Sprzęgło obszarowe 1.0.0</text>
<rect x="40" y="228" width="432" height="32" rx="8" class="d-edge d-tint"/>
<text x="256" y="248" text-anchor="middle" class="d-ink">Linia główna 1.0 · do 15 linii</text>
<rect x="40" y="284" width="200" height="72" rx="8" fill="none" class="d-edge"/>
<text x="56" y="308" font-weight="600" class="d-ink">Linia 1.1</text>
<text x="56" y="324" font-size="11.5" class="d-quiet">sprzęgło liniowe 1.1.0</text>
<text x="56" y="340" font-size="11.5" class="d-quiet">do 64 urządzeń: 1.1.1, 1.1.2…</text>
<rect x="272" y="284" width="200" height="72" rx="8" fill="none" class="d-edge"/>
<text x="288" y="308" font-weight="600" class="d-ink">Linia 1.15</text>
<text x="288" y="324" font-size="11.5" class="d-quiet">sprzęgło liniowe 1.15.0</text>
<text x="288" y="340" font-size="11.5" class="d-quiet">do 64 urządzeń: 1.15.1…</text>
<rect x="520" y="140" width="216" height="72" rx="8" fill="none" class="d-edge"/>
<text x="536" y="164" font-weight="600" class="d-ink">Obszary 2–15</text>
<text x="536" y="180" font-size="11.5" class="d-quiet">każdy zbudowany jak obszar 1</text>
<text x="536" y="196" font-size="11.5" class="d-quiet">sprzęgła 2.0.0 … 15.0.0</text>
</svg>
<figcaption>Topologia KNX TP: obszary, linie, urządzenia</figcaption>
</figure>

Adres fizyczny urządzenia wynika z miejsca w tym drzewie: obszar.linia.urządzenie (numeracja i limit 64 urządzeń to wiedza ogólna, nie z knx.org).

!!! info "Uzupełnienie spoza knx.org (wiedza ogólna, podstawa kursu KNX Basic)"

    - **Adres fizyczny** (indywidualny) w formacie obszar.linia.urządzenie, np. 1.1.5, identyfikuje urządzenie przy programowaniu w ETS. Na linii TP jest do 64 urządzeń bez wzmacniaczy (do 256 z repeaterami).
    - **Adres grupowy**, np. 1/0/1 (trzypoziomowy), łączy funkcje: przycisk wysyła telegram na adres grupowy, a wszystkie aktory nasłuchujące tego adresu reagują.
    - **Obiekty komunikacyjne** to „wejścia i wyjścia” urządzenia, które w ETS przypisuje się do adresów grupowych.
    - **Typy punktów danych (DPT)** określają format wartości, np. DPT 1.001 to przełączanie, DPT 9.001 temperatura w °C.
    - **Telegram** to ramka z adresem nadawcy, adresem docelowym i danymi; magistrala TP pracuje z szybkością 9,6 kbit/s, a kolizje rozstrzyga metoda CSMA/CA.
