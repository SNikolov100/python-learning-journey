from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    valid_artifact = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact,
    }

    valid_collector = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.valid_artifact.keys():
            raise ValueError("Unknown artifact type!")

        artifact_object = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact_object:
            raise ValueError(f"{artifact_name} has been already registered!")

        cls = self.valid_artifact[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(cls)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.valid_collector:
            raise ValueError("Unknown collector type!")

        collector_object = next((a for a in self.collectors if a.name == collector_name), None)
        if collector_object:
            raise ValueError(f"{collector_name} has been already registered!")

        cls = self.valid_collector[collector_type](collector_name)
        self.collectors.append(cls)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        register_collector_name = next((c for c in self.collectors if c.name == collector_name), None)
        if register_collector_name is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        register_artifact_name = next((a for a in self.artifacts if a.name == artifact_name ), None)
        if register_artifact_name is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        if not register_collector_name.can_purchase(register_artifact_name.price, register_artifact_name.space_required):
            return "Purchase is impossible."
        self.artifacts.remove(register_artifact_name)
        register_collector_name.purchased_artifacts.append(register_artifact_name)
        register_collector_name.available_money -= register_artifact_name.price
        register_collector_name.available_space -= register_artifact_name.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {register_artifact_name.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        exist_artefact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if exist_artefact is None:
            return "No such artifact."
        self.artifacts.remove(exist_artefact)
        return "Removed " + exist_artefact.artifact_information()

    def fundraising_campaigns(self, max_money: float):
        count_increased_money = 0
        for cellector in self.collectors:
            if cellector.available_money <= max_money:
                cellector.increase_money()
                count_increased_money += 1
        return f"{count_increased_money} collector/s increased their available money."

    def get_auction_report(self):
        count_of_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        self.collectors.sort(key=lambda c: (-len(c.purchased_artifacts), c.name))

        result = ["**Auction statistics**",
                  f"Total number of sold artifacts: {count_of_sold_artifacts}",
                  f"Available artifacts for sale: {len(self.artifacts)}",
                  "***"
                  ]

        for collector in self.collectors:
            result.append(collector.__str__)
        return "\n".join(result)







