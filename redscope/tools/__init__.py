import psycopg2
from pathlib import Path
from rsterm.configs import RsTermConfig


def get_redscope_connection() -> psycopg2.connect:
    redscope_config_path = Path(__file__).absolute().parent.parent / "redscope.yml"
    config = RsTermConfig.parse_config(redscope_config_path)
    return config.get_db_connection_('redscope')
