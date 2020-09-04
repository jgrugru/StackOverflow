# def func(x):
#     print("hello from func", x)

# lista = list()
# for i in range(10):
#     a = lambda: func(i)
#     lista.append(a)

# lista[0]()

# fun_list = []

# def retfun(i):
#     print("Inside retfun function. Here is the i value: ", i)
#     def fun(e):
#         print("Here is e[i] value:", e[i])
#         return e[i]
#     return fun


# for i in range(5):
#     fun_list.append(retfun(i))
#     print("Here is the value for fun_list: ", fun_list)

# mylist = range(5)
# print([f(mylist) for f in fun_list])


# fun_list = []
# for i in range(4):
#     def fun(e, _ndx=i):
#         print("Here is the e value inside fun: ", e)
#         print("Here is the _ndx value inside fun: ", _ndx)
#         print("Here is the e[_ndx} value inside fun: ", e[_ndx])
#         return e[_ndx]
#     fun_list.append(fun)

# mylist = [3,214,15,1235] ## this is the list that will be passed to every function inside the fun_list, which will end up holding 4 functions
# print([x(mylist) for x in fun_list])


# def my_own_filter(func, *iterable):
#     l = []
#     if func is None:
#         for i in iterable:
#             if i:
#                 l.append(i)
#     else:
#         print(iterable)
#         for i in iterable:
#             if isinstance(i, int) and isEven(i):
#                 l.append(i)
#             elif isinstance(i, list) or isinstance(i, tuple):
#                 for x in i:
#                     if isEven(x):
#                         l.append(x)    
#     return(l)

# def isEven(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# print(my_own_filter(func, 1, 0, -1, 1, 2, 3, 4))
# print(my_own_filter(isEven, (1, 2, 3), [], [3, 4, 5]))

# s = "Hello World"
# first_word = ''
# for letter in s:
#     if letter != ' ':
#         first_word += letter
#     else:
#         break
# print(first_word)


# import re
# test_string = "/apps/wm/config/test/test"
# test_string1 = "/apps/wm/test/config/test/test"
# print(not bool(re.match("/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)/(\w*)", test_string1)))

# xr = zip(range(0, 5), range(0, 5))
# yr = zip(range(3, 4), range(0, 1))


# rangeList = range(0,10)
# for x in rangeList:
#     print(x)
# print(rangeList)

# print(list(xr), list(yr))
# print(list(xr))

# from pathlib import PureWindowsPath

# fbpy = PureWindowsPath("C:/Users/jeffg/Desktop/ProgrammingProjects/WebScraping/FacebookMP.py")
# print(fbpy)

# from configparser import ConfigParser
# config = ConfigParser()

# config['settings'] = {
#     'debug': 'true',
#     'secret_key': 'abc123',
#     'log_path': '/my_app/log'
# }

# with open('./dev.ini', "w") as f:
#     config.write(f)

# print("asdfa", 3+1)

# import easygui as eg

# print(eg.fileopenbox())

# def test_calc_total():
#     total = mathlib.calc_total(4,5)
#     assert total == 9

# from subprocess import run
# x = run("dir", shell=True, check=True, capture_output=True)
# print(x)

# import re
# lines = "1. some random stuff text and then something completely different \
# 2. some random stuff text and % then something completely different \
# 3. some random % stuff text and then something completely different"
# print(re.findall('\d\. [^\d\.]*', lines))

# from selenium import webdriver 
# from time import sleep 
# from selenium.webdriver.chrome.options import Options
# chrome_path = r"C:\Users\jeffg\Desktop\ProgrammingProjects\WebScraping\chromedriver.exe"

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--disable-notifications')
# prefs = {'profile.default_content_setting_values.notifications': 2}
# chrome_options.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\jeffg\Desktop\WebScraping\chromedriver.exe')

# ChromeOptions options = new ChromeOptions();
# options.addArguments("user-data-dir=/path/to/your/custom/profile");


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_path = r"C:\Users\jeffg\Desktop\ProgrammingProjects\StackOverFlow\chromedriver.exe"
# profile_path = r"C:\Users\jeffg\AppData\Local\Google\Chrome\User Data\Profile 1"
# \ch_options = Options()
# # ch_options.add_argument("--user-data-dir="+profile_path)
# ch_options.add_argument("--user-data-dir=C:/Users/jeffg/AppData/Local/Google/Chrome/User Data")
# ch_options.add_argument("--profile-directory=Profile 1")
# driver = webdriver.Chrome(executable_path=r"C:\Users\jeffg\Desktop\ProgrammingProjects\StackOverFlow\chromedriver.exe", chrome_options=ch_options)
# driver.get("https://www.google.com")

# import pandas as pd

# df = pd.DataFrame(data={'Date':['2020-04-01','2020-05-01','2020-06-01','2020-06-05 '], 'Col2':['195.585770','210.527466','331.500000','331.500000']})
# df['Date'] = pd.to_datetime(df['Date']')
# for index, row in df.iterrows():
#     if not index == 0:
#         print(row['Date'] - df['Date'][index-1])

# import pandas as pd
# df = pd.DataFrame({"ColA":[1,3,"ColA",1],
#                    "ColB":[5,1,"ColB",2],
#                    "ColC":[1,5,"ColC",2]})
# print(df)
# print(df[~df.eq(df.columns).any(1)])

# import pandas as pd
# df = pd.Series([1,3,-5,3,2,5,1])
# max = 5
# min = 0
# runningTotal = 0

# def addToRunningTotal(number, runningTotal):
#     if number + runningTotal > max:
#         runningTotal = max
#     elif number + runningTotal < min:
#         runningTotal = min
#     else:
#         runningTotal+=number
#     print(runningTotal)
#     return runningTotal

# for index, row in df.iteritems():
#     runningTotal = addToRunningTotal(row, runningTotal)


# import os


# def test_something(tmpdir):
#     with tmpdir.as_cwd() as p:
#         print('here', p)
#         print(os.getcwd())


# def main():
#     print("test Module's Name: {}".format(__name__))

# if __name__ == '__main__':
#     print("Run directly")
# else:
#     print("Run from import")

# x = 5
# y = 0
# try:
#     z = x / int(y)
# except ZeroDivisionError as e:
#     print("You can't divide by zero!")
#     z = None
# except TypeError as e:
#     print("You can't divide with a string!")
#     z = None
# print("Division is: ", z)

# list = [{"num":1,"test":"A"},{"num":6,"test":"B"},{"num":5,"test":"c"},{"num":1,"test":"D"}]
# min = 500
# for x in list:
#     if x["num"]<=min or min==None:
#         min=x["num"]
#         print(x)
# print(min)

# import pandas as pd

# df = pd.DataFrame({"a":[1,4],"b":[2,1],"c":[7,9],"d":[1,3]})
# print(df.describe()['a'])

# class Vehicle():
#     def general_usage(self):
#         print("general use: transportation")

# class Car(Vehicle):
#     def __init__(self):
#         print("I am a car.")
#         self.wheels = 4
#         self.has_roof = True

#     def specific_usage(self):
#         print("Specific use: commute, vacation")

# class MotorCycle(Vehicle):
#     def __init__(self):
#         print("I am a motorcycle.")
#         self.wheels = 2
#         self.has_roof = False

#     def specific_usage(self):
#         print("Specific use: road trip, racing")

# c = Car()
# c.general_usage()
# c.specific_usage()

# m = MotorCycle()
# m.general_usage()
# m.specific_usage()

# print(issubclass(MotorCycle,Vehicle))


# class Father():
#     def skills(self):
#         print("I enjoy gardening.")

# class Mother():
#     def skills(self):
#         print("I love cooking")

# class Child(Father,Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("I enjoy sports")

# c = Child()
# c.skills()

# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg=msg
#     def print_exception(self):
#         print("User defined exception: ", self.msg)
#     def handle(self):
#         print("accident occurred. take detour")

# try:
#     raise Accident('car crash between two cars')
# except Accident as e:
#     e.handle()

# def process_file():
#     try:
#         f=open("passlist.txt")
#         x=1/0
#     except FileNotFoundError as e:
#         print("inside except")
#     finally:
#         print("cleaning up file")
#         f.close()
# process_file()

# import os
# import csv
# sentence = ['this stuff', 'is not','that easy']
# with open("test.csv", "w+") as f:
#     f_writer = csv.writer(f)
#     for x in sentence:
#         f_writer.writerow(x)

# sentence = ['this stuff', 'is not','that easy']
# with open('test.csv', 'w') as my_file:
#     f_writer = csv.writer(my_file, delimiter='\n')
#     f_writer.writerow(sentence)

# with open('eggs.csv', 'w', newline='') as csvfile:
#     f_writer = csv.writer(csvfile, delimiter=' ')#,quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     f_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     f_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# import click

# with open("testing.txt", "w+") as f:
#     x = f.read()
# print(x)
# @click.command()
# @click.option('--count', default=5, help='Number of Hello Worlds')
# @click.option('--name', prompt="Your name", default='jeff', help='The person to greet.')
# def hello(count, name):
#     for x in range(count):
#         click.echo('Hello %s' % name)

# if __name__ =='__main__':
#     hello()


# import click
# @click.command()
#basic options
# @click.option('--name', '-n', default='Jeff',help='First name')

#multiple values
# @click.option('--salary', '-s', nargs=2,help="Your monthly salary", type=int)

#click argument
# @click.argument("number1", default="Jeff")
# @click.argument("number2", default="Jeff")
# @click.argument("method", default="Jeff")

# #multiple options
# # @click.option("--location",'-l', help="Places You've visited", multiple=True)
# def main(number1, number2, method ):#, salary, location):
#     """ Add Number 1 and Number 2 """
#     if method == 'add':
#         result = int(number1) + int(number2)
#     elif method == 'subtract':
#         result = int(number1) - int(number2)
#     elif method == 'multiply':
#         result = int(number1) * int(number2)
    # click.echo(result)
    # click.echo("Hello world, {}. My Salary is {}".format(name,sum(salary)))
    # click.echo('\n'.join(location))
    # click.echo("Hello my name is {}".format(name))

# @click.command()
# @click.argument('source', nargs=-1)
# @click.argument('destination', nargs=1)

# def main(source, destination):
#     for f in source:
#         click.echo('Moving {} to Folder {}'.format(f,destination))
# @click.command()
# @click.option('--name')#, prompt="Enter your name")
# @click.option('--password', hide_input=True, prompt=True,confirmation_prompt=True)
# def main(name, password):
#     # fname = click.prompt("Enter your firstname")
#     click.echo(f"Your name is {name} and your password is {password}")

# if __name__ == '__main__':
#     main()



# class RemoteControl():
#     def __init__(self):
#         self.channels = ["HBO","cnn","abc","espn"]
#         self.index=-1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.index+=1
#         if self.index == len(self.channels):
#             raise StopIteration
#         return self.channels[self.index]
    
#     def __len__(self):
#         return 5

#     def __str__(self):
#         return "this is a remote control"

# r= RemoteControl()
# print(len(r))
# print(r)
# itr=iter(r)
# print(itr.)
# print(next(itr))
# import os
# from pathlib import Path
# x = Path('.')
# print(os.path.getsize(x))


# x = [x for x in range(10) if x % 2 == 0]
# print(x)

 

# import os
# from pathlib import Path
# filepath = Path(r'C:\Users')
# for dirpath,dirnames,filenames in os.walk(filepath):
#     # print("dirpath",dirpath)
#     if dirpath == filepath:
#         # print(filenames)
#         if len(filenames) > 0:
#             for x in filenames:
#                 print(x, '1234142')
#         else:
#             for x in os.listdir(filepath):
#                 print(x)
#     # else:
#     #     print(dirpath)
 
# for x in os.listdir(filepath):
#     abspath = os.path.join(filepath, x)
#     if os.path.isdir(abspath):
#         print('dir',x)
#     elif os.path.isfile(abspath):
#         print('file',x)




# class exampleArgs():
#     def AddNumbers(self, x, y, z=''):
#         if z:
#             print("I'm in the z")
#             return x + y
#         if y is None:
#             print("I'm in the y")
#             return x + z 
#         if x is None:
#             print("I'm in the x")
#             return y + z 

#     def myfunc2(*zzz, **kwargs):
#         for a in zzz:
#             print(a)

# testing = exampleArgs()
# print(testing.AddNumbers(1,3, 4))
# print("Is this working?")

# testing.myfunc2(3,4,5,1)
# 
# mydict = {'value1':['asdf','asdf','5555'],'value2':['aaaa','bbbb','cccc']}
# dictlist = mydict.items()
# print(type(dictlist))
# mylist = sorted(dictlist, key=lambda x: x[0],reverse=True)
# print(type(dictlist))
# print(dictlist)
# for key, value in mydict.iteritems():
#     temp = [key,value]
#     dictlist.append(temp)

# print(dictlist)

##returning functions 
# def htmltag(tag):
#     def htmlbody(msg):
#         print('<{0}>{1}</{0}>'.format(tag,msg))
#     return htmlbody

# x=htmltag('h1')
# x('this is a header')
# x('another header')

# x=htmltag('p')
# x('this is a paragraph')

# mx = lambda x,y:x if x > y else y

# print(mx(5,10))

#in line lambda functions and map function
# mylist = range(1,9)
# print((map(lambda x: x**2, mylist)))
# print([x**2 for x in mylist])

#filter function. Without list function, returns filter object
# print(list(filter(lambda x: x>4, mylist)))

# from functools import reduce
#reduce function
# print(reduce(lambda x,y: x*y, mylist))



# def getHighestDigit(x):
#     for digit in range(1,10):
#         if x % digit >= 0:
#             highestDigit = digit
#     return highestDigit

### Find the highest digit
# nextdigit = X - getHighestDigit(X)
# intstring = str(getHighestDigit(X))
# while nextdigit >= 10:
#     nextdigit = nextdigit - getHighestDigit(nextdigit)
#     intstring += str(nextdigit)
# intstring += str(nextdigit)
# print(intstring)
##################333

# Find minimum int N ..... L<= N <= D and the sum of its digits is X
# Find maximun int M ..... L <= M <= D and the sum of its digits is X
# 1 100 4 => 4 40
# 100 500 12 => 129 480


# 1 100 4 => 4 40
# 100 500 12 => 129 480

# import re
# newtxt="200 sample text with many lines\n hell01 \n hell02 \n hell03 \n hell04 \n hell05\n hell06\n hell07 \n hell08"
# text = re.compile(r'^\d{3} [a-z].*')
# mylist = newtxt.split('\n')

# if text.match(mylist[0]):
#     print(mylist[0][0:3].rstrip())
#     for x in range(1,6):
#         print(mylist[x].strip())
# import random

# highest = 10
# answer = random.randint(1, highest)
# print(answer)   #TODO: Remove after testing
# print("Please guess the number between 1 and {}: ".format(highest))
# guess = int(input())

# while answer:
#     if guess == 0:
#         print("Game Over")
#         break
#     if guess == answer:
#         print("Hurray you got it")
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher: ")
#             guess = int(input())
#         if guess > answer:
#             print("Please guess lower: ")
#             guess = int(input())
Lines = ["bldr_Game_wall_5m|13751.722656 46.671505 2962.292480|-155.094345 0.000000 -2.000000"]
for line in Lines:
    test = line.split('|', 3)
    objline = "SpawnObject( ", "\"",test[0],"\"", ", " , "\"",test[1],"\"", ", " , "\"",test[2],"\"" , ");\n"
    print("SpawnObject( ", "\"",test[0],"\"", ", " , "\"",test[1],"\"", ", " , "\"",test[2],"\"" , ");\n")
    