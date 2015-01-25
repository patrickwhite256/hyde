#hyde

A fun little python project for hiding files in images.

Hiding files example:

```
hyde.py Tricoloring.png secret_message.txt
```

Unhiding files example:

```
jekyll.py Tricoloring-secret.png
```

## Possibly planned features
* compressing files before storing them
* support for more than just pngs
* web interface (maybe through django)
* storing multiple files
* storing across multiple images
