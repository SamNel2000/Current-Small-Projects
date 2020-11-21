#using backslash (\) allows you to make a statement
#and cover more than one line.
a = 5
b = 7
if a < \
	b:
	print(b - a)

#(), [], and {} all can span more than one line
names = ['Sam',
		'Matt']
print(names)

#List of Keywords, reserved words, myst be spelled exactly
"""
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""

#whitespace between strings means concatenation
print("cat" "dog" + " " + "catdog")

#strings, ints can just standalone:
420
"blazeit"
#and not effect anything

#float types
c = 3.14e-2 #numbers can be typed in scientific notation
d = 4e02 #zero after e ignored
e = 3.14_53_93 #underscores are allowed for grouping purposes
f = 23. #float assumed, after decimel point ignored
g = 5E5 #float and capital or Lowercase E doesn't matter
print(c, d, e, f, g)

#examples of imaginary iterals
print(3.14j,
	   10.j,
	   10j,
	   .001j,
	   1e100j,
	   3.14e-10j,
	   3.14_15_93j)

#none is an object that is used to 
#signify the absence of a value.
print(None)
#the truth value is false
if(None):
	print('None is true')
else:
	print('None is false')

print(Ellipsis)
print(...) #both Ellipsis and ... are the same
#the truth value is true
if(Ellipsis):
	print('... is true')
else:
	print('... is false')

#type shows what class something is
thing = "this"
print(type(thing))

#Name resolution of free variables occurs at runtime, 
#not at compile time. This means that the following
#code will print 42:
i = 10
def f():
    print(i)
i = 42
f()