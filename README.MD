# Simple routine to show manipulation of Google sheets

## To run

1. Install homebrew (https://brew.sh/)
2. Install python3 (and pip3 automatically) `brew install python3` (https://stackoverflow.com/a/47004414)
3. Install virtualenv `pip3 install virtualenv`
4. Create App on Google Developers console (https://cloud.google.com/appengine/docs/standard/python/console#console)
5. Add Google Sheets API & Google Drive API to app (https://docs.gspread.org/en/latest/oauth2.html#enable-api-access)
6. Create and download OAuth2 credentials json file (https://docs.gspread.org/en/latest/oauth2.html#oauth-client-id)
7. Save as `credentials.json` in root folder
8. `virtualenv .env && source .env/bin/activate && pip install -r requirements.txt`
9. Set params
10. `python3 main.py`
