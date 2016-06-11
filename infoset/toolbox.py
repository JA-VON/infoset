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
import string
import os

# from pprint import pprint

OUI_URL = 'http://standards-oui.ieee.org/oui.txt'
OUI_YAML_FILE_NAME = "oui_data.yaml"

CACHE_FILE_PATH = '{}/bin/oui.txt'.format(os.getcwd())


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

    # Get vendor OUI MAC addresses
    if cli_args.mode == 'oui':
        do_oui(cli_args, config)


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


def do_oui(cli_args, config):
    """

    Converts the groups of addresses that are assigned to NIC manufacturers based on the first 3 bytes of the address
    into a YAML file stored in data/aux in directory

    :param config:
    :param verbose:
    :return: None
    """

    oui_data = {}
    if cli_args.inet is True:
        print('Reading OUI data from url:{}'.format(OUI_URL))
        response = urllib.request.urlopen(OUI_URL)
        # This is a very timely(>10 mins) operation
        data = response.read()
        data = data.split("\n")
        for line in data:
            hex_value = line[:6]
            if all(x in string.hexdigits for x in hex_value):
                organization = line[6:].replace("(base 16)", "").strip().title()
                oui_data[hex_value.lower()] = organization
    else:
        print('Reading OUI MAC Address data from local cache file in bin')
        with open(CACHE_FILE_PATH, 'r') as file_data:
            for line in file_data:
                hex_value = line[:6]
                if all(x in string.hexdigits for x in hex_value):
                    organization = line[6:].replace("(base 16)", "").strip().title()
                    oui_data[hex_value.lower()] = organization
    file_location = '{}/data/aux/{}'.format(os.getcwd(), OUI_YAML_FILE_NAME)
    with open(file_location, 'wt+') as f:
        yaml.dump(oui_data, f, default_flow_style=False)


if __name__ == "__main__":
    main()
