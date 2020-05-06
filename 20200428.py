# print('Hello World')
# print('Hello World'.upper())
# print('Hello World'.lower())
# print('Hello World. I am Tack.'.upper().split(' '))

# x = 'Hello World'
# print(x)
# print(x.upper())

# x ='Good morning'
# x=x.upper()
# print(x)

# print(['Hello'])
# print(type(['Hello']))
# print(['Hello','World'])
# print(['a','b','c',1,2,3])
# print(['a','b',['c',1,2,3]])

# print(['a','b','c','d','e'][0])
# print(['a','b',['c',1,2,3]][2])
# print(['a','b',['c',1,2,3]][2][0])
# print(['a','b','c','d','e'][-1])

# print(['a','b','c',[0,1,2,3]][3][1:3])
# # 1から3まで取り出す、3含まない
# x = ['a','b','c']
# x[1]='BBB'
# print(x)
# x.append('d')
# print(x)

# # タプルtuple
# print(('Hello','World'))
# print(type(('Hello','World')))
# print(('Hello',))
# print(('a','b','c','d','e')[2:5])
# print((1,2,3,['a','b','c']))

# # ディクショナリ
# print({'a':'apple'})
# print(type({'a':'apple'}))
# print({'a':'apple','b':'ball','c':'cat'})
# print({'a':'apple','b':'ball','c':'cat'}['a'])

# x = {'a':'apple','b':'ball','c':'cat'}
# print(x['a'])

# x = {1:'apple',2:'ball',3:'cat'}
# print(x[1])

# x = {'a':'apple','b':'ball','c':'cat'}

# # 追加
# x['d'] = 'dog'
# print(x)

# # 上書き
# x['c'] = 'cat2'
# print(x)

# # 削除
# del x['c']
# print(x)

# # 削除、取り出し
# x.pop('d')
# print(x)

# x.update({'c':'cat'})
# print(x)

# # ディクショナリで一度に追加
# x.update({'d':'dog','e':'egg'})
# print(x)

# y = {'d':'dog','e':'egg'}
# x.update(y)
# print(x)

# y = {'c':'cat2','d':'dog'}
# x.update(y)
# print(x)

# x = {'a':'apple','b':'ball','c':'cat'}

# # キーを取り出す
# print(x.keys())
# y1 = x.keys()
# print(y1) #dict_keys(['a','b','c'])
# # 取り出したキーをリストとして代入
# y2 = list(y1)
# print(y2) #['a','b','c']
# print(y2[0]) #a
# print(x[y2[0]]) #apple

# # 値を取り出す
# print(x.values()) #dict_values(['apple','ball','cat'])

# # 組み合わせそのままタプルのリストで取り出す
# print(x.items()) #dict_items([('a','apple'),('b','ball'),('c','cat')])

# print(len(['a','b','c','d'])) # 4
# print(len('abcde')) # 5
# print(range(len('abcde'))) # range(0, 5)

# print(type(True))
# print('abc'=='abc') # True
# print('a' in ['a','b','c'])
# print('a' in 'abc')
# print(True and True)
# print(False or False) # False

# for i in [1,2,3,4,5]:
#   for j in [10,20,30,40,50]:
#     print(i,j)
# for i in 'Hello World':
#   print(i)
# x = {'a':'apple','b':'ball','c':'cat'}
# for i in x.values():
#   print(i)
# for i in x:
#   print(x[i])
# for i in x.items():
#   print(i)

print([i for i in 'abcde']) # ['a','b','c','d','e']
print([i + i for i in 'abcde']) # ['aa','bb','cc','dd','ee']
# 仕組み↓
x=[]
for i in 'abcde':
  x.append(i)
print(x) # ['a','b','c','d','e']

print([i*100 for i in [1,2,3,4,5,]]) # [100,200,300,400,500]
print([i*5 for i in range(5)]) # [0,5,10,15,20]

x={'a':'apple','b':'ball','c':'cat'}
print([x[key] for key in x]) # ['apple','ball','cat']