# Media transmisyjne i bezpieczeństwo

KNX TP (skrętka) jest najpopularniejszym medium, a pozostałe media łączą się z nim przez sprzęgła i routery ([knx.org](https://www.knx.org/knx-technology)).

| Medium | Do czego służy (wg knx.org) |
| --- | --- |
| KNX TP | Przewodowa magistrala na skrętce, zasilana z zasilacza KNX; standard w nowych instalacjach |
| KNX RF | Radio sub-GHz; modernizacje, czujniki bateryjne lub bezbateryjne, odległe strefy |
| KNXnet/IP (IPv4) | Szkielet IP oraz tunelowanie przez interfejsy i routery KNX IP |
| KNX IoT (IPv6) | Wi-Fi, Ethernet i Thread; warstwa fizyczna poza specyfikacją KNX |
| KNX PL (powerline) | Nie wymieniony na knx.org; historycznie transmisja po przewodach 230 V (wiedza ogólna) |

**KNX Secure** szyfruje komunikację i uwierzytelnia urządzenia; obsługuje go ETS6 ([ETS](https://www.knx.org/what-ets)). **Segment Proxy** (Security Proxy) tłumaczy ruch KNX Data Secure na zwykły KNX, dzięki czemu bezpieczne urządzenia nie komunikują się wprost z niezabezpieczonymi.

**KNX IoT** otwiera KNX na świat IP i usług zewnętrznych:

- **KNX IoT Point API** to urządzenia IPv6 certyfikowane na poziomie stosu i aplikacji.
- **KNX IoT API Server** udostępnia znormalizowane API oparte na KNX Information Model, który ETS6 eksportuje natywnie.
- **KNX IoT Router** łączy urządzenia TP, RF i IPv4 z urządzeniami KNX IoT, także razem z Thread Border Routerem.
