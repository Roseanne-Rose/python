f=open(r"C:\Users\Rose\Desktop\word.txt","r",encoding="UTF-8")
char_list=[]
content=f.read()
for char in content:
    if char.isalpha():
        char_list.append(char)
f.close()
# window_len=7
# count=0
# for i in range(len(char_list)-window_len+1):
#     window=char_list[i:i+7]
#     A="".join(window)
#
#     if (A=="itheima"):
#         count=count+1
count=content.count("itheima")
print(f"一共有：{count}")