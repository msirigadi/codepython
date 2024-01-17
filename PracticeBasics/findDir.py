import os
"""
os.makedirs("tree/c/other_courses/cpp")
os.makedirs("tree/c/other_courses/python")
os.makedirs("tree/cpp/other_courses/c")
os.makedirs("tree/cpp/other_courses/python")
os.makedirs("tree/python/other_courses/c")
os.makedirs("tree/python/other_courses/cpp")
"""
os.chdir("tree")


class Find:
    def __init__(self):
        self.__pathlist = []

    def find(self, path, dir):
        if len(os.listdir()) == 0:
            return
        print(os.listdir())
        #prevpath = path
        for subpath in os.listdir():
            if subpath == "python":
                print(os.getcwd())
                #os.chdir(subpath)
                self.__pathlist.append(os.getcwd() + '/' + subpath)
                print(self.__pathlist)
                continue

            #os.chdir(prevpath)
            self.find(prevpath + subpath, dir)


cobj = Find()
cobj.find("./tree", "python")

print(cobj.__pathlist)


