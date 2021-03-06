__author__ = 'thauser'
from argh import arg

import logging
from pnc_cli import utils
from pnc_cli.swagger_client.apis import BuildconfigurationsetsApi
from pnc_cli.swagger_client.apis import BuildconfigsetrecordsApi


sets_api = BuildconfigurationsetsApi(utils.get_api_client())
bcsr_api = BuildconfigsetrecordsApi(utils.get_api_client())


@arg("-p", "--page-size", help="Limit the amount of build records returned")
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_build_configuration_set_records(page_size=200, sort="", q=""):
    """
    List all build configuration set records.
    """
    response = utils.checked_api_call(bcsr_api, 'get_all', page_size=page_size, sort=sort, q=q)
    if response:
        return response.content


@arg("id", help="ID of build configuration set record to retrieve.")
def get_build_configuration_set_record(id):
    """
    Get a specific BuildConfigSetRecord
    """
    response = utils.checked_api_call(bcsr_api, 'get_specific', id=id)
    if not response:
        logging.error("A BuildConfigurationSetRecord with ID {} does not exist.".format(id))
        return
    return response.content


@arg("id", help="ID of BuildConfigSetRecord to retrieve build records from.")
@arg("-p", "--page-size", help="Limit the amount of build records returned")
@arg("-s", "--sort", help="Sorting RSQL")
@arg("-q", help="RSQL query")
def list_records_for_build_config_set(id, page_size=200, sort="", q=""):
    """
    Get a list of BuildRecords for the given BuildConfigSetRecord
    """
    bcrs_check = utils.checked_api_call(sets_api, 'get_all', q="id==" + id)
    if not bcrs_check:
        logging.error("A BuildConfigurationSet with ID {} does not exist.".format(id))
        return
    response = utils.checked_api_call(bcsr_api, 'get_build_records', id=id, page_size=page_size, sort=sort, q=q)
    if response:
        return response.content
