import re
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    # sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv = ['d:\\anaconda3\\Scripts\\scrapy', 'crawl', 'quotes']
    sys.exit(execute())