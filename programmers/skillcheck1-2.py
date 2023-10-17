#아이디 

def solution(new_id):
    new_id = new_id.lower()
    for i in new_id:
        if i not in ["-","_","."] and i.isalnum()==False:
            new_id=new_id.replace(i,"")
    while ".." in new_id:
        new_id=new_id.replace("..",".")
    new_id=new_id.strip(".")

    if new_id=="":
        new_id+="a"

    if len(new_id)>=16:
        new_id=new_id[:15]
    if new_id[-1]==".":
        new_id=new_id.rstrip(".")

    if len(new_id)<=3:
        new_id=new_id+new_id[-1]*(3-len(new_id))

    return new_id