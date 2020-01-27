import sys
import fileFactory

if __name__ == "__main__":
    argv = sys.argv[:3] + ["-", "-"]
    fileFactory.unbake(argv[1], argv[2])
