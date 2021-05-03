import requests

def single_domain_url_fetch_waybackurls(domain, filename):
    r=requests.get(f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey")
    with open(filename, 'w') as file:
        file.writelines("%s\n" % r.text)


def multiple_doamins_url_fetch_waybackurls(filename, output):
    with open(filename, 'r') as file:
        file=file.readlines()
        for url in file:
            r=requests.get(f"https://web.archive.org/cdx/search/cdx?url={url}/*&output=txt&fl=original&collapse=urlkey")
            with open(output, 'a') as file1:
                file1.writelines("%s\n"  % r.text)





