import os

import fileFactory


if __name__ == "__main__":
    os.chdir("./examples")

    fileFactory.bake("blueprint.txt", "merged.tscript");    

    try:
        os.makedirs("./unmerged")
    except FileExistsError: pass
    os.chdir("./unmerged")

    fileFactory.unbake("../merged.tscript", "blueprint.txt")

    os.chdir("./../..")

