# 📝 Esercitazioni Django API

Questo repository raccoglie i miei progetti e le esercitazioni pratiche svolte durante il percorso di formazione. Utilizzo questo progetto come ambiente di test per consolidare le basi dello sviluppo Backend e della gestione delle API REST.

## 🚀 Come avviare il progetto

Per testare l'API localmente sul tuo computer, segui questi passaggi:

1. **Clona il repository**:
   ```bash
   git clone <link-del-tuo-repo>
   cd <nome-della-cartella>
   ```

2. **Avvia il server**:
   ```bash
   python manage.py runserver
   ```

3. **Esplora l'API**
   Apri il browser su http://127.0.0.1:8000/api/ per visualizzare la Landing Page con tutti i link disponibili.

## 🛠️ Cosa ho realizzato in questa sessione (15/01/2026)

**Gestione del Server e Ambiente**
- Ho gestito il server Django direttamente dal terminale di VS Code utilizzando il comando `python manage.py runserver`.
- Ho risolto i problemi di navigazione iniziale tramite comandi Bash, assicurandomi di lanciare i processi dalla "root" del progetto.

**Architettura del Codice (Principio DRY)**
- Ho applicato il principio Don't Repeat Yourself, estraendo la lista `POSTS_DATA` per renderla una costante globale in `views.py`.
- Ho strutturato i dati in modo che ogni modifica alla lista principale venga riflessa in tutte le rotte collegate.

**Routing Dinamico e Parametri**
- Ho creato rotte dinamiche in `urls.py` per catturare variabili dall'URL, come `<str:name>` e `<int:post_id>`.
- Ho sincronizzato i parametri tra gli indirizzi definiti negli URL e gli argomenti delle funzioni nelle Views.

**Sviluppo della Logica di Filtraggio**
- Ho implementato una funzione di ricerca per identificare un singolo post tramite il confronto degli ID.
- Ho realizzato un sistema di filtro (user_posts) per visualizzare i contenuti associati a uno specifico userId.

**Esperienza Utente e Documentazione**
- Ho costruito una Landing Page JSON (`api_index`) che elenca tutti gli endpoint disponibili sul server.
- Ho gestito le risposte di errore, impostando messaggi personalizzati e lo stato HTTP 404.
