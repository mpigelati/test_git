import subprocess
import json
print("hellow world")
gitlog= "git log > git_log.txt"
subprocess.call(gitlog,shell=True)

def Fun_json(my_list):
    print("mylist",my_list)
    global count
    #print("my_list_len",len(my_list))
    my_json = {}
    my_json = []

    my_json.append(
          {
               'Commit':my_list[0].split(" ")[1].rstrip("\n"),
               'Auther':my_list[1].split(":")[1].rstrip("\n"),
               'Date': my_list[2].split(":")[1].rstrip("\n"),
               'Dev_Comment': my_list[3].lstrip(" ")
            }
        )
    with open("data.json", 'W')as fd:
        #print(fd)
        json.dump(data,fd,indent=4)

with open('git_log.txt','r') as fd:
    print(fd)
    data =fd.readlines()
    size=len(data)-1
    #print("size",size)
    t_list=[]

for i, line in enumerate(data):
    if("commit" in line and size != i):
        for j in range(i,i+5):
            if(data[j] != "\n"):
                t_list.append(data[j])
        Fun_json(t_list)
        #print(t_list)
        t_list.clear()
