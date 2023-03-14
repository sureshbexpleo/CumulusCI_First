#!/usr/bin/env bash
printenv
STATUS_CODE=$(curl -H "Content-Type: multipart/form-data" -u $JIRA_USERNAME:$JIRA_PASSWORD -F "file=@/home/runner/work/CumulusCI_First/CumulusCI_First/output/output.xml" "$JIRA_SERVER_URL/rest/raven/2.0/import/execution/robot?projectKey=${PROJECT_KEY}&testExecKey=${JIRA_EXECUTION_ID}" -o /dev/null -w '%{http_code}\n' -s)
if [[ "$STATUS_CODE" -ne 200 ]] ; then
  echo "Site status changed to $STATUS_CODE"
else
  exit 0
fi