#!/usr/bin/python

__author__ = 'Mariano Andres Di Maggio'

import os
import sys
import pymongo

from builtins import print
from pymongo import MongoClient


def main():
    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-  Starting Program  |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|- \n')

    # Conectando con MongoDB
    dbmclient = MongoClient('192.168.0.213', 31793)

    dbdatabase = dbmclient.website
    users = dbdatabase.users

    user1 = {'mariano_dim' : 'user123'}
    user1_id = users.insert_one(user1).inserted_id
    print(user1_id)

# Llamada a la funcion de arranque
if __name__ == '__main__':
    main()
