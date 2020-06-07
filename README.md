# vconv

---

Programma per convertiere i video mkv in mp4.

### Requirements

ffmpeg

## Usage

Il programma prevede i seguenti parametri:

parametro | significato
--- | ---
--help | Restituisce il messaggio di help
--version | Restituisce la versione del programma
--verbose | Output verboso con le informazioni sulla conversione in corso.
--quiet | Non restituisce alcun output sul terminale.
--file FILE | Specifica il percorso del file mkv da convertire
--dir DIR | Specifica il percorso di una cartella contenente i file mkv
--out | Specifica una sottocartella del percorso indicato in cui verranno inseriti i file convertiti
--test | Se presente imposta la conversione solo per i primi 30 secondi di video.

Per ulteriori informazioni digitare:

    $ vconv -h

## Changelog

**2020-04-11 02_01**

Aggiunti i Flags --quiet, --verbose e --test.
Risolto bug per cui il programma crashava se il file esisteva
già nella cartella di destinazione

**2020-04-11 01_01**

Prima versione

## Author

Leonardo Vicentini