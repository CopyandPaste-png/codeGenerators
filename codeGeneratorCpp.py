#{"script":"","code":""" """}

data ={
0:[
    {"script":"GUI.h","code":
"""
#pragma once
#include "mainframe.h"

class GUI : public wxApp
{
public:
    GUI();
    virtual bool OnInit();
    int OnExit();

public:
    //Unique ptrs
    std::unique_ptr<mainframe>mframe;
};
"""
    },
    {"script":"GUI.cpp","code":
"""
#include "GUI.h"

IMPLEMENT_APP(GUI)

GUI::GUI() {}

bool GUI::OnInit()
{
    return true;
}

int GUI::OnExit()
{
    return 0;
}
"""
    },
    {"script":"mainframe.h","code":
"""
#pragma once
#include <wx/wx.h>
#include <memory.h>

/*
You need to add the include folder from wxWidgets+ link the wxWidgets library

*/

class mainframe : public wxFrame
{
public:
    mainframe();
    ~mainframe();
};
"""
    },
    {"script":"mainframe.cpp","code":
"""
#include "mainframe.h"

mainframe::mainframe() : wxFrame(nullptr, wxID_ANY, "NAME", wxPoint(30, 30), wxSize(800, 600))
{
}


mainframe:: ~mainframe() {}
"""
    }]
}

def parseChoice(choice:int):
    for i in range(len(data[choice])):

        filename = data[choice][i]["script"]
        code = data[choice][i]["code"].strip()
        #code = code.replace("\n","",1)
        
        with open(filename,"w") as f:
            f.write(code)

        print(f"{filename} writing complete")

def main():
    print("Welcome to code writer")    
    scripts=[
    "wxWidgets init","database-postgresql","database-mySQL"]
    print("What script do you want to build today?")

    [print(f"{scripts.index(i)}:{i}") for i in scripts]
    
    x =int(input("input:"))

    parseChoice(x)

if __name__=="__main__":
    main()

