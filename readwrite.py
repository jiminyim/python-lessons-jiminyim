with open('name.txt') as f:
    my_name = f.read()

with open('output/hello.txt', 'w') as f:
    f.write("Hello, our names are ")
    f.write(my_name)