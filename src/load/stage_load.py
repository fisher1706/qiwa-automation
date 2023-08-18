from typing import Optional

from locust import LoadTestShape

from src.load.locustfile import users

users_count = len(users)


class LoadShape(LoadTestShape):
    time_limit = 600

    stages: list[dict] = [
        {"duration": 60, "users": users_count // 5, "spawn_rate": 1},
        {"duration": 150, "users": users_count // 1.5, "spawn_rate": 2},
        {"duration": 300, "users": users_count, "spawn_rate": 5},
        {"duration": 350, "users": users_count // 1.5, "spawn_rate": 2},
        {"duration": 500, "users": users_count, "spawn_rate": 5},
        {"duration": 560, "users": users_count // 1.5, "spawn_rate": 2},
        {"duration": 600, "users": users_count // 5, "spawn_rate": 1},
    ]

    def tick(self) -> Optional[tuple[int, int]]:
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
