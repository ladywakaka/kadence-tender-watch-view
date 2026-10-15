# KADENCE Tender Watch – shared view

Password-protected, read-only snapshot of the KADENCE Tender Watch board, published with GitHub Pages.
The page source is stored only encrypted (`src/snapshot.html.enc`); the workflow decrypts it and locks the page with StatiCrypt.

To update: rebuild `tender-snapshot.html` with `build.py` in the private `kadence-tender-watch` repo, run
`scripts/encrypt.sh tender-snapshot.html`, commit and push.
