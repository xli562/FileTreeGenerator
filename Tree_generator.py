import os


def get_file_tree(path:str, iterations:int = 15) -> dict:
    # Making sure the input path is a directory, otherwise throw ValueError
    if os.path.isdir(path) == False:
        raise ValueError('Path provided is not a directory')
    else:
        relations = {}      # Dictionary of relations
        parents = []
        lastChildren = [path]       # Children from the last iteration
        if iterations >= 1:
            for iteration in range(iterations):
                parents = lastChildren
                relations[iteration+1] = {}
                print(f'iter{iteration}', parents)
                lastChildren = []
                for parent in parents:
                    if os.path.isdir(parent):
                        try:
                            children_of_parent = os.listdir(parent)
                            for n in range(len(children_of_parent)):
                                # Changing relative path to absolute path format for each child
                                children_of_parent[n] = parent + '/' + children_of_parent[n]
                                # Making the lastChildren list
                                lastChildren.append(children_of_parent[n])
                            relations[iteration+1][parent] = children_of_parent
                        except PermissionError as error:
                            error = str(error)
                            print('==========================')
                            print('==========================')
                            print('==============',error)
                            print('==========================')
                            print('==========================')

        return relations

relations = get_file_tree("D:/", 2)
print(relations)