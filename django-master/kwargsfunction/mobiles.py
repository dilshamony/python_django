mobiles={
    "galaxya6":{"frontcam":"14px","rearcam":"40px","ram":8,"price":18000},
    "galaxya5":{"frontcam":"12px","rearcam":"30px","ram":4,"price":8000},
    "galaxya2":{"frontcam":"10px","rearcam":"20px","ram":3,"price":4000}
}

mobilename=input("enter mobile name")
spec=input("enter specification")
#print(mobiles[mobilename][spec)-->error
if mobilename in mobiles:
    print(mobiles[mobilename])#print full detais of that mobile
    print(mobiles[mobilename]["price"])#print price of that mobile
    if spec in mobiles[mobilename]:
        print(mobiles[mobilename][spec])
    else:
        print("invalid specification")
else:
    print("no mobiles exist with given name")