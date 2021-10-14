#{"script":"","code":""" """}
data={
0:[
    {"script":"","code":""" """}]
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