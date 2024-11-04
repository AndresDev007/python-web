cd link_bio
source venv/Scripts/activate
python -m pip install --upgrade pip
python -m install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate