self.logger = logging.getLogger()
self.logger.setLevel(logging.INFO)

#create handler,write log
fh = logging.FileHandler(os.path.join(logPath, "outPut.log" ))
#Define the output format of formatter handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

self.logger.addHandler(fh)