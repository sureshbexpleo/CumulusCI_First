#!/usr/bin/env bash
#printenv
#curl -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${{secrets.JIRA_TOKEN}}"  --data @/home/runner/work/CumulusCI_First/CumulusCI_First/output/output.xmlhttps://devstack.vwgroup.com/jira/rest/raven/2.0/import/execution/robot?testExecKey=${JIRA_EXECUTION_ID}
STATUS_CODE=$(curl -LI -H "Content-Type: text/xml" -X POST -H "Authorization: Bearer ${JIRA_TOKEN}"  --data @/home/runner/work/CumulusCI_First/CumulusCI_First/output/output.xml https://devstack.vwgroup.com/jira/rest/raven/2.0/import/execution/robot?testExecKey=$JIRA_EXECUTION_ID -o /dev/null -w '%{http_code}\n' -s)
if [[ "$STATUS_CODE" -ne 200 ]] ; then
  echo "Site status changed to $STATUS_CODE"
else
  exit 0
fi