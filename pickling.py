import pickle
import tkinter
f = open ("test.pck","rb")
pickle.dump(12.3,f)
pickle.dump([1,2,3], f)

f.close()

f = open ("test.pck","rb")
x = pickle.load(f)
y= pickle.load(f)

print (x)
print(y)

