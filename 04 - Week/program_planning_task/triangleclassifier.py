from triangle import Triangle, Equilateral, Isosceles, Scalene

class TriangleClassifier():
    """Class containg logic for classifying triangles"""
    
    def __init__(self):
        """Initialising method creates a dictonary where each triangle type is a key and the instances of it are the value"""
        self.__types = {
            "Equilateral":0, 
            "Isosceles":0, 
            "Scalene":0, 
            "None":0
            }
        

    def classify(self, angles):
        """Classify methods takes angles and unpacks them onto variable holding each angle in order to compare angle values.

        Checks whether the triangle is valid and returns None if not and adds +1 to None dictionary key if so.
        Checks if all angles are equal and creates Iscosceles object if so, adding +1 to Isosceles key in the class dictionary.
        Checks if 2 angles are equal and creates Equilateral object if so, adding + 1 to Equilateral key in the class dictionary.
        Else triangle is Scalene, +1 to Scalene key in class dictionay.
        """
        alpha, beta, gamma = angles

        if not Triangle.is_valid(angles):
            self.__types["None"] += 1
            return None
        elif alpha == beta == gamma:
            triangle = Equilateral(angles)
        elif alpha == beta or beta == gamma or alpha == gamma:
            triangle = Isosceles(angles)
        else:
            triangle = Scalene(angles)

        self.__types[triangle.name] += 1

    def get_types(self):
        print (self.__types)
    
    def __repr__(self):
        return f"""
            Equilateral: {self.__types["Equilateral"]}, 
            Isosceles: {self.__types["Isosceles"]}, 
            Scalene: {self.__types["Scalene"]}, 
            None : {self.__types["None"]}
        """