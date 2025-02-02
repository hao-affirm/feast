from tests.integration.feature_repos.integration_test_repo_config import (
    IntegrationTestRepoConfig,
)
from tests.integration.feature_repos.universal.data_sources.athena import (
    AthenaDataSourceCreator,
)

FULL_REPO_CONFIGS = [
    IntegrationTestRepoConfig(
        provider="aws",
        offline_store_creator=AthenaDataSourceCreator,
    ),
]

AVAILABLE_OFFLINE_STORES = [("aws", AthenaDataSourceCreator)]
