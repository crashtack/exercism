class Clock(object):
    """ A Clock class that ignores date """

    def __init__(self, hours=0, minutes=0):
        """ Initialize the Clock object """
        self.hours = hours % 24
        self.minutes = minutes

        self.time_min = (self.hours * 60) + self.minutes
        self.time_min = self.time_min % 1440

    def add(self, minute=0):
        """ Add minutes to the time and check for overflow """
        self.time_min += minute
        self.time_min = self.time_min % 1440

        return '{:02d}:{:02d}'.format(
            int(self.time_min / 60) % 24,
            self.time_min % 60
        )

    def __eq__(self, other):
        """ Check if time_min is equal """
        if isinstance(other, self.__class__):
            return self.time_min == other.time_min
        else:
            return False

    def __ne__(self, other):
        """ Check if time_min is not equal """
        return not self.__eq__(other)

    def __str__(self):
        """ Returns the hh:mm time format """
        return '{:02d}:{:02d}'.format(
            int(self.time_min / 60) % 24,
            self.time_min % 60
        )
