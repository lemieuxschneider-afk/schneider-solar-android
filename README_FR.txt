SCHNEIDER SOLAR — Projet Android hors ligne
=============================================

FICHIERS
- main.py : application Kivy en français, calculs locaux hors ligne
- buildozer.spec : configuration Android
- .github/workflows/android.yml : configuration pour compiler l'APK sur GitHub Actions

ÉTAPES SUR TÉLÉPHONE SEULEMENT
1. Télécharge et décompresse ce ZIP avec le gestionnaire de fichiers Android.
2. Ouvre https://github.com et crée un compte ou connecte-toi.
3. Crée un dépôt NOUVEAU nommé schneider-solar-android.
   Pour un débutant, choisis Public pour éviter les limites de minutes Actions
   applicables aux dépôts privés gratuits. Le code déposé sera alors public :
   ne mets aucun mot de passe, clé privée, adresse personnelle ou donnée secrète.
4. Dans le dépôt, utilise Add file > Upload files pour envoyer main.py et
   buildozer.spec depuis le dossier décompressé, puis Commit changes.
5. Pour créer le workflow, choisis Add file > Create new file. Dans le nom du
   fichier, saisis exactement .github/workflows/android.yml
   Colle le contenu du fichier android.yml de ce ZIP et valide avec Commit changes.
   Si tu peux sélectionner le fichier du ZIP directement dans le sélecteur GitHub,
   tu peux aussi utiliser Upload files, mais les dossiers cachés ne sont pas toujours visibles.
6. Ouvre l'onglet Actions du dépôt. Le workflow « Construire APK SCHNEIDER SOLAR »
   démarre après le commit. La première compilation peut prendre plusieurs minutes.
7. Ouvre le dernier exécution (run) terminée avec succès, puis cherche la section
   Artifacts et télécharge SCHNEIDER-SOLAR-APK. Décompresse le téléchargement si nécessaire.
8. Appuie sur le fichier .apk depuis le gestionnaire de fichiers pour l'installer.
   Android peut demander d'autoriser l'installation depuis cette source.

Liens utiles
- GitHub : https://github.com
- Documentation Kivy Android : https://kivy.org/doc/stable/guide/packaging-android.html
- Buildozer Action : https://github.com/ArtemSBulgakov/buildozer-action

IMPORTANT
Ce ZIP contient le code source, pas encore un APK compilé.
La compilation nécessite Internet; une fois installée, l'application réalise ses calculs hors ligne.
Les résultats sont des estimations techniques, pas un plan électrique certifié.
Vérifie les caractéristiques réelles des panneaux, batteries, onduleur et MPPT ainsi que les
protections, sections de câbles et la mise à la terre avant toute installation.
