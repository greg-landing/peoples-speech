
from search.engine.existing_dataset_search_engine import ExistingDatasetSearchEngine

class SearchEngineFactory:
    def __init__(self, config):
        self.config = config

    def create(self):
        if self.config["engine"] == "ExistingDatasetSearchEngine":
            return ExistingDatasetSearchEngine(self.config)




