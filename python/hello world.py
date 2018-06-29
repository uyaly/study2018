# print('hello, world')

subdirs = [r'..\books\22.Look Out Fish!', r'..\books\23.Sleeping animals']

for i in range(len(subdirs)):
    # name = str[subdirs[i].rfind("/")+1:subdirs[i].rfind(".")]
    # print subdirs[i]
    name = str(subdirs[i])
    # print name
    lenth = len(subdirs[i])
    print name[9:lenth]