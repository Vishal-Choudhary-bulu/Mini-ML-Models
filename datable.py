from sklearn import tree

#[hot, crazy, caring, stupid]

X = [[3,8,2,5],[2,4,8,2],[6,2,2,6],[7,8,3,3],[4,5,6,8],[5,8,2,9],[4,9,8,3],[8,7,5,9],[9,6,2,7],[8,2,8,4]]

Y = ["dont't date", "date", "date","date", "don't date","don't date","date","date","don't date","date"]

guru = tree.DecisionTreeClassifier()

guru = guru.fit(X,Y)

asker = guru.predict([[6,3,5,6]])

print(asker)