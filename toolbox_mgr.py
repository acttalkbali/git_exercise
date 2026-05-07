toolbox = ["Hammer", "Cutter", "Screwdriver"]

if tool:=input("Tool to be added? "):
    toolbox.append(tool)

while (tool:= input("Tool to remove ? ")) not in toolbox and tool:
    print("I don't have this tool! My toolbox only contains", toolbox)

if tool:
    toolbox.remove(tool)

print("The toolbox now contains ", toolbox)
print("Its third element is", toolbox[2])