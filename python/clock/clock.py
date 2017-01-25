class Clock(object):
    """ Returns time from inputed hours and minutes """

    def __init__(self, hours=None, minutes=None):
        """ Initialize the Clock object """
        if hours is None:
            self.hours = 0
        else:
            self.hours = hours

        if minutes is None:
            self.minutes = 0
        else:
            self.minutes = minutes

        self.time_min = (self.hours * 60) + self.minutes
        self.time_min = self.time_min % 1440

    def add(self, minute=None):
        self.time_min += minute
        self.time_min = self.time_min % 1440

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        """ Returns the hh:mm time format """
        return '{:02d}:{:02d}'.format(
            self.hours,
            self.minutes
            # int(self.time_min / 24),
            # self.time_min % 60
        )
