
################################################################
### print a decision tree
from sklearn.tree import DecisionTreeRegressor, export_graphviz
import subprocess

def visualize_tree(tree, tree_name, feature_names):
    """Create tree png using graphviz

    Args
    ----
    tree:           scikit-learn DecsisionTree
    tree_name:      name of the tree
    feature_names:  list of feature names
    
    Source: http://chrisstrelioff.ws/sandbox/2015/06/08/decision_trees_in_python_with_scikit_learn_and_pandas.html
    """
    with open("{0}.dot".format(tree_name), 'w') as f:
        export_graphviz(tree, out_file=f, filled=True, feature_names = feature_names, proportion=False, rounded = True)

    command = ["dot", "-Tpng", "{0}.dot".format(tree_name), "-o", "{0}.png".format(tree_name)]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to produce visualization")

'''
dt = DecisionTreeClassifier()
dt.fit(X,y)

visualize_tree(dt, 'dt_01', X.columns)
'''
################################################################