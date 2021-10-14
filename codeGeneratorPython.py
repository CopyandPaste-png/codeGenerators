#{"script":"","code":""" """}

data ={
0:[{"script":"webscrap.py","code":
"""
import requests
from bs4 import BeautifulSoup

def parseWebsite(requestedWebsite:str):
    website = requests.get("")
    website_content = BeautifulSoup(website.content,"html.parser")

    first = website_content.find("div",{"class"=""})

    for i in first.findAll("ul",{"class"=""}):
        pass

def main():
    pass

if __name__=="__main__":
    main()
"""
    },
    {"script":"requirements.txt","code":
"""
bs4
requests
"""
    }],
1:"",
2:[{"script":"postgreSQL.py","code":
"""
import psycopg2
from config import config

def connect():
    conn=None
    try:
        params= config()
        print("Connecting...")

        conn=psycopg2.connect(**params)

        cur = conn.cursor()

        print("Version:")
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()
                print("Connection closed")

def selectAll(tablename):
    conn=None
    try:
        params= config()
        print("Connecting...")

        conn=psycopg2.connect(**params)

        cur = conn.cursor()

        query = "SELECT * FROM"
        query += tablename

        cur.execute(query)

        db_version = cur.fetchall()
        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
                conn.close()
                print("Connection closed")

if __name__=="__main__":
    pass 
"""
    },
    {"script":"config.py", "code":
"""
from configparser import ConfigParser

def config(filename="database.ini",section="postgresql"):
    parser= ConfigParser()
    parser.read(filename)

    db={}

    if parser.has_section(section):
        params= parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename}")

    return db
"""
    },
    {"script":"database.ini", "code":"""
[postgresql]
host=localhost
database=
user=
password=
"""
    },
    {"script":"requirements.txt","code":"""
psycopg2
"""
    }],
3:"",
4:"",



}

def parseChoice(choice:int):
    for i in range(len(data[choice])):

        filename = data[choice][i]["script"]
        code = data[choice][i]["code"].replace("\n","",1)

        with open(filename,"w") as f:
            f.write(code)

        print(f"{filename} writing complete")


def main():
    print("Welcome to code writer")    
    scripts=[
    "webscrap-bs4-basic","webscrap-selenium","database-postgresql","database-mySQL"]
    print("What script do you want to build today?")

    [print(f"{scripts.index(i)}:{i}") for i in scripts]
    
    x =int(input("input:"))

    parseChoice(x)

if __name__=="__main__":
    main()