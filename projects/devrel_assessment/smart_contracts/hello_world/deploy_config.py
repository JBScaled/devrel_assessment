import logging

import algokit_utils
from algokit_utils import (
    TransactionParameters,
)
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)

# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.hello_world.hello_world_client import (
        HelloWorldClient,
    )

    app_client = HelloWorldClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )
    message = "Jorrin! Welcome to the wonderful world of Algorand"

    box_name = "Success"
    
    #call the hello method and pass in the neccessary Box reference 
    response = app_client.hello(message=message, box_name=box_name, transaction_parameters=TransactionParameters(boxes=[(1018, box_name)]))
    logger.info(
        f"Called hello on {app_spec.contract.name} ({app_client.app_id}) "
        f"with name={message}, received: {response.return_value}"
    )
