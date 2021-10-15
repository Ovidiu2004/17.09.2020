a=str(input("Introduceti un sirul- "))
a="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
a1=""
a2=a
a3=a
#a
print("Sirul initial: ", a)
for k in a:
    a=chr(ord(k)+1)
    a1+=a
    b=a1.replace('!',' ')
    c=b.replace('[','A')
print("primul sir este- ",c)
#b
for k in a2:
    e=a2.replace(('Z'),('A'))
print("al doilea sireste- ",e)
#c
for k in a3:
    f=a3.replace((' '),('-'))
print("al treilea sir este- ",f)