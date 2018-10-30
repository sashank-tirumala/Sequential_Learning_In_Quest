import pandas as pd
from Node import Node

class Tree:
    def __init__(self, cat_attr_list, num_attr_list):
        self.class_list_name = 'prog/Class_List_Index'
        self.cat_attr_list1 = cat_attr_list
        self.num_attr_list1 = num_attr_list
        todo = 1

    def display(self):
        todo = 1
    def create_tree(self):
        name_list = [root_node]
        for node_name in name_list:
            new_node_names = split(node_name)
            name_list.remove(node_name)
            if(new_node_names != None):
                name_list.append(new_node_names[0])
                name_list.append(new_node_names[1])
        todo = 1
    def split(self, node_name):
        temp_node = Node(node_name)
        values = temp_node.eval_attr_for_node(cat_attr_list=self.cat_attr_list1, num_attr_list=self.num_attr_list1)
        new_names = self.find_new_names(node_name)
        self.update_class_list(values, new_names)
        return new_names

    def new_names(self, node_name):
        node_name = node_name[1:]
        val = int(node_name)
        newvals = ('N'+str(val*2), 'N'+str(val*2+1))
        return newvals

    def update_class_list(self, node_data, new_names):
        attr_data = self.load_attr_data(node_data)
        if(node_data['attr'] in self.cat_attr_list1):
            # a1 = attr_data[attr_data[node_data['attr']].isin(node_data['split'])]
            # a_not_1 = attr_data[~attr_data[node_data['attr']].isin(node_data['split'])]
            a1 = attr_data[attr_data[node_data['attr']].isin(node_data['split'])]
            a2 = attr_data[~attr_data[node_data['attr']].isin(node_data['split'])]
            a2['node'] = new_names[1]
            a1['node'] = new_names[0]
            print(a1.head())
            print(a2.head())
            # print(attr_data.loc[!islesser].head())
        # attr_data1 = attr_data.cut[node_data['split']]
        # print[attr_data1.head()]

    def load_attr_data(self, node_data1):
        df = pd.merge(pd.read_csv('prog/'+node_data1['attr']),pd.read_csv(self.class_list_name),on='class_index')
        df = df.loc[df['node'] == node_data1['name']]
        return df



attr_list1 = ['Sex','Pclass']
attr_list2 = ['Age','Fare']
t1 = Tree(cat_attr_list=attr_list1, num_attr_list=attr_list2)
n1 = Node('N1')
values = n1.eval_attr_for_node(cat_attr_list=attr_list1, num_attr_list=attr_list2)
t1.update_class_list(values,['N2','N3'])
