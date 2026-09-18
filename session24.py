"""
    MongDBHelper

    Database contains Collections
    And Collection contains Documents

    Document: Dictionary

    User        : name, phone, email, age, gender etc
    Address     : adrsLine, city, state, pincode

    User Has An Address
    User can have 1 Address
    User can have many Addresses

    1. Referential Technique

    collection1: users
        {
            '_id': 'jahsdg7612364387hashd',
            'name': 'John Watson'
            etc

            'address_id': 'ghfete6213hsag23742'
        }
    
    collection2: addresses
        {
             '_id': 'ghfete6213hsag23742',
             'adrsLine': 'Redwood Shores',
             'city': 'Ludhiana'
             etc

             'user_id': 'jahsdg7612364387hashd'
        }

        Loose Coupling: User and Address are 
        saved differently and they have reference saved inside them

    2. Containerized Technique

        Tightly Coupled
        collection1: users
        {
            '_id': 'jahsdg7612364387hashd',
            'name': 'John Watson'
            etc

            'address': {
                'adrsLine': 'Redwood Shores',
                'city': 'Ludhiana'
                etc
            }
        }

        {
            '_id': 'jahsdg7612364387hashd',
            'name': 'John Watson'
            etc

            'addresses': [
                {
                    'adrsLine': 'Redwood Shores',
                    'city': 'Ludhiana'
                    etc
                },

                {
                    'adrsLine': 'Country Homes',
                    'city': 'Jalandhar'
                    etc
                }
            
            ]
        }

"""

"""
    1. Create Connection with MongoDB Atlas in Cloud
    2. Select the Database and the collection, in which you want to work
    3. Create Write Function (insert, delete, update)
        MongoDB: insert_one(), delete_one(), update_one()
    4. Create Read Function (retrieve/fetch)
        MongoDB: find()

        Their can be a query to delete, update as well find

"""
# Controller for DB Operations

from pymongo.mongo_client import MongoClient
import os

class MongoDBHelper:

    # 1. Create Connection with MongoDB Atlas in Cloud
    def __init__(self):
        # Create a new client and connect to the server
        self.client = MongoClient(os.environ.get("MONGO_URI"))
        print('[MongoDBHelper] Connection Created')

    # 2. Select the Database and the collection, in which you want to work
    def select_db(self, db_name='gw2025', collection='users'):
        self.db = self.client[db_name]
        self.collection = self.db[collection]
        print('[MongoDBHelper] DB {} Collection {} Selected'.format(db_name, collection))

    # 3. Create insert function
    def insert(self, document):
        result = self.collection.insert_one(document)
        #                        insert_many (Can create separate function)
        print('[MongoDBHelper] Document [Inserted] in collection {}'.format(self.collection.name))
        return result
    
    # 4. Create delete function
    def delete(self, query):
        result = self.collection.delete_one(query)
        print('[MongoDBHelper] Document [Delete] from collection {}'.format(self.collection.name))
        return result
    
    # 5. Create update function
    def update(self, query, document):
        result = self.collection.update_one(query, {'$set':document})
        print('[MongoDBHelper] Document [Updated] in collection {}'.format(self.collection.name))
        return result
    
    # 6. Create Read function
    def fetch(self, query=''):
        documents = self.collection.find(query)
        print('[MongoDBHelper] Documents [Fetched] from collection {}'.format(self.collection.name))
        return list(documents)
        
