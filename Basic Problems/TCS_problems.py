# %%
"""
input : 5244
output : 160
explanation : 5*2*4*4 = 160
"""

def problem1(N : int)->int:
    ans:int=1
    print(ans)
    while N>0:
        ans*=N%10
        N//=10
    return ans
problem1(5244)
# %%
"""
String: sequence of characters
"""
def problem2(string: str)->None:

    return
# %%
# toggle binary value
def decToBinary(n:int)->str:

    bin:str = ""
    while n > 0:
        bit = n & 1 # checks for 0 or 1
        bin += str(bit)
        n = n >> 1

    # bin=bin[::-1]
    # bin = "".join("1"if n=="0" else "0" for n in bin) #toggle by for loop
    # return bin
    return int(bin,2)
print(decToBinary())
# %%
def tobinary(n:int)->int:
    # return bin(10)
    return bin(n^n.bit_length())
print(tobinary(10))
# %%
