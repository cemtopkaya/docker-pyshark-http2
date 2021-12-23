#!/usr/bin/python3
import pyshark

# http2-h2c.pcap is a sample PCAP file. 
capture = pyshark.FileCapture('./pcap_files/http2-h2c.pcap')
for packet in capture:
  print(str(packet.layers))
  if 'HTTP2' in str(packet.layers):
     field_names = packet.http2._all_fields
     for field_name in field_names:
        http2_stream_id = {val for key, val in field_names.items() if key == 'http2.streamid'}
        print("".join(http2_stream_id))