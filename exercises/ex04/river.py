"""File to define River class."""

__author__ = "730482808"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    """Create class for River"""

    day: int
    bear: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages for fish and bears"""
        if Fish.age > 3:
            self.fish.pop
        if Bear.age > 5:
            self.bear.pop
        return None

    def bears_eating(self):
        """Facilitate removal of fish and hunger_score of bears"""
        if len(self.fish) > 4:
            self.remove_fish(3)
            Bear.eat(3)
        return None

    def check_hunger(self):
        """Check bear hunger score"""
        alive_bears: list[Bear] = self.bears
        if Bear.hunger_score() < 0:
            alive_bears.remove
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Bring new fish into population"""
        i: int = 0
        while i < len(self.fish) // 2:
            idx: int = 0
            while idx < 4:
                self.fish.append(Fish())
                idx += 1
            i += 1
        return None

    def repopulate_bears(self):
        """Bring new bears into population"""
        i: int = 0
        while i < len(self.bears) // 2:
            self.bears.append(Bear())
            i += 1
        return None

    def view_river(self):
        """Display population data of river"""
        return f"(~~~ Day {self.day}: ~~~ \
            Fish population: {self.fish} \
            Bear population: {self.bears})"

    def remove_fish(self, amount: int):
        """Function to remove fish"""
        alive_fish: list[Fish] = self.fish
        while amount > 0:
            alive_fish.remove
        self.fish = alive_fish
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None
