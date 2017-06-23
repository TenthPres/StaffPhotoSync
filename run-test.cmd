webScrape.py

photoFaceCrop.py

for /r %%f in (cropped\*.jpg) do (
powershell "Set-ADUser %%~nf -Replace @{thumbnailPhoto=([byte[]](Get-Content '%%~ff' -Encoding byte))}"
gam user %%~nf@tenth.org update photo "%%~ff"
)