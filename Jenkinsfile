#!groovy
pipeline {
  agent any
  triggers { cron('H 6 * * *') }
  environment {
    // Optional envs: SLACK_WEBHOOK, EMAIL_RECIPIENTS
  }
  stages {
    stage('Checkout') { steps { checkout scm } }

    stage('Cross-browser Tests') {
      parallel {
        Chrome: {
          node {
            stage('Install and Run - Chrome') {
              script {
                if (isUnix()) {
                  sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                  sh "python3 -m pytest -q --headless --browser_name=chrome --junitxml=Reports/results-chrome.xml --html=Reports/report-chrome.html --self-contained-html"
                } else {
                  bat 'py -3 -m pip install --upgrade pip && py -3 -m pip install -r requirements.txt'
                  bat 'py -3 -m pytest -q --headless --browser_name=chrome --junitxml=Reports/results-chrome.xml --html=Reports/report-chrome.html --self-contained-html'
                }
              }
            }
          }
        }
        Firefox: {
          node {
            stage('Install and Run - Firefox') {
              script {
                if (isUnix()) {
                  sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                  sh "python3 -m pytest -q --headless --browser_name=firefox --junitxml=Reports/results-firefox.xml --html=Reports/report-firefox.html --self-contained-html"
                } else {
                  bat 'py -3 -m pip install --upgrade pip && py -3 -m pip install -r requirements.txt'
                  bat 'py -3 -m pytest -q --headless --browser_name=firefox --junitxml=Reports/results-firefox.xml --html=Reports/report-firefox.html --self-contained-html'
                }
              }
            }
          }
        }
      }
    }

    stage('Publish HTML Report') {
      steps {
        publishHTML([reportDir: 'Reports', reportFiles: 'report-chrome.html', reportName: 'Automation HTML Report - Chrome', keepAll: true, alwaysLinkToLastBuild: true, allowMissing: true])
        publishHTML([reportDir: 'Reports', reportFiles: 'report-firefox.html', reportName: 'Automation HTML Report - Firefox', keepAll: true, alwaysLinkToLastBuild: true, allowMissing: true])
      }
    }

    stage('Archive artifacts') {
      steps {
        // archive handled in post
        echo 'Archiving will happen in post steps'
      }
    }
  }
  post {
    always {
      // Publish JUnit for both browsers if available
      junit allowEmptyResults: true, testResults: 'Reports/results-*.xml'

      // Archive artifacts
      archiveArtifacts artifacts: 'Reports/**, Screenshots/**', allowEmptyArchive: true

      // Slack notification if SLACK_WEBHOOK is set
      script {
        if (env.SLACK_WEBHOOK) {
          def msg = "Build ${env.JOB_NAME} #${env.BUILD_NUMBER} finished with status ${currentBuild.currentResult}. (<${env.BUILD_URL}|Open>)"
          if (isUnix()) {
            sh "curl -s -X POST -H \"Content-type: application/json\" --data '{\"text\": \"${msg}\"}' \"${env.SLACK_WEBHOOK}\" || true"
          } else {
            bat "powershell -Command \"Invoke-RestMethod -Uri '${env.SLACK_WEBHOOK}' -Method Post -Body (ConvertTo-Json @{text='${msg}'}) -ContentType 'application/json' -UseBasicParsing\""
          }
        }
        // Email if EMAIL_RECIPIENTS is set (requires email-ext plugin)
        if (env.EMAIL_RECIPIENTS) {
          emailext body: "Build ${env.JOB_NAME} #${env.BUILD_NUMBER} finished with status ${currentBuild.currentResult}.", subject: "Jenkins: ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${currentBuild.currentResult}", to: env.EMAIL_RECIPIENTS
        }

        echo 'Pipeline completed'
      }
    }
  }
}
