#coding=utf-8
import random
#我们要生成200个激活码 1.首先需要定义一个get函数，这个函数可以生成一个字符串和数字组成的随机序列
#2.加入一个循环调用get函数200次
#3.写入一个txt文档中
def get(a):
	 string=[chr(i) for i in range(97,123)]
	 number=[chr(i) for i in range(48,58)]
	 all_chr=string+number
	 b=0
	 strings=''
	 while b<a:
		 strings+=''.join(random.sample(all_chr,1))
		 b+=1
	 return strings
if __name__ == '__main__' :
	lists=[]
	c=0
	while c<200: 
		 lists.append(get(20)+'\n')
		 c+=1
	e='201.txt'
	with open(e,'w') as file_object:
		 for list in lists:
			 file_object.write(list)
