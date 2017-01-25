class Clock(object):
    """ A Clock class that ignores date """

    def __init__(self, hours=None, minutes=None):
        """ Initialize the Clock object """
        if hours is None:
            self.hours = 0
        else:
            self.hours = hours % 24

        if minutes is None:
            self.minutes = 0
        else:
            self.minutes = minutes

        self.time_min = (self.hours * 60) + self.minutes
        self.time_min = self.time_min % 1440

    def add(self, minute=None):
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
