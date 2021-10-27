x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;


# w pythonie trzeba dbać o odpowiednie formatowanie kodu
# nie można użyć pętli for z zagnieżdżonym if'em w jednej linii tak ja poniżej

for i in "qwerty": if ord(i) < 100: print (i)

# powinniśmy podaną linię zapisać jako:
#
# for i in "qwerty":
#     if ord(i) < 100:
#         print (i)

for i in "axby":
    print (ord(i) if ord(i) < 100 else i)

