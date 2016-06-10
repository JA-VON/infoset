"""Calico utility script.

Calico utility script
"""

import yaml

import interfaces
from utils import ConfigReader
from utils import jm_general
from snmp import poll
from snmp import snmp_manager
from snmp import snmp_info
from web import ws_device
import urllib.request
import os

# import sys
# from pprint import pprint

OUI_URL = 'http://standards-oui.ieee.org/oui.txt'


def main():
    """Main Function.

    Args:
        None
    Returns:
        None
    """
    # Initialize key variables
    additional_help = """\
Utility script for the project.
"""

    # Process the CLI
    cli_object = interfaces.Cli(additional_help=additional_help)
    cli_args = cli_object.args()

    # Process the config
    config = ConfigReader(cli_args.directory)

    # Show configuration data
    if cli_args.mode == 'config':
        do_config(cli_args, config)

    # Show interesting information
    if cli_args.mode == 'test':
        do_test(cli_args, config)

    # Process hosts
    if cli_args.mode == 'poll':
        do_poll(config, cli_args.verbose)

    # Create pages
    if cli_args.mode == 'pagemaker':
        do_pages(config, cli_args.verbose)


def do_config(cli_args, config):
    """Process 'config' CLI option.

    Args:
        connectivity_check: Set if testing for connectivity
    Returns:
        None
    """
    # Show hosts if required
    if cli_args.hosts is True:
        print('hosts:')
        print(yaml.dump(config.hosts(), default_flow_style=False))

    # Show hosts if required
    if cli_args.snmp_auth is True:
        print('snmp_auth:')
        print(yaml.dump(config.snmp_auth(), default_flow_style=False))


def do_test(cli_args, config):
    """Process 'test' CLI option.

    Args:
        connectivity_check: Set if testing for connectivity
    Returns:
        None
    """
    # Show host information
    validate = snmp_manager.Validate(cli_args.host, config.snmp_auth())
    snmp_params = validate.credentials()
    snmp_object = snmp_manager.Interact(snmp_params)

    if bool(snmp_params) is True:
        print('\nValid credentials found:\n')
        print(yaml.dump(snmp_params, default_flow_style=False))
        print('\n')

        # Get SNMP data and print
        status = snmp_info.Query(snmp_object)
        yaml_data = status.everything()
        print(yaml_data)
    else:
        # Error, host problems
        log_message = (
            'Uncontactable host %s or no valid SNMP '
            'credentials found for it.') % (cli_args.host)
        jm_general.logit(1006, log_message)


def do_pages(config, verbose=False):
    """Process 'pagemaker' CLI option.

    Args:
        config: Configuration object
        verbose: Verbose output if True
    Returns:
        None
    """
    # Poll
    ws_device.make(config, verbose)


def do_poll(config, verbose=False):
    """Process 'run' CLI option.

    Args:
        config: Configuration object
        verbose: Verbose output if True
    Returns:
        None
    """
    # Poll
    poll.snmp(config, verbose)


def do_oui(config, verbose = False):
    """

    Converts the groups of addresses that are assigned to NIC manufacturers based on the first 3 bytes of the address
    into a YAML file stored in data/aux in directory

    :param config:
    :param verbose:
    :return: None
    """

    # uncomment if attempting to read from url
    # response = urllib.request.urlopen(OUI_URL)

    print('Reading OUI data from url:{}'.format(OUI_URL))

    # This is a very timely(>10 mins) operation reading from local cache instead
    # data = response.read()

    cache_file_path = '{}/infoset/bin/oui_cache.txt'.format(os.getcwd())
    oui_lines = []
    with open(cache_file_path,'r') as file_data:
        for line in file_data:
            oui_lines.append(line)

    for index in range(0, len(oui_lines)):
        pass




if __name__ == "__main__":
    main()
