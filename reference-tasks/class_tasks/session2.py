# ---------------------------------------------------------------------------- #
#                          Python Types Investigation                          #
# ---------------------------------------------------------------------------- #
#
# For each of these types: integer, float, boolean, string, list, tuple, dictionary, and set
#
# ----------------------------- Do the following: ---------------------------- #
#
#   1. Create an instance of that type with some values
#   2. Print the value and its id: print(my_var, id(my_var))
#   3. Attempt to modify the value (reassign, append, update, concatenate, etc.)
#   4. Print the value and its id again: print(my_var, id(my_var))
#   5. Answer the questions below:
#      - Is it mutable?
#      - How can it be modified?
#      - Was it a mutation or reassignment?
#
# ----------------------------------- Note ----------------------------------- #
# If id() is the same before and after, it's a mutation. If it's different, it's reassignment.

# Part 1

a = 1
b = 1.5
c = True
d = 'test'
e = [1, 2]
f = ('test', 1)
g = {
    'test1' : 1,
    'test2' : 2,
    'test3' : 3,
}
h = {1, 2, 3}



# Part 2

print('integer: ', a, id(a))
print('float: ',b, id(b))
print('boolean: ',c, id(c))
print('string: ',d, id(d))
print('list: ',e, id(e))
print('tuple: ',f, id(f))
print('dictionary: ',g, id(g))
print('set: ',h, id(h))


# Part 3

a = 'test'
b = b + 0.5
c = 'test'
d += d
e.append('new')
f = ('test2', 2)
g[c] = 'new'
h.add('new')

# Part 4

print('modified:')
print('integer: ', a, id(a))
print('float: ',b, id(b))
print('boolean: ',c, id(c))
print('string: ',d, id(d))
print('list: ',e, id(e))
print('tuple: ',f, id(f))
print('dictionary: ',g, id(g))
print('set: ',h, id(h))

# Part 5

# list dictionary and set are mutable as their id's remain the same
# the rest are immutable and were reassigned