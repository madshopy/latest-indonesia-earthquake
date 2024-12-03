@echo off
rm dir dis s/ q/

@REM py -m pip install --upgrade build  untuk pertama
py -m build
@REM py -m pip install --upgrade twine untuk pertama
py -m twine upload --repository pypi dist/*