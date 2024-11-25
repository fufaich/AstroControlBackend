class DatabaseConfig:
    port = 5432
    dbhost = "localhost"
    dbpassword = "Virus367"
    dbuser = "postgres"
    dbname = "aero_managment"

    def __init__(self, dbname, dbuser, dbpassword, dbhost, port):
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbhost = dbhost
        self.port = port

    @classmethod
    def as_dict(cls):
        """Возвращает конфигурацию в виде словаря."""
        return {
            'dbname': cls.dbname,
            'user': cls.dbuser,
            'password': cls.dbpassword,
            'host': cls.dbhost,
            'port': cls.port
        }

    @classmethod
    def get_config(cls):
        """Возвращает объект DatabaseConfig с текущими атрибутами."""
        return cls(
            dbname=cls.dbname,
            dbuser=cls.dbuser,
            dbpassword=cls.dbpassword,
            dbhost=cls.dbhost,
            port=cls.port
        )