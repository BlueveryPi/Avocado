import os
import argparse

parser=argparse.ArgumentParser(description="Process Avocado.")

parser.add_argument("file", type=str, help="Code file to process.")

args=parser.parse_args()
path=args.file

if not os.path.exists(path):
    raise TypeError("Inappropriate argument type")
elif not os.path.isfile(path):
    raise TypeError("Argument is not a file")
else:
    if not path.endswith(".avo"):
        raise TypeError("Inappropriate file type")
    else:
        with open(path, "r+", encoding="utf-8") as f:
            code=f.read().replace("\n", "")
            code=[char for char in code]
            memory=[]
            for i in range(32768):
                memory.append(0)
            pointer=0
            
            for i, command in enumerate(code):
                if command=="아":
                    if pointer<32768:
                        pointer+=1
                    else:
                        raise OverflowError("Pointer too large")

                elif command=="보":
                    if pointer>0:
                        pointer-=1
                    else:
                        raise OverflowError("Pointer too small")

                elif command=="카":
                    memory[pointer]+=1

                elif command=="도":
                    memory[pointer]-=1

                elif command=="쑥":
                    if code[i+1]!="쑥":
                        raise SyntaxError(f"Unmatched '쑥' in {i}")
                    else:
                        code.pop(i+1)
                        if type(memory[pointer])==int:
                            memory[pointer]=float(memory[pointer])
                        else:
                            memory[pointer]=int(memory[pointer])

                elif command=="!":
                    if type(memory[pointer])==float:
                        print(chr(int(memory[pointer])), end="")
                    else:
                        print(int(memory[pointer]), end="")
                else:
                    raise SyntaxError(f"Invalid syntax in {i}")