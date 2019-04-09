import os
from pymongo import MongoClient

COLLECTION_NAME = 'waves'

class MongoRepository(object):
    def __init__(self):
        mongo_url = os.environ.get('MONGO_URL')
        self.db = MongoClient(mongo_url).waves

    def find_all(self, selector):
        return self.db.waves.find(selector)
    
    def find(self, selector):
        return self.db.waves.find_one(selector)

    def create(self, wave):
        return self.db.waves.insert_one(wave)
    
    def update(self, selector, wave):
        return self.db.waves.replace_one(selector, wave).modified_count

    def delete(self, selector):
        return self.db.waves.delete_one(selector).deleted_count

        