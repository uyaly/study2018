import re

import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    args = parser.parse_args()

    if not args.file:
        print 'Usage: python analyze_log -f <log_file>'
        sys.exit(-1)

    re_fum = re.compile('(?<= )[A-F0-9]{2}')

    with open(args.file, 'r') as f:
        line = f.readline()
        while line:
            if not line.startswith('Report'):
                line = f.readline()
                continue
            # get new line
            try:
                args = line.split(' ')
                type = args[0]
                time = args[1]
                num = args[2]
                extra = args[4]
            except:
                continue

            send_bufs = []
            recv_bufs = []
            send_buf = []
            recv_buf = []
            is_sending = True
            while True:
                line = f.readline()
                values = re_fum.findall(line)
                if not values:
                    if send_buf and recv_buf:
                        send_bufs.append(send_buf)
                        recv_bufs.append(recv_buf)
                    print '''Type: {}\nTime: {}\nNumber: {}\nExtra: {}'''.format(type, time, num, extra)
                    for i in xrange(len(send_bufs)):
                        print 'Send: {}'.format(' '.join(send_bufs[i]))
                        print 'Recv: {}'.format(' '.join(recv_bufs[i]))
                    break
                else:
                    if values[0] == '7E':
                        is_sending = True
                        if send_buf and recv_buf:
                            send_bufs.append(send_buf)
                            recv_bufs.append(recv_buf)
                        send_buf = []
                        recv_buf = []
                    if is_sending:
                        send_buf.extend(values)
                    else:
                        recv_buf.extend(values)
                    if values[-1] == '7E':
                        is_sending = False
