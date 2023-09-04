import urllib.request as urllib

def main(url):
    print("Checking connectivity")

    response = urllib.urlopen(url)
    print("Connected to", url, "Successfully")
    print("The response code was:", response.getcode())

print("This is a Site Connectivity Checker")
input_url = input("Input the url of the site: ")

main(input_url)


