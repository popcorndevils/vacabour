import pathlib

DATA_DIRECTORY = pathlib.Path("./vocab_data/")
DATA_FILE = "data.vc"  
DATA_FULL_PATH = DATA_DIRECTORY.joinpath(f"./{DATA_FILE}")
