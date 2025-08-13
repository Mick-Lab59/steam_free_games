\# Steam Free Games – Home Assistant Integration



Cette intégration récupère automatiquement les jeux gratuits disponibles sur \*\*Steam\*\* via l'API de \[gamerpower.com](https://www.gamerpower.com/).



\## Installation



\### Via HACS

1\. Ouvrez HACS → \*\*Intégrations\*\* → Menu → \*\*Custom repositories\*\*.

2\. Ajoutez ce repo avec la catégorie \*\*Integration\*\*.

3\. Installez \*\*Steam Free Games\*\*.

4\. Redémarrez Home Assistant.



\### Manuel

1\. Copier `custom\_components/steam\_free\_games` dans le dossier `custom\_components` de votre configuration Home Assistant.

2\. Redémarrez Home Assistant.



\## Configuration

Ajoutez dans `configuration.yaml` :

```yaml

steam\_free\_games:



