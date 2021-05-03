import argparse
import sys
from banner.banner import banner_design
from function import single_domain_url_fetch_waybackurls, multiple_doamins_url_fetch_waybackurls
banner=banner_design()

parser=argparse.ArgumentParser(description=banner,formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--domain', help='domain name for which you wanna fetch urls')
parser.add_argument('-o', '--output', help='output file name store in txt format')
parser.add_argument('-f', '--file', help='filename containing domains for which you wanna fetch urls')
args=parser.parse_args()


if len(sys.argv)==5 and sys.argv[2]==args.domain and sys.argv[4]==args.output:
    single_domain_url_fetch_waybackurls(args.domain, args.output)
elif len(sys.argv)==5 and sys.argv[2]==args.file and sys.argv[4]==args.output:
    multiple_doamins_url_fetch_waybackurls(args.file, args.output)