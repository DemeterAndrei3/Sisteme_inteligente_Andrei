# Sisteme_inteligente_Andrei

# Stație meteorologică

## Descriere generală
Proiectul își propune realizarea unei stații meteorologice care colectează și analizează date despre condițiile meteo locale. Scopul este să monitorizăm parametri precum temperatura, umiditatea, presiunea atmosferică și, eventual, viteza vântului, pe o perioadă de timp.

## Obiective
- Colectarea datelor meteo la intervale regulate de timp.
- Stocarea datelor într-un fișier (de exemplu, CSV) sau într-o bază de date.
- Realizarea unor grafice pentru evoluția temperaturii, umidității etc.
- Analiza unor tendințe simple (de exemplu, variația temperaturii pe parcursul unei zile sau al unei săptămâni).

## Dataset
Datasetul va conține măsurători meteo înregistrate la intervale regulate (de exemplu, la fiecare 5 sau 10 minute). Fiecare înregistrare va avea:
- Data și ora
- Temperatura (°C)
- Umiditatea (%)
- Presiunea atmosferică (hPa)
- (Opțional) Viteza vântului (m/s)

Fișierul de date va fi încărcat în acest repository, în folderul `data/`, sub forma unui fișier CSV, de exemplu: `data/masuratori_meteo.csv`.

## Posibile extinderi
- Afișarea datelor în timp real într-o interfață grafică sau pe un dashboard web.
- Calcularea unor statistici (medie, minim, maxim pe zi/săptămână).
- Compararea datelor locale cu date de la o sursă meteo online.
