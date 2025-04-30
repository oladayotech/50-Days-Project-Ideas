a = isinstance("aa", str)

print(a)

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))