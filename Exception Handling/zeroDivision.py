# %%
a=10/0
print(a)
# %%
try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
# %%
try:
    a=10/0
    print(a)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
    print("Error details:", e)
finally:
    print("Execution completed.")
# %%

print("other ecxeptions")
exceptions = """
1. IndexError
2. KeyError
3. ValueError
4. TypeError
5. FileNotFoundError
6. ImportError
7. AttributeError
8. RuntimeError
9. MemoryError
10. OverflowError
11. StopIteration
12. AssertionError
13. NameError
14. SyntaxError
15. IndentationError
16. TabError
17. OSError
18. ConnectionError
19. TimeoutError
20. RecursionError"""
print(exceptions)
# %%
