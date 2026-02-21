# Scrappy
Un scrapper qui enregistre en format CSV.

# Minimum requis

Il faut avoir python d'installé.

## Lib utilisé à installer

(Il est conseillé d'utiliser un docker ou env pour pouvoir executer)

### Pour créer un env

``` bash
python3 -m venv venv
```

``` bash
pip install requests
```
``` bash
pip install beautifulsoup4
```
``` bash
pip install pandas
```

# Pour executer

```bash
python3 main.py [URL] [NAME_OUTPUT]
```
URL étant l'url du site que vous voulez examiner et tirer les informations.
NAME_OUTPUT est le nom du fichier en .csv qui sera créé dans le dossier data.