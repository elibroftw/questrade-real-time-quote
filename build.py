from zipfile import ZipFile

# src_files = ['manifest.json', 'background.js', 'icons/icon48.png', 'icons/icon96.png']
src_files = ['manifest.json', 'background.js', 'icons/icon.svg']
with ZipFile('Questrade Real Time Quote.zip', 'w') as zf:
    for file in src_files:
        try:
            zf.write(file)
        except FileNotFoundError:
            print('FileNotFoundError:', file)

print('Built Zip')