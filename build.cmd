pip install pyinstaller

rmdir /s /q dist\webScrape
pyinstaller --onedir webScrape.py

rmdir /s /q dist\photoFaceCrop
pyinstaller --onedir photoFaceCrop.py

copy haarcascade_frontalface_default.xml dist\haarcascade_frontalface_default.xml

copy run-prod.cmd dist\run.cmd