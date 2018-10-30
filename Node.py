import pandas as pd

class Node:
    def __init__(self,name):
        self.name = name
        self.class_list_name = 'prog/Class_List_Index'
        self.histogram = pd.read_csv(self.class_list_name)['classification'].value_counts()
    def eval_attr_for_node(self,cat_attr_list, num_attr_list):
        """ This function will evaluate the best attribute for this node. It will then based on that choose the split point calculate Gini_Index, the histograms and so on"""
        if(self.histogram[True] == 0 or self.histogram[False] == 0):
            print('print terminal node, no further splitting required')
            return 'Terminal Node'
        else:
            best_gini = 1
            best_attr = ''
            best_split = 1
            # temp_num = NumericNode.NumericNode(self.name)
            for attr in cat_attr_list:
                new_pair = self.__eval_best_gini_cat__(attr)
                if(new_pair[0] < best_gini):
                    best_gini = new_pair[0]
                    best_split = new_pair[1]
                    best_attr = attr
            for attr in num_attr_list:
                new_pair = self.__eval_best_gini_num__(attr)
                if(new_pair[0] < best_gini):
                    best_gini = new_pair[0]
                    best_split = new_pair[1]
                    best_attr = attr
            res_dict = {'name':self.name, 'gini':best_gini, 'split': best_split, 'attr':best_attr}
            return res_dict
    def __eval_best_gini__(self, attr):
        print('Dynamic Bind, somehow parent func node is called, eval_best_gini')
    def __calculate_gini__(self, LT, LF, RT, RF):
        T1 = LT + LF
        T2 = RT + RF
        if(T2 == 0):
            return 1
        T = T1 + T2
        gini_T1 = 1- ((LF/T1)**2) -((LT/T1)**2)
        gini_T2 = 1- ((RF/T2)**2) -((RT/T2)**2)
        gini = (T1/T)*gini_T1 + (T2/T)*gini_T2
        return gini

    def __load_attr_data__(self, attr):
        print('Dynamic Bind, somehow parent func node is called, load_attr_data')


    def __eval_best_gini_cat__(self, attr):
        attr_data = self.__load_attr_data_cat__(attr)
        category_list = attr_data[attr].cat.categories.tolist()
        category_list = self.__get_all_subsets__(category_list)
        a1 = attr_data.groupby([attr,'classification']).size()
        best_gini = 1
        best_split = 1
        category_list.pop()
        for x in category_list:
            LT = 0
            RT = 0
            LF = 0
            RF = 0
            temp = attr_data[attr_data[attr].isin(x)]
            for y in x:
                LT = LT + a1[y][True]
                LF = LF + a1[y][False]
            RT = self.histogram[True] - LT
            RF = self.histogram[False] - LF
            current_gini = self.__calculate_gini__(RT,RF,LT,LF)
            if(current_gini < best_gini):
                best_gini = current_gini
                best_split = x
        return (best_gini,best_split)

    def __load_attr_data_cat__(self, attr):
        df = pd.merge(pd.read_csv('prog/'+str(attr), dtype={str(attr):'category'}),pd.read_csv(self.class_list_name),on='class_index')
        df = df.loc[df['node'] == self.name]
        df = df.drop(columns = ['node', 'class_index'])
        return df

    def __get_all_subsets__(self,catls):
        res = []
        siz = len(catls)
        for x in range(siz+1):
            temp = self.__choose__(catls, x)
            for y in temp:
                res.append(y)
        return res
    def __choose__(self, lists, n):
        res = []
        if n == 0:
            return res
        if(n == 1):
            for x in lists:
                temp = []
                temp.append(x)
                res.append(temp)
                # print('in loop 1')
        else:
            choose_1 = self.__choose__(lists, 1)
            i=1
            for x in choose_1:
                temp = lists.copy()
                temp = temp[i:]
                choose_n_1 = self.__choose__(temp, n-1)
                for y in choose_n_1:
                    res.append(x + y)
                i = i + 1
        return res

    def __eval_best_gini_num__(self, attr):
        attr_data1 = self.__load_attr_data_num__(attr)
        best_gini = 1
        best_split = 1
        LT = 0
        LF = 0
        RT = self.histogram[True]
        RF = self.histogram[False]
        for index, rows in attr_data1.iterrows():
            val = rows['classification']
            if(val == True):
                LT = LT + 1
                RT = RT - 1
            else:
                LF = LF + 1
                RF = RF - 1
            current_gini = self.__calculate_gini__(LT,LF,RT,RF)
            if(current_gini<=best_gini):
                best_gini = current_gini
                best_split = rows[attr]
        return (best_gini, best_split)

    def __load_attr_data_num__(self, attr):
        df = pd.merge(pd.read_csv('prog/'+str(attr)),pd.read_csv(self.class_list_name),on='class_index')
        df = df.loc[df['node'] == self.name]
        df = df.drop(columns = ['node', 'class_index'])
        return df



# n1 = Node('N1')
# num_attr_list1 = ['Age','Fare','Parents_Children_Aboard','Siblings_Spouses_Aboard']
# cat_attr_list1 = ['Sex','Pclass']
# print(n1.eval_attr_for_node(num_attr_list=num_attr_list1, cat_attr_list=cat_attr_list1))
t1 = ['a','b','c','d','e','f','g','h','i','j','k']
n1 = Node('N1')
print(n1.__choose__(t1,1))
