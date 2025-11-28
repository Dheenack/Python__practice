# %%
# generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Usage
for num in count_up_to(5):
    print(num)
print("after 1 loop")
for num in count_up_to(5):
    print(num)
# %%

# generator expression
squares = (x**2 for x in range(5))

# Usage
for square in squares:
    print(square)

print("after 1 loop")
for square in squares:
    print(square)
# %%
