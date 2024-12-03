@echo off
rmdir dis S/ Q/
py -m build
py -m twine upload --repository pypi dist/*

@REM py -m pip install --upgrade build  untuk pertama
@REM py -m pip install --upgrade twine untuk pertama

