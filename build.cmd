pip install pyinstaller

rm .\StaffPhotos.zip

rmdir /s /q dist
rmdir /s /q build

pyinstaller --onedir webScrape.py

pyinstaller --onedir photoFaceCrop.py

copy haarcascade_frontalface_default.xml dist\haarcascade_frontalface_default.xml

copy run-prod.cmd dist\run.cmd


PowerShell -Command "Compress-Archive -Path .\dist\* -DestinationPath StaffPhotos.zip"