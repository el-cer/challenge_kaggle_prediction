def ordinal_encoding(row):
    if(row=="no"):
        return 0
    if(row=="Sometimes"):
        return 1
    if(row=="Frequently"):
        return 2
    if(row=="Always"):
        return 3

X['CAEC']=df_train['CAEC'].apply(ordinal_encoding)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.15,random_state =123)