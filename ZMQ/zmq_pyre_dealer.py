#!/usr/bin/env python

"""
usage: pyre_dealer05.py [-h] [-c COUNT] [-m MESSAGE] [-v]

synopsis:
  a simple Pyre dealer/server.  Receives response from clients.

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        number of messages to send. Default: 2
  -m MESSAGE, --message MESSAGE
                        a message body to be sent
  -v, --verbose         Print messages during actions.

examples:
  python dealer05.py
  python dealer05.py --count=4
  python dealer05.py -c 4 --message="a simple message"
"""


from __future__ import print_function
# from six.moves import input
import argparse
import socket
import json
import time
import itertools
import pyre
import gevent
import gevent.monkey
gevent.monkey.patch_socket()


Node_name = socket.gethostname()
Node_value = '{} server'.format(Node_name)
Group_name = 'group1'


def dbg_print(opts, msg, **kwargs):
    """Print a message if verbose is on."""
    if opts.verbose:
        print(msg, **kwargs)


def send_request(node, peer, msg, opts):
    """Send a request."""
    body = {'host': Node_name, 'request': msg}
    bodystr = json.dumps(body)
    dbg_print(opts, 'sending: "{}"'.format(bodystr))
    node.whispers(peer, bodystr)


def receive_response(node, opts):
    """Receive a response."""
    while True:
        data = node.recv()
        if data[0] == b'WHISPER':
            break
    dbg_print(opts, 'received response: {}'.format(data))
    return data


def run(opts):
    node = pyre.Pyre(Node_name)
    node.set_header(Node_name, Node_value)
    node.start()
    while not node.peers():
        print('No peers.  Waiting.')
        time.sleep(2)
    peers = node.peers()
    dbg_print(opts, 'peers: {}'.format(peers))
    dbg_print(opts, 'sending')
    peer_cycler = itertools.cycle(peers)
    send_tasks = []
    for idx in range(opts.count):
        peer = peer_cycler.__next__()
        msg = '{}. {}'.format(idx, opts.message)
        task = gevent.spawn(send_request, node, peer, msg, opts)
        send_tasks.append(task)
    receive_tasks = []
    for idx in range(opts.count):
        task = gevent.spawn(receive_response, node, opts)
        receive_tasks.append(task)
    # gevent.joinall(list(itertools.chain(send_tasks, receive_tasks)))
    dbg_print(opts, 'before join send_tasks')
    gevent.joinall(send_tasks)
    dbg_print(opts, 'after join send_tasks')
    print('-' * 50)
    for task in gevent.iwait(receive_tasks):
        data1 = task.value
        data2 = data1[3]
        data2 = json.loads(data2)
        print('sent: "{}"  received from {}: "{}"'.format(
            data2['request'], data2['sender'], data2['response']))
    print('-' * 50)
    node.stop()


def main():
    description = """\
synopsis:
  a simple Pyre dealer/server.  Receives response from clients.
"""
    epilog = """\
examples:
  python dealer05.py
  python dealer05.py --count=4
  python dealer05.py -c 4 --message="a simple message"
"""
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
#     parser.add_argument(
#         "command",
#         help="A command, one of: getlist, getone, add, update, delete"
#     )
    parser.add_argument(
        "-c", "--count",
        type=int, default=2,
        help="number of messages to send.  Default: 2",
    )
    parser.add_argument(
        "-m", "--message",
        default='default message',
        help="a message body to be sent",
    )
#     parser.add_argument(
#         "-g", "--send-with-gevent",
#         action="store_true",
#         help="Send messages/requests with gevent tasks",
#     )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print messages during actions.",
    )
    options = parser.parse_args()
    run(options)


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    # import ipdb; ipdb.set_trace()
    main()