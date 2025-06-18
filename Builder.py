from abc import ABC, abstractmethod

class MorningRoutineBuilder(ABC):
    def __init__(self):
        self.routine = []

    @abstractmethod
    def add_wake_up(self): pass

    @abstractmethod
    def add_activity(self): pass

    @abstractmethod
    def add_breakfast(self): pass

    def get_routine(self):
        return self.routine

class LazyPersonBuilder(MorningRoutineBuilder):
    def add_wake_up(self):
        self.routine.append("Wakes up at 11:00 AM")

    def add_activity(self):
        self.routine.append("Scrolls Reels 2 hours")

    def add_breakfast(self):
        self.routine.append("Drinks cold coffee with cookies")


class FitnessBuilder(MorningRoutineBuilder):
    def add_wake_up(self):
        self.routine.append("Wakes up at 5:30 AM")

    def add_activity(self):
        self.routine.append("Meditates, runs 5km")

    def add_breakfast(self):
        self.routine.append("Eats protein shake and eggs")


class MorningRoutineDirector(object):
    def __init__(self, builder):
        self.builder = builder

    def build_routine(self):
        self.builder.add_wake_up()
        self.builder.add_activity()
        self.builder.add_breakfast()

def print_routine(builder):
    routine = builder.get_routine()
    print("Morning Routine:")
    for do in routine:
        print(" -", do)
    print("")

lazy_builder = LazyPersonBuilder()
fit_builder = FitnessBuilder()

director = MorningRoutineDirector(lazy_builder)
director.build_routine()
print_routine(lazy_builder)

director = MorningRoutineDirector(fit_builder)
director.build_routine()
print_routine(fit_builder)

