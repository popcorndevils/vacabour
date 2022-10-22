import pathlib

DATA_DIRECTORY = pathlib.Path("./.vocabourdata/")
GLOSSARY_FILE = "glossary.vc"  
DATA_FULL_PATH = DATA_DIRECTORY.joinpath(f"./{GLOSSARY_FILE}")
