# a=[1,2,2,3,4,5,5]
# b=[]
# def removedup():
# 	for i in a:
# 		if i not in b:
# 			b.append(i)
# 	return b
# b=removedup()
# k={}
# def createdict():
# 	j=0
# 	for i in b:
# 		k[j]=i
# 		j=j+1
# 	return k
# print(createdict())
	


class Person:
	def __init__(self, name, age):
		self.name1 = name
		self.age1 = age

	def walk(self):
		print("{} {} is walking".format(self.name1, self.age1))

