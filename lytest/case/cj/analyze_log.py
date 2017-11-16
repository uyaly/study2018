import csv
import re
import sys
import argparse

# D:\PycharmProjects\test\study\lytest\case\cj>python analyze_log.py  -i 3.log -o xxx.csv

def output_result_console(type, time, status, alarm, send_bufs, recv_bufs):
    if send_buf and recv_buf:
        send_bufs.append(send_buf)
        recv_bufs.append(recv_buf)
    print '''Type: {}\nTime: {}\nStatusber: {}\nAlarm: {}'''.format(type, time, status, alarm)
    for i in xrange(len(send_bufs)):
        print 'Send: {}'.format(' '.join(send_bufs[i]))
        print 'Recv: {}'.format(' '.join(recv_bufs[i]))

def output_result_csv(csvfile, type, time, status, alarm, send_bufs, recv_bufs):
    if not csvfile:
        return
    writter = csv.writer(csvfile)
    writter.writerow((type, time, status, alarm))
    for i in xrange(len(send_bufs)):
        writter.writerow(('Send', ' '.join(send_bufs[i])))
        writter.writerow(('Recv', ' '.join(recv_bufs[i])))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    if not args.input:
        print 'Usage: python analyze_log -i <log_file> [-o <csv_file>]'
        sys.exit(-1)

    re_fum = re.compile('(?<= )[A-F0-9]{2}')

    csvfile = None
    if args.output:
        csvfile = open(args.output, 'wb')

    with open(args.input, 'r') as f:
        line = f.readline()
        while line:
            if not line.startswith('Report')and not line.startswith('Alarm'):
                line = f.readline()
                continue
            # get new line
            try:
                args = line.split(' ')
                type = args[0]
                time = args[1]
                status = args[2]
                alarm = args[4]
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
                    output_result_console(type, time, status, alarm, send_bufs, recv_bufs)
                    output_result_csv(csvfile, type, time, status, alarm, send_bufs, recv_bufs)
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
    if csvfile:
        csvfile.close()
