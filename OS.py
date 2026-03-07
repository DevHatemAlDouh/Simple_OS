import os

import shutil

import os.path


# Create Folder.....
def mkdir(mackDir):
    if not os.path.exists(mackDir):
        os.mkdir(mackDir)
        print(f"mkdir: Create direct could: {mackDir}")
    else:
        print(f"{mackDir} is already created")


# Remove Folder....
def rmdir(removeDir):
    try:
        if os.path.exists(removeDir):
            if os.path.isdir(removeDir):
                os.rmdir(removeDir)
                print(f"rmdir: Deleted direct could: {removeDir}")
            else:
                print(f"{removeDir} is not directory")
        else:
            print(f"{removeDir} not founded")
    except OSError:
        print(f"{removeDir} is not empty")


# lise all items
def ls(directory='.'):
    if os.path.exists(directory):
        if os.path.isdir(directory):
            own = 0
            for filename in os.listdir(directory):
                if os.path.isdir(filename):
                    own += 1
                    print(f".{filename}", end="    ")
                else:
                    own += 1
                    print(f"{filename}", end="    ")
            return cowls(own)
        else:
            print(f"{directory} is not directory")
    else:
        print(f"{directory} not fawned ")
        return cowls(0)


def cowls(own):
    return own


# enter File
def cd(File_name):
    if os.path.exists(File_name):
        os.chdir(File_name)
    else:
        print(f"{File_name} not founded")


# exit File
def cd__():
    os.chdir("..")


# Home File
def cd_Home():
    os.chdir("/")


def Format(form):
    if form in ["txt", "docx", "pptx", "pdf", "xlsx"]:
        return "T"
    else:
        return "F"


# cat
def cat(File_name):
    if File_name == ">" or File_name == ">>":
        pass
    elif os.path.exists(File_name):
        if os.path.isfile(File_name):
            fromars = []
            for j in range(len(File_name)):
                if File_name[-1 - j] != ".":
                    fromars.insert(0, File_name[-1 - j])
                else:
                    break
            if Format("".join(fromars)) == "T":
                with open(File_name, "r") as f:
                    print(f.read())
                    f.close()
            else:
                print(f"{File_name} format is not valued")
        else:
            print(f"{File_name} is not file")
    else:
        print(f"{File_name} not fawned")


def cat_(File_name):
    if File_name == ">":
        pass
    elif os.path.exists(File_name):
        if os.path.isfile(File_name):
            fromars = []
            for j in range(len(File_name)):
                if File_name[- 1 - j] != ".":
                    fromars.insert(0, File_name[- 1 - j])
                else:
                    break
            if Format("".join(fromars)) == "T":
                os.remove(File_name)
                with open(File_name, "w") as f:
                    writes = []
                    while True:
                        write = input()
                        if write != "stop":
                            writes.append(write)
                        else:
                            f.write("\n".join(writes))
                            f.close()
                            break
            else:
                print(f"{File_name} format is not valued")
        else:
            print(f"{File_name} is not file")

    elif not os.path.exists(File_name):
        fromars = []
        for j in range(len(File_name)):
            if File_name[-1 - j] != ".":
                fromars.insert(0, File_name[-1 - j])
            else:
                break
        if Format("".join(fromars)) == "T":
            with open(File_name, "w") as f:
                writes = []
                while True:
                    write = input()
                    if write != "stop":
                        writes.append(write)
                    else:
                        f.write("\n".join(writes))
                        f.close()
                        break
        else:
            print(f"{File_name} format is not valued")
    else:
        print(f"{File_name} not founded")


def cat__(File_name):
    if File_name == ">>":
        pass
    elif os.path.exists(File_name):
        if os.path.isfile(File_name):
            for j in range(len(File_name)):
                if File_name[-4] + File_name[-3] + File_name[-2] + File_name[-1] != ".pdf":
                    fromars = []
                    for k in range(len(File_name)):
                        if File_name[-1 - k] != ".":
                            fromars.insert(0, File_name[-1 - k])
                        else:
                            break
                    if Format("".join(fromars)) == "T":
                        with open(File_name, "a") as f:
                            writes = []
                            while True:
                                write = input()
                                if write != "stop":
                                    writes.append(write)
                                else:
                                    f.write("\n".join(writes))
                                    f.close()
                                    break
                    else:
                        print(f"{File_name} format is not valued")
                        break
                else:
                    print(f"{File_name} is a pdf and you can't edit in pdf")
                    break
        else:
            print(f"{File_name} is not file")
    else:
        print(f"{File_name} not founded")


# remove File
def rm(File_name):
    if os.path.exists(File_name):
        if os.path.isfile(File_name):
            os.remove(File_name)
            print(f"rm: {File_name} have ben deleted")
        else:
            print(f"{File_name} is not file")
    else:
        print(f"{File_name}  not founded")


# copy Folder....
def cp(shack, file, src, dst):
    if os.path.exists(src):
        if os.path.exists(shack):
            shutil.copy2(src, dst)
            print(f"cp: This file {file} had ben coped from  {src} to {dst}")
        else:
            print(f"{shack} not founded")
    else:
        print(f"{src} not founded")


# move Folder
def mv(shack, file, src, dst):
        if os.path.exists(src):
            if os.path.exists(shack):
                shutil.copy2(src, dst)
                print(f"mv: This file {file} had ben moved from  {src} to {dst}")
                os.remove(file)
            else:
                print(f"{shack} not founded")
        else:
            print(f"{src} not founded")


# Display the current path....
def pwd():
    return os.getcwd()


os.chdir('D:')


def Getcwdu(get):
    Get_info = ""

    Get = str(get)
    for portent_in_Get in range(len(Get)):
        if portent_in_Get > 1:
            Get_info = Get_info + Get[portent_in_Get]
    if Get_info == os.sep:
        print("~$", end="")
    else:
        print(f"~{Get_info}$", end="")


cmd = ["cd", "ls", "pwd", "cp", "mv", "rm", "mkdir", "rmdir", "cat"]


def run(u_inp):
    if u_inp[0] in cmd:
        if u_inp[0] == "pwd":
            try:
                if u_inp[1] is None:
                    pass
            except IndexError:
                print(pwd())
        elif u_inp[0] == "cp" or u_inp[0] == "mv":
            len2 = (len(u_inp) - 1) // 2
            for items in range(len2):
                if u_inp[0] == "mv":
                    src = pwd() + u_inp[1 + items * 2]
                    shack = pwd() + u_inp[2 + items * 2]
                    dst = pwd() + u_inp[2 + items * 2] + '\\' + u_inp[1 + items * 2]
                    file = u_inp[1 + items * 2]
                    mv(shack, file, src, dst)

                elif u_inp[0] == "cp":
                    src = pwd() + u_inp[1 + items * 2]
                    shack = pwd() + u_inp[2 + items * 2]
                    dst = pwd() + u_inp[2 + items * 2] + '\\' + u_inp[1 + items * 2]
                    file = u_inp[2 + items * 2]
                    cp(shack, file, src, dst)

        else:
            for items in range(len(u_inp) - 1):
                if u_inp[0] == "mkdir":
                    mkdir(u_inp[1 + items])

                elif u_inp[0] == "rmdir":
                    rmdir(u_inp[1 + items])

                elif u_inp[0] == "rm":
                    rm(u_inp[1])

                elif u_inp[0] == "ls":
                    if u_inp[1] == "..":
                        print(User_Name)
                    elif u_inp[1] == " ":
                        con = cowls(ls())
                        if con != 0:
                            print()
                    else:
                        con = cowls(ls(u_inp[1]))
                        if con != 0:
                            print()

                elif u_inp[0] == "cd":
                    if u_inp[1] == "..":
                        cd__()
                    elif u_inp[1] == "~" or u_inp[1] == "--" or u_inp[1] == " ":
                        cd_Home()
                    else:
                        cd(u_inp[1])

                elif u_inp[0] == "cat":
                    if u_inp[1 + items] == ">" or u_inp[1 + items] == ">>":
                        if u_inp[1] == ">" or u_inp[1] == ">>":
                            if u_inp[1] == ">":
                                cat_(u_inp[2])
                            else:
                                cat__(u_inp[2])
                    else:
                        cat(u_inp[1])

    elif u_inp[0] == " ":
        pass
    else:
        print("Command is not valued")


User_Name = input("Enter Your Name: ")
while True:
    print(f"{User_Name}@{os.__name__}:", end="")
    Getcwdu(os.getcwd())
    User_input = input()
    user_after_edit = []
    user_split = User_input.split(" ")
    for i in user_split:
        if i != "":
            user_after_edit.append(i)
    if user_after_edit == ["ls"] or user_after_edit == ["cd"] or user_after_edit == []:
        user_after_edit += " "

    run(user_after_edit)
