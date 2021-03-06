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
                if command=="쑥":
                    if code[i+1]!="쑥":
                        raise SyntaxError(f"Unmatched '쑥' in {i}")
                    else:
                        code.pop(i+1)

            i=-1
            
            while i<len(code)-1:
                i+=1
                command=code[i]
                #print(command)

                if command=="아":
                    if pointer<32768:
                        pointer+=1
                    else:
                        raise OverflowError("Pointer too large / character {i}")

                elif command=="보":
                    if pointer>0:
                        pointer-=1
                    else:
                        raise OverflowError("Pointer too small / character {i}")

                elif command=="카":
                    memory[pointer]+=1

                elif command=="도":
                    memory[pointer]-=1

                elif command=="쑥":
                    if type(memory[pointer])==int:
                        memory[pointer]=float(memory[pointer])
                    else:
                        memory[pointer]=int(memory[pointer])

                elif command=="!":
                    if type(memory[pointer])==float:
                        print(chr(int(memory[pointer])), end="")
                    else:
                        print(int(memory[pointer]), end="")

                elif command=="?":
                    if int(memory[pointer])>len(code)-1:
                        raise IndexError(f"Jump to line {int(memory[pointer])} failed: Index too large / character {i}")
                    elif int(memory[pointer])<0:
                        raise IndexError(f"Jump to line {int(memory[pointer])} failed: Index too small / character {i}")
                    else:
                        i=int(memory[pointer])

                elif command=="오":
                    if memory[pointer-1]<memory[pointer+1]:
                        if i>0:
                            i-=1
                        else:
                            raise IndexError(f"Jump to line {i-1} failed: Index too small / character {i}")

                    elif memory[pointer-1]>memory[pointer+1]:
                        if i<len(code)-1:
                            i+=1
                        else:
                            raise IndexError(f"Jump to line {i+1} failed: Index too large / character {i}")

                else:
                    raise SyntaxError(f"Invalid syntax in {i}")