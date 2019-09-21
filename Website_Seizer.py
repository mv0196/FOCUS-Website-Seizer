websitelist=["https://www.facebook.com","https://www.youtube.com","www.youtube.com"]
path="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect="127.0.0.1"
from datetime import datetime as dt
while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,14)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
		with open(path,'r+') as f:
			content=f.read()
			for w in websitelist:
				if w in content:
					pass
				else:
					f.write(redirect+"  "+w+"\n")
	else:
		# with open(path,'r') as f:
			# content=f.readlines()
		# print(len(content))
		# for i in websitelist:
			# for j in content:
				# if i in j:
					# print(j)
					# content.remove(j)
		# print(len(content))			
		# with open(path,'w')as f:
			# for i in content:
				# f.write(i)
		with open(path,'r+') as f:
			content=f.readlines()
			f.seek(0)
			for line in content:
				if not any(w in line for w in websitelist): #genetaror or tupple comprehension
					f.write(line)
			f.truncate()