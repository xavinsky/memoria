---
title: Récupérer des données via une API
subgroup: Import / export données
type: syntax
---

## Importer requests
Syntaxe: import **requests**
Résultat: -

## Requête GET vers une API REST
Syntaxe: response = requests.**get**(url, params={"key": "value"})
Résultat: objet Response — params est encodé automatiquement en query string dans l'URL

## Vérifier le succès de la requête
Syntaxe: response.**status_code**
Résultat: code HTTP : 2xx succès, 4xx erreur côté client (ex: 404 not found), 5xx erreur côté serveur

## Récupérer le contenu JSON de la réponse
Syntaxe: data = response.**json**()
Résultat: dict ou liste Python — équivalent de json.loads(response.text)

## Paginer une API pour tout récupérer
Syntaxe:
```code
results = []
page = 1
while True:
    page_data = requests.**get**(url, params={"page": page}).json()
    if not page_data:
        break
    results += page_data
    page += 1
df = pd.DataFrame(results)
```
Résultat: boucle jusqu'à recevoir une page vide — beaucoup d'APIs limitent le nombre de résultats par requête et exposent un paramètre page/offset pour tout récupérer
