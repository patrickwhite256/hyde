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

##The Django interface

Now featuring a super basic web interface in Django! Should it have been using Flask? Absolutely. Did I know about Flask before I was 80% done the Django part? No.
It's pretty hideous, I'd welcome anyone who wants to make it prettier. I don't really mind it, so there's that.

Running the Django server:

(within the `hyde_django` directory)

```
./manage.py runserver
```

You should be able to visit it at http://localhost:8000 after that.
DON'T open it to a public port, or host it anywhere, because there's some pretty serious security flaws at the moment. It's only for curiousity purposes right now.

## Possibly planned features
* compressing files before storing them
* support for more than just pngs
* ~~web interface (maybe through django)~~ a basic version of this is working
* storing multiple files
* storing across multiple images
