# infoset


infoset is Python 3 inventory system that reports and tabulates the status of network connected devices. The information reported includes:

1. Open Systems Interconnection model (OSI model) data such as:
  1. Layer 1 information (Network port names, speed, state, neighbors)
  2. Layer 2 information (VLANs, 802.1q trunk links)
  3. Layer 3 information (ARP information)
2. System status

## Features
infoset has the following features:

1. Open source.
2. Written in python, a modern language.
3. Easy configuration.
4. Threaded polling of devices for data. Fast.
5. Support for Cisco and Juniper gear. More expected to added with time.
6. Support for SNMPv2 and/or SNMPv3 for all configured network devices.

We are always looking for more contributors!

## Inspiration
The project took inspiration from switchmap whose creator, Pete Siemsen, has been providing guidance.

## Oversight
infoset is a student collaboration between:

1. The University of the West Indies Computing Society. (Kingston, Jamaica)
2. The University of Techology, IEEE Student Branch. (Kingston, Jamaica)
3. The Palisadoes Foundation http://www.palisadoes.org

And many others.

## Dependencies
The only dependencies that must be manually installed for this project are pip,python3 and rrdtool itself.
### Ubuntu / Debian / Mint
The commands are:
```
# sudo apt-get install python3 python3-pip python3-dev librrd-dev rrdtool
```

### Fedora
The commands are:
```
# sudo apt-get install python3 python3-pip python3-dev librrd-dev rrdtool
```
# Developing
![](http://i.imgur.com/cJP2vks.gif)
```
# git clone https://github.com/UWICompSociety/infoset
# cd infoset
# sudo make
# source venv/bin/activate
# sudo make install
```
Infoset also includes a web interface, to start the server run `python3 server.py` then navigate to <http://localhost:5000>

## Creating Executable
`infoset` follows traditional python project structure and includes a `setup.py` file which can be used to create and install
an executable for the project. This is achieved through the `make develop` command, which will place the `infoset` executable
into /venv/bin/infoset and /bin/infoset. Alternatively, you can run the commands manually, `python setup.py develop` or `python setup.py install`

# Configuration Samples

The `examples/` directory includes a number of sample files. These will now be explained.

#Script Linting
Running `python lint.py script.py` in the top level directory of the repo will run the in-house code style checker, pep8 and pyflakes on `script.py`. Utilizing the `--test` flag will add the in-house test file to the argument list. For example, running `python lint.py --test infoset/web/ws_device.py` outputs:

pep8 output:

code_style_test.py:625:1: E302 expected 2 blank lines, found 1


pyflakes output:

code_style_test.py:635: undefined name 'defaultdict'
code_style_test.py:647: undefined name '_ifindex'


Script output:

code_style_test.py:
  __init__: line 28: no. of arguments in function signature and no. of arguments in docstring are not the same.
  __init__: line 28: config is found in function signature's argslist, but not in docstring
  __init__: line 28: host is found in function signature's argslist, but not in docstring
  __init__: line 28: no docstring found
  ethernet: line 34: no. of arguments in function signature and no. of arguments in docstring are not the same.
  ethernet: line 34: config is found in docstring, but not in function signature's argslist
  ethernet: line 34: host is found in docstring, but not in function signature's argslist
  device: line 51: no. of arguments in function signature and no. of arguments in docstring are not the same.
  device: line 51: config is found in docstring, but not in function signature's argslist
  device: line 51: host is found in docstring, but not in function signature's argslist
  _port_enabled: line 222: enabled is returned in the function, but is not found in the return section of the docstring
  _port_enabled: line 222: active is in the return section of the docstring, but is not returned in the function
  _port_up: line 245: enabled is returned in the function, but is not found in the return section of the docstring
  _port_up: line 245: active is in the return section of the docstring, but is not returned in the function
  _get_inactive: line 291: no. of arguments in function signature and no. of arguments in docstring are not the same.
  _get_inactive: line 291: port_data is found in docstring, but not in function signature's argslist
  _get_inactive: line 291: 'TBD' is returned in the function, but is not found in the return section of the docstring
  _get_inactive: line 291: inactive is in the return section of the docstring, but is not returned in the function
  _get_vlan: line 413: vlans is returned in the function, but is not found in the return section of the docstring
  _html_footer: line 441: html is in the return section of the docstring, but is not returned in the function
  _html_header: line 459: html is in the return section of the docstring, but is not returned in the function
  _index_html: line 483: no. of arguments in function signature and no. of arguments in docstring are not the same.
  _index_html: line 483: config is found in function signature's argslist, but not in docstring
  _index_html: line 483: html is in the return section of the docstring, but is not returned in the function
  cdpcachedeviceid: line 625: no. of arguments in function signature and no. of arguments in docstring are not the same.
  cdpcachedeviceid: line 625: var is found in docstring, but not in function signature's argslist
  cdpcachedeviceid: line 625: oid is returned in the function, but is not found in the return section of the docstring

infoset/web/ws_device.py:
  ethernet: line 44: no. of arguments in function signature and no. of arguments in docstring are not the same.
  ethernet: line 44: config is found in docstring, but not in function signature's argslist
  ethernet: line 44: host is found in docstring, but not in function signature's argslist
  device: line 61: no. of arguments in function signature and no. of arguments in docstring are not the same.
  device: line 61: config is found in docstring, but not in function signature's argslist
  device: line 61: host is found in docstring, but not in function signature's argslist
  _port_enabled: line 232: enabled is returned in the function, but is not found in the return section of the docstring
  _port_enabled: line 232: active is in the return section of the docstring, but is not returned in the function
  _port_up: line 255: enabled is returned in the function, but is not found in the return section of the docstring
  _port_up: line 255: active is in the return section of the docstring, but is not returned in the function
  _get_inactive: line 301: no. of arguments in function signature and no. of arguments in docstring are not the same.
  _get_inactive: line 301: port_data is found in docstring, but not in function signature's argslist
  _get_inactive: line 301: 'TBD' is returned in the function, but is not found in the return section of the docstring
  _get_inactive: line 301: inactive is in the return section of the docstring, but is not returned in the function
  _get_vlan: line 423: vlans is returned in the function, but is not found in the return section of the docstring
  _html_footer: line 451: html is in the return section of the docstring, but is not returned in the function
  _html_header: line 469: html is in the return section of the docstring, but is not returned in the function
  _index_html: line 493: no. of arguments in function signature and no. of arguments in docstring are not the same.
  _index_html: line 493: config is found in function signature's argslist, but not in docstring
  _index_html: line 493: html is in the return section of the docstring, but is not returned in the function

You may also change how the script attemps to invoke pep8 and pyflakes, for e.g.:

    python lint.py --pep8invocation=blahblah --pyflakesinvocation=whatever_uu_want infoset/web/ws_device.py

## Apache Configuration Samples

The `examples/apache` directory includes sample files to create a:

1. dedicated infoset site (`sites-available.example.org.conf`)
2. URI of an existing site (`conf-available.example.conf`)

## infoset Configuration Samples

The `examples/etc` directory includes a sample files that can be edited. infoset assumes all files in this directory, or any other specified configuration directory, only contains infoset configuration files. Most user will only need to edit the three files supplied.

Feel free to use the `etc/` directory as your permanent configuration file location.

### Sample Configuration File
Here is a sample configuration file that will be explained later in detail. infoset will attempt to contact hosts with each of the parameter sets in the `snmp_group` section till successful.
```
web_directory: /home/example/public_html
data_directory: /home/example/infoset/data

hosts:
    - host1
    - host2
    - host3

snmp_groups:
    - group_name: Corporate Campus
      snmp_version: 3
      snmp_secname: woohoo
      snmp_community:
      snmp_port: 161
      snmp_authprotocol: sha
      snmp_authpassword: testing123
      snmp_privprotocol: des
      snmp_privpassword: secret_password

    - group_name: Remote Sites
      snmp_version: 3
      snmp_secname: foobar
      snmp_community:
      snmp_port: 161
      snmp_authprotocol: sha
      snmp_authpassword: testing123
      snmp_privprotocol: aes
      snmp_privpassword: secret_password
```
#### Configuration File Details Table

|Parameter|Description|
| --- | --- |
| data_directory: | The data directory where all infostor data will be kept. This can be the `data/` directory.|
| web_directory: | The directory where all infostor HTML files will be kept. Make this directory your web root.|
| hosts: | YAML key describing hosts. All hosts are listed under this key.|
| snmp_groups: | YAML key describing groups of SNMP authentication parameter. All parameter groups are listed under this key.|
| group_name: | Descriptive name for the group|
| snmp_version: | SNMP version. Must be present even if blank. Only SNMP versions 2 and 3 are supported by the project.
| snmp_secname: | SNMP security name (SNMP version 3 only). Must be present even if blank.|
| snmp_community: | SNMP community (SNMP version 2 only). Must be present even if blank.|
| snmp_port: | SNMP Authprotocol (SNMP version 3 only). Must be present even if blank.|
| snmp_authprotocol:| SNMP AuthPassword (SNMP version 3 only). Must be present even if blank. |
| snmp_authpassword:| SNMP PrivProtocol (SNMP version 3 only). Must be present even if blank.|
| snmp_privprotocol:| SNMP PrivProtocol (SNMP version 3 only). Must be present even if blank.|
| snmp_privpassword: | SNMP PrivPassword (SNMP version 3 only). Must be present even if blank.|
| snmp_port:| SNMP UDP port|

# The Toolbox.py Script : Running infoset
infoset comes with a handy `toolbox.py` script, this script provides all the same functionality as creating or installing the executable

## Testing Host Connectivity
You can test connectivity to a host using this command where the configuration directory is `etc/` and the host is `host1`
```
$ bin/toolbox.py test --directory etc/  --host host1
```

## Polling All Devices
This command will execute against all configured hosts and create appropriate YAML files in the configuration file's `$DATA_DIRECTORY/snmp` directory
```
$ bin/toolbox.py poll --directory etc/
```

## Creating Web Pages for All Devices
Update, Infoset is now using Flask! Pagemaker is no longer neccessary, run `python server.py`
and navigate to [localhost:5000](http://localhost:5000) to acess the web interface.

Your webserver will now be able to access the newest HTML in `$WEB_DIRECTORY`.

## Update Vendor MAC Addresses
inet flag will load from http://standards-oui.ieee.org/oui.txt, note this is a timely operation, there is a local cache of the file
excluding the inet tag will instead load the MAC Addresses from this file.

This command will execute against all configured hosts and create appropriate HTML files in the configuration file's `$WEB_DIRECTORY` directory
```
$ bin/toolbox.py oui --inet
```

Vendor MAC address can now be queried using the Oui class in the jm_lib directory.

# Next Steps
There are many dragons to slay and kingdoms to conquer!
## Contribute
Here are a few things to know.

1. Contributions are always welcome. Contact our team for more.
2. View our contributor guidelines here: https://github.com/UWICompSociety/infoset/blob/master/CONTRIBUTING.md
3. View our guidelines for committing code here: https://github.com/UWICompSociety/infoset/blob/master/COMMITTERS.md

## Mailing list
Our current mailing list is: https://groups.google.com/forum/#!forum/gdg-jamaica
## New Features
Visit our GitHub issues for a full list of features and bug fixes. https://github.com/UWICompSociety/infoset/issues
## Design Overview
Visit our wiki's infoset document for the rationale of the design. http://wiki.palisadoes.org/index.php/Infoset
## Sample Output
Visit http://calico.palisadoes.org/infoset to view infoset's latest stable web output.
