from project.artifacts.base_artifact import BaseArtifact


class RenaissanceArtifact(BaseArtifact):

    def artifact_information(self):
        return f"Renaissance Artifact: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}"

