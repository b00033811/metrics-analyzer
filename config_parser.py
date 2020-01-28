import yaml
from io_handler import load_config
with load_config('config.yaml') as (f, err):
    if err:
        print(err)
    else:
        conf=yaml.safe_load(f)
        print(conf)