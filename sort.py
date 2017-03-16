import pandas as pd
dfrot = pd.read_csv("/Users/ernestomartinez/Documents/Winter17/Math180/newsudrot.csv")
df1 = pd.read_csv("/Users/ernestomartinez/Documents/Winter17/Math180/minstep.csv")
dfshift = pd.read_csv("/Users/ernestomartinez/Documents/Winter17/Math180/newsudshift.csv")
newsudrotsort = pd.DataFrame()
newsudshiftsort = pd.DataFrame()
for i in range(0,91):
	link = df1.Link_Type[i] # link
	tempnewsudrot = dfrot[link]
	tempnewsudrot = tempnewsudrot.sort_values() # sorts rotation links in lexicographic order
	tempnewsudrot = tempnewsudrot.reset_index(drop = True) # resets rotation index
	newsudrotsort = pd.concat([newsudrotsort,tempnewsudrot],axis = 1)
	tempnewsudshift = dfshift[link] 
	tempnewsudshift = tempnewsudshift.sort_values() # sorts shift links in lexicographic order
	tempnewsudshift = tempnewsudshift.reset_index(drop = True) # resets shift index
	newsudshiftsort = pd.concat([newsudshiftsort,tempnewsudshift],axis = 1)
newsudrotsort.index += 1
newsudshiftsort.index += 1
newsudrotsort.to_csv(path_or_buf = '/Users/ernestomartinez/Documents/Winter17/Math180/newsudrotSORTED.csv')
newsudshiftsort.to_csv(path_or_buf = '/Users/ernestomartinez/Documents/Winter17/Math180/newsudshiftSORTED.csv')