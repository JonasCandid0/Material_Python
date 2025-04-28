linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)  

'''o len é o contador de cada algarismo ou letra q está passada na lista, esse código está 
contando cada dado presente na variavel linguagens, ele faz isso de forma ordenada mas n sendo em ordem alfabetica
é feito por contagem de algarismos ou letras '''

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens) 
'''aqui já é feito a ordenação ao contrário, é pego os dados mais extensos como python e csharp 
como os primeiros a serem puxados'''