import sys


_stage = 0
pattern0 = '0x00000007 <blob>='
pattern1 = '\"acct\"<blob>='
pattern2 = 'data:'

if __name__ == "__main__":
    file = open(sys.argv[1])
    line = " "
    while line is not "":
        try:
            line = file.readline()
            if _stage == 0:
                if pattern0 in line:
                    print(line.rstrip())
                    _stage = 1
            elif _stage == 1:
                if pattern1 in line:
                    print(line.rstrip())
                    _stage = 2
            elif _stage == 2:
                if pattern2 in line:
                    line = file.readline()
                    print(line.strip())
                    _stage = 0
            else: print("ERROR")

        except Exception:
            sys.exit()

