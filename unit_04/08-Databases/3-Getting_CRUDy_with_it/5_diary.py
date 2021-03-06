#
#  Using Databases in Python: Gettin' CRUD-y With It 
#  Python Techdegree
#
#  Created by Dulio Denis on 1/5/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
#  And, like anything else we do, eventually we're
#  going to write an entry that we just don't like
#  or need and we'll want to get rid of it. Let's
#  use Peewee to remove records from the database.
# ------------------------------------------------
#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import sys

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now) 

    class Meta:
        database = db
    
def initialize():
    '''Create the database and the table if they don't exist.'''
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    '''Add an entry.'''
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()

def add_entry():
    '''Add an entry.'''
    print("Enter your entry. Press 'cntl-d' when finished." )
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Yn]').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully.")

def view_entries(search_query=None):
    '''View previous entries.'''
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('N) for next entry')
        print('d) delete entry')
        print('q) to return to the main menu')

        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    '''Search entries for a string.'''
    view_entries(input('Search query: '))
        
def delete_entry(entry):
    '''Delete an entry.'''
    if input('Are you sure? [yN] ').lower() == 'y':
        entry.delete_instance()
        print('Entry deleted.')

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])

if __name__ == "__main__":
    initialize()
    menu_loop()
 