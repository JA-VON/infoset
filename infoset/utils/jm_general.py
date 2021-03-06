#!/usr/bin/env python3
"""Nagios check general library."""

import sys
import os
import shutil
import json
import yaml


def logit(error_num, error_string, is_error=True):
    """Log to STDOUT.

    Args:
        error_num: Error number
        error_string: Descriptive error string
        is_error: Is this an error or not?

    Returns:
        None
    """
    # Log the message
    if is_error is True:
        meta_message = ('(%s): %s') % (error_num, error_string)
        log_message = ('ERROR %s') % (meta_message)
        print(log_message)
        sys.exit(3)
    else:
        meta_message = ('(%sS): %s') % (error_num, error_string)
        log_message = ('STATUS %s') % (meta_message)
        print(log_message)


def dict2yaml(data_dict):
    """Convert a dict to a YAML string.

    Args:
        data_dict: Data dict to convert

    Returns:
        yaml_string: YAML output
    """
    # Process data
    json_string = json.dumps(data_dict)
    yaml_string = yaml.dump(yaml.load(json_string), default_flow_style=False)

    # Return
    return yaml_string


def move_files(source_dir, target_dir):
    """Delete files in a directory.

    Args:
        source_dir: Directory where files are currently
        target_dir: Directory where files need to be

    Returns:
        Nothing

    """
    # Make sure source directory exists
    if os.path.exists(source_dir) is False:
        log_message = ('Directory %s does not exist.') % (
            source_dir)
        logit(1011, log_message, True)

    # Make sure target directory exists
    if os.path.exists(target_dir) is False:
        log_message = ('Directory %s does not exist.') % (
            target_dir)
        logit(1012, log_message, True)

    source_files = os.listdir(source_dir)
    for filename in source_files:
        full_path = ('%s/%s') % (source_dir, filename)
        shutil.move(full_path, target_dir)


def delete_files(target_dir):
    """Delete files in a directory.

    Args:
        target_dir: Directory in which files must be deleted

    Returns:
        Nothing

    """
    # Make sure target directory exists
    if os.path.exists(target_dir) is False:
        log_message = ('Directory %s does not exist.') % (
            target_dir)
        logit(1013, log_message, True)

    # Delete all files in the tmp folder
    for the_file in os.listdir(target_dir):
        file_path = os.path.join(target_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as exception_error:
            log_message = ('Error: deleting files in %s. Error: %s') % (
                target_dir, exception_error)
            logit(1014, log_message, True)
        except:
            log_message = ('Unexpected error')
            logit(1015, log_message, True)


def cleanstring(data):
    """Remove multiple whitespaces and linefeeds from string.

    Args:
        data: String to process

    Returns:
        result: Stipped data

    """
    # Initialize key variables
    nolinefeeds = data.replace('\n', ' ').replace('\r', '').strip()
    words = nolinefeeds.split()
    result = ' '.join(words)

    # Return
    return result
