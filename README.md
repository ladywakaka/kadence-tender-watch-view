# KADENCE Tender Watch – shared view

Password-protected copy of the full KADENCE Tender Watch dashboard (fit scores, 5-year past awards, filters, go/no-go), published with GitHub Pages.
The page source is stored only encrypted (`src/snapshot.html.enc`); the workflow decrypts it and locks the page with StatiCrypt.

Data is a snapshot of the Claude dashboard's database. Go/no-go changes on this page are saved only in each viewer's browser.

To update: export the `tenders` and `runs` collections from the Claude artifact to `<db_dir>`, then
`python3 scripts/build_view.py ../kadence-tender-watch/dashboard/kadence-tender-watch.html <db_dir> /tmp/view.html`,
`scripts/encrypt.sh /tmp/view.html`, commit and push.
