
# coding: utf-8

# In[1]:

class_ntust = {
    "member1" : "⽢道夫",
    "member2" : "亞拉岡",
    "member3" : "索倫",
    
}


# In[2]:

class_ntust["member1"] = "雅文"


# In[3]:

class_ntust


# In[4]:

class_ntust2={
    "member4" : "⾦鋼狼",
    "member5" : "暴風女",
    "member6" : "X教授",

}


# In[5]:

class_ntust.update(class_ntust2)


# In[6]:

class_ntust


# In[7]:

drinks = {
"item1" : {"珍珠奶茶","紅茶"},
"item2" : {"烏龍奶茶","烏龍茶"},
"item3" : {"蜂蜜紅茶","紅茶"},
}


# In[8]:

type(drinks)


# In[9]:

x = drinks["item1"]
type(x)


# In[10]:

x


# In[11]:

for name,contents in drinks.items():
    if "紅茶" in contents:
        print(name)


# <big><big><big><big><big>作業1<big><big><big><big><big>

# In[67]:

##錯的重寫! 2018/03/19 11:26
a = "222446688137"
number_counts = {number:a.count(number) for number in a}
print(number_counts)
for key,value in number_counts.items():
    if value > 1:
        print(key,":",value,"個","true")


# <big><big><big><big><big>作業<big><big><big><big><big>

# In[45]:


iron_man_color = input("請輸入顏色")
if iron_man_color == "紅色":
    print("鋼鐵⼈盔甲是紅⾊的")
elif iron_man_color == "綠色":
    print("鋼鐵⼈其實也可以參考浩克的顏⾊")
elif iron_man_color == "藍色":
    print("鋼鐵⼈變成藍⾊⼩精靈也不錯")
else:
    print("沒有",iron_man_color)




# <big><big><big><big><big>作業2<big><big><big><big><big>

# In[14]:

lucky_number = "8"
while True:
    number = input("猜數字:")
    if number == lucky_number:
        print("bingo")
        break
    elif number > lucky_number:
        print("太大了")
    elif number < lucky_number:
        print("太小了")
    else:
        print("加油好嗎?")
    


# <big><big><big><big><big>作業3<big><big><big><big><big>

# In[49]:

#印出99乘法表
###要把x做成[1~10]list
for x in range(1,10):
    for y in range(1,10):
        print(x,"*",y,"=",x*y)


# <big><big><big><big><big>作業4<big><big><big><big><big>

# In[16]:

a_list = []
for number in range(1,6):
    if number %2 ==1:
        a_list.append(number)
a_list


# <big><big><big><big><big>作業5<big><big><big><big><big>

# In[53]:

#用生成式寫99乘法表
rows = range(1,10)
cols = range(1,10)
for row in rows:
    for col in cols:
        print(row,"*",col,"=",row*col)


# In[ ]:




# <big><big><big><big><big>作業6<big><big><big><big><big>

# In[50]:

def ironman_color(x):
    x = input("顏色:")
    if x == "紅色":
        return "bingo"
    elif x == "綠色":
        return "綠綠的"
    elif x == "藍色":
        return "藍藍的"
    else:
        return("沒這種色")
        
ironman_color("x")


# In[ ]:




# <big><big><big><big><big>作業7<big><big><big><big><big>

# In[63]:

def run_with_positional_args(func,*args):
    return func(*args)
def sum_args(*args):
    return sum(args)
run_with_positional_args(sum_args,1,2,3,4)


# In[ ]:

##用含式寫計算機
def calculator(func,*args):
    return func(*args)
#def calculator1(*args):
    


# In[72]:

##用含式寫計算機簡單版
##寫不出來2018/3/25
def calcu(x,y,z):
    x= 0
    z= 0
    x == input("數字")
    y == input("符號")
    z == input("數字")
    if y == "+" :
        return sum(x,z)
    elif y == "-" :
        return x-z
    elif y == "*" :
        return x*z
    elif y == "/":
        return x/z
def calcu(2,"*",1)


# In[ ]:




# In[ ]:



