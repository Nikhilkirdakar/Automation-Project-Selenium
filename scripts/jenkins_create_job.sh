#!/usr/bin/env bash
set -euo pipefail

# Usage:
# export JENKINS_URL="https://jenkins.example.com"
# export JENKINS_USER="admin"
# export JENKINS_TOKEN="<api-token>"
# export JOB_NAME="python-selenium-daily"
# export GIT_REPO="https://github.com/Nikhilkirdakar/Automation-Project-Selenium.git"
# ./scripts/jenkins_create_job.sh

if [ -z "${JENKINS_URL:-}" ] || [ -z "${JENKINS_USER:-}" ] || [ -z "${JENKINS_TOKEN:-}" ] || [ -z "${JOB_NAME:-}" ] || [ -z "${GIT_REPO:-}" ]; then
  echo "Please set JENKINS_URL, JENKINS_USER, JENKINS_TOKEN, JOB_NAME and GIT_REPO environment variables"
  exit 1
fi

# Obtain Jenkins crumb
CRUMB_JSON=$(curl -s --user "$JENKINS_USER:$JENKINS_TOKEN" "$JENKINS_URL/crumbIssuer/api/json")
CRUMB=$(echo "$CRUMB_JSON" | python -c "import sys, json; print(json.load(sys.stdin).get('crumb',''))")

read -r -d '' JOB_XML <<'XML'
<flow-definition plugin="workflow-job@2.46">
  <description>Pipeline for running pytest tests</description>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.92">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.11.3">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>__GIT_REPO__</url>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/main</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
    </scm>
    <scriptPath>Jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers>
    <hudson.triggers.TimerTrigger>
      <spec>H 6 * * *</spec>
    </hudson.triggers.TimerTrigger>
  </triggers>
</flow-definition>
XML

JOB_XML="${JOB_XML//__GIT_REPO__/$GIT_REPO}"

# Create or update the job
curl -s -X POST "$JENKINS_URL/createItem?name=$JOB_NAME" \
  --user "$JENKINS_USER:$JENKINS_TOKEN" \
  -H "Jenkins-Crumb:$CRUMB" \
  -H "Content-Type: application/xml" \
  --data-binary "$JOB_XML"

echo 'Job create/update request sent. Check Jenkins UI or job status.'
