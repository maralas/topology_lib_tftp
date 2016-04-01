# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Maria Alas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_transfer_files communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

# Add your library functions here.


def send_tftp_command(enode, remote_host, c, four=False, six=False,
                      l=False, m=False, r=False, v=False,
                      shell='bash'):
    """
    This function will execute TFTP command in bash.

      -four: -4, Connect with IPv4 only, even if IPv6 support was compiled in.

      -six: -6 Connect with IPv6 only, if compiled in.

      -c: -c command
              Execute  command  as  if it had been entered on the tftp prompt.
              Must be specified last on the command line.

      -l: -l  Default to literal mode. Used to avoid special processing of ':'
              in a file name.

      -m: -m mode
              Set  the  default  transfer  mode to mode.  This is usually used
              with -c.

      -r: -R port:port
              Force the originating port number to be in the  specified  range
              of port numbers.

       -v: -v     Default to verbose mode.
    """
    pass

    # This function will execute TFTP command in bash:
    #
    # command = 'tftp {host_ip} -c get file.txt file.txt
    #

    arguments = locals()

    required_arg = ['remote_host', 'c']

    optional_arg = {'v': '-v', 'four': '-4', 'six': '-6',
                    'l': '-l', 'm': '-m', 'r': '-R', 'v': '-v'}

    options = ''
    command = remote_host

    for key, value in list(arguments.items()):
        if value is True:
            options = '{0}{1} '.format(options, optional_arg.get(key))

    tftp_cmd = 'tftp {0}{1} -c {2}'.format(options, command, c)
    tftp_response = enode(tftp_cmd, shell=shell)
    assert tftp_response is '', 'unexpected response {0}'.format(tftp_response)


__all__ = [
    'send_tftp_command'
]
