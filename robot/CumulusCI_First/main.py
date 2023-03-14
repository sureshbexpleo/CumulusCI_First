import requests,os
s = requests.Session()
print(os.environ)
if 'HTTPS_PROXY' in os.environ:
    if os.environ['HTTPS_PROXY'].find("http") == -1:
        s.proxies['https'] = 'http://' + os.environ['HTTPS_PROXY']
    else:
        s.proxies['https'] = os.environ['HTTPS_PROXY']
url="https://devstack.vwgroup.com/jira/rest/raven/2.0/import/execution/robot?projectKey=GFMC&testExecKey=${JIRA_EXECUTION_ID}"
headers={"Authorization": "Basic " + "dWYwZXB2bDpVb1JqclhQbEN1bG43eFRKSUc3NDRmMTdqWU1jZWJ2bFFCUUNDbg==", 'Content-type': 'text/xml'}
with open('/home/runner/work/CumulusCI_First/CumulusCI_First/output/output.xml') as f:
    data = f.read().replace('\n', '').replace('\r', '').encode()
    res = s.post(url, headers=headers, data=data)
    print(res.content)

# res=s.post(url,headers=headers,data=data)
# print(res.reason)