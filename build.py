from zipfile import ZipFile
from contextlib import suppress
import os

chrome_files = ['manifest-chrome.json', 'background.js', 'icons/icon16.png', 'icons/icon48.png', 'icons/icon128.png']
ff_files = ['manifest-firefox.json', 'background.js', 'icons/icon.svg']

with suppress(FileExistsError):
    os.mkdir('builds')


def package(files, variation):
    with ZipFile(f'builds/Questrade Real Time Quote - {variation}.zip', 'w') as zf:
        for file in files:
            try:
                if file.count('manifest'):
                    zf.write(file, 'manifest.json')
                else:
                    zf.write(file)
            except FileNotFoundError:
                print(f'ERROR: FileNotFoundError(file)')


package(chrome_files, 'Chrome')
package(ff_files, 'Firefox')
print('Built Zips')