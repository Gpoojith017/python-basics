a=[12,13,14,56]
try:
    print(a[1])
except ZeroDivisionError:
    print("error occured due to the zero division")
except IndexError:
    print("error occured due to index out of range")
except NameError:
    print("exception raised due to undefined variable")
except:
    print("some exception raised")
else:
    print("no exception at all")
finally:
    print("This is the finally")
print("out of the block")
