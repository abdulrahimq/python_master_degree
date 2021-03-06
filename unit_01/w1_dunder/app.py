#
#  dunder main app
#  Python Techdegree
#
#  Created by Dulio Denis on 12/4/18.
#  Copyright (c) 2018 ddApps. All rights reserved.
# ------------------------------------------------
#  We can utilize a conditional check to verify if our script is being run directly or being imported. 
#  Then we can handle those conditions differently based on our needs.
#
def print_hello():
    print("Hello, from first App!")

print(__name__)

if __name__ == '__main__':
    print_hello()
