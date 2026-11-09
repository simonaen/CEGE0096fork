class Triangle:
    def __init__(self, angles):
        if self.is_valid(angles):
            self.__a, self.__b, self.__c = angles


    @staticmethod
    def is_valid(angles):
        """Static method that doesn't require an instance of the class to validate wheter @angles can build a valid triangle.
        Based on the rules that: 
            1. The angles are 3; 
            2. All angles are bigger than 0; 
            3. The sum of all angles is 18
        Returns True or False on the basis of the requirements being met.    
        """
        return (len(angles) == 3 
                and all(a > 0 for a in angles) 
                and sum(angles) == 180
         )

    @property
    def name(self):
        """Returns class instance name. Neede to know which type of triangle is created."""
        return self.__class__.__name__
    

class Equilateral(Triangle):
    """All three angles are equal."""


class Isosceles(Triangle):
    """Exactly two angles are equal."""


class Scalene(Triangle):
    """All angles are different."""