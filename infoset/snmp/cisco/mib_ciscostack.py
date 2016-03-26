#!/usr/bin/env python3
"""Module for CISCO-STACK-MIB."""

from collections import defaultdict

from infoset.snmp.base_query import Query


class CiscoStackQuery(Query):
    """Class interacts with CISCO-STACK-MIB.

    Args:
        None

    Returns:
        None

    Key Methods:

        supported: Queries the device to determine whether the MIB is
            supported using a known OID defined in the MIB. Returns True
            if the device returns a response to the OID, False if not.

        layer1: Returns all needed layer 1 MIB information from the device.
            Keyed by OID's MIB name (primary key), ifIndex (secondary key)

    """

    def __init__(self, snmp_object):
        """Function for intializing the class.

        Args:
            snmp_object: SNMP Interact class object from snmp_manager.py

        Returns:
            None

        """
        # Define query object
        self.snmp_object = snmp_object

        # Get one OID entry in MIB (portDuplex)
        test_oid = '.1.3.6.1.4.1.9.5.1.4.1.1.10'

        super().__init__(snmp_object, test_oid, tags=['layer1'])

    def layer1(self):
        """Get layer 1 data from device.

        Args:
            None

        Returns:
            final: Final results

        """
        # Initialize key variables
        final = defaultdict(lambda: defaultdict(dict))

        # Get interface portDuplex data
        values = self.portduplex()
        for key, value in values.items():
            final[key]['portDuplex'] = value

        # Return
        return final

    def portduplex(self):
        """Return dict of CISCO-STACK-MIB portDuplex for each port.

        Args:
            None

        Returns:
            data_dict: Dict of portDuplex using ifIndex as key

        """
        # Initialize key variables
        data_dict = defaultdict(dict)
        dot1dbaseport = self._portifindex()

        # Process OID
        oid = '.1.3.6.1.4.1.9.5.1.4.1.1.10'
        results = self.snmp_object.walk(oid, normalized=True)
        for key, value in results.items():
            # Assign duplex value to ifindex key
            ifindex = dot1dbaseport[int(key)]
            data_dict[ifindex] = value

        # Return the interface descriptions
        return data_dict

    def _portifindex(self):
        """Return dict of CISCO-STACK-MIB portIfIndex for each port.

        Args:
            None

        Returns:
            data_dict: Dict of portIfIndex using dot1dBasePort as key

        """
        # Initialize key variables
        data_dict = defaultdict(dict)

        # Process OID
        oid = '.1.3.6.1.4.1.9.5.1.4.1.1.11'
        results = self.snmp_object.walk(oid, normalized=True)
        for key, value in results.items():
            data_dict[int(key)] = value

        # Return the interface descriptions
        return data_dict
