from dataclasses import dataclass

@dataclass
class Items:
    id: int
    name: str
    category: str
    price: float
    quantity: int
    pharmacy_id: int

    @staticmethod
    def makeTableSqlite():
        return """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            pharmacy_id INTEGER NOT NULL,
            FOREIGN KEY (pharmacy_id) REFERENCES pharmacy (id)
        );
        """
