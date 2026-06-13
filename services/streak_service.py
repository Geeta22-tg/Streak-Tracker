import csv
import os
from models.streak import Streak

class StreakService:

    FILE_NAME = "streaks.csv"

    @classmethod
    def get_all_streaks(cls):

        streaks = []

        try:
            with open(cls.FILE_NAME, "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    streak = Streak(
                        row["skill"],
                        row["days"]
                    )

                    streaks.append(streak)
        except FileNotFoundError:
            pass

        return streaks

    @classmethod
    def add_streak(cls, skill):

        file_exists = os.path.exists(cls.FILE_NAME) and os.path.getsize(cls.FILE_NAME) > 0

        with open(cls.FILE_NAME, "a", newline="") as file:

            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Skill", "Days"])

            writer.writerow([skill, 0])

    @classmethod
    def increase_streak(cls, skill):

        streaks = cls.get_all_streaks()

        with open(cls.FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["skill", "days"])

            for streak in streaks:

                if streak.skill == skill:
                    streak.increase_streak()

                writer.writerow(streak.provide_in_list())