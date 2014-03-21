#!/usr/bin/env python
#-*-coding:utf-8-*-

from tornado import ioloop
from tornado import netutil

class EchoServer(netutil.TCPServer):

    def handle_stream(self, stream, address):
        self._stream = stream
        self._read_line()

    def _read_line(self):
        self._stream.read_util('\n', self._handle_read)

    def _handle_read(self, data_in):
        self._stream.write('You sent: %s' %data_in)
        self._read_line()

if __name__ == "__main__":
    server = EchoServer()
    server.listen(2007)
    ioloop.IOLoop.instance().start()