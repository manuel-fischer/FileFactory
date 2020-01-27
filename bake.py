import sys
import fileFactory

if __name__ == "__main__":
    argv = sys.argv[:3] + ["-", "-"]
    fileFactory.bake(argv[1], argv[2])
