import tomllib

def load_toml_files(file_path: str, extract_key: str = ''):
    assert file_path.split(".")[-1] == "toml", "File should be toml of extension `.toml`"
    with open(file_path, 'rb') as file_obj:
        config = tomllib.load(file_obj)

    return config if not extract_key else config[extract_key]