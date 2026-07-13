from sklearn import tree

#[height, weight, shoe size]

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [190, 75, 43], [175, 60, 42], [155, 55, 35]]

y = ['male', 'female', 'female', 'male', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

altura = int(input("Digite a altura: "))
peso = int(input ("Digite o peso: "))
shoe_size = int(input("quanto calça: "))
dados = [altura, peso, shoe_size]

prediction = clf.predict([[altura, peso, shoe_size]])
print (prediction)