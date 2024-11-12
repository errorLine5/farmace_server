
import sqlite3
import shortuuid


class ImageBucket:
    def __init__(self):
        self.db = sqlite3.connect('image_bucket.db')
        self.db.execute('CREATE TABLE IF NOT EXISTS images (id TEXT PRIMARY KEY, data BLOB)')

    def add_image(self, image_id: str, image_data: bytes):
        url_generator = shortuuid.ShortUUID()

        url = url_generator.random(length=10) + '_' + url_generator.random(length=10)
        #check if data already exists if it does return the url
        test_id = self.db.execute('SELECT id FROM images WHERE data = ?', (image_data,)).fetchone()
        if test_id is not None:
            return test_id[0]


        self.db.execute('INSERT INTO images (id, data) VALUES (?, ?)', (url, image_data))
        self.db.commit()
        return url

    def get_image(self, url: str):
        return self.db.execute('SELECT data FROM images WHERE id = ?', (url,)).fetchone()[0]

    def delete_image(self, url: str):
        self.db.execute('DELETE FROM images WHERE id = ?', (url,))
        self.db.commit()

    def close(self):
        self.db.close()
