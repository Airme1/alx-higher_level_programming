class Robot:
    """Represents a robot, with a name."""

    # a class variable, counting the no of robots
    population = 0

    def __init__(self, name):
        """Initialize the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # when this person is created, the robot
        # adds to the population

        Robot.population += 1

    def die(self):
        """death of a robot"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greetings to masters"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """prints the current population"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-390")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work here. So let's destroy them.")

droid1.die()
droid2.die()

Robot.how_many()
