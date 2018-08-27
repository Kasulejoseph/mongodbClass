
try:
    print(5/0)
except Exception as e:
    print("error: ", type(e), e)
print("But life has to move on")