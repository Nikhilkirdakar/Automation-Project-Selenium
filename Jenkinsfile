pipeline {
  agent any
  triggers {
    // Run once every morning at ~6:00 (use H for stable hashing)
    cron('H 6 * * *')
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install dependencies') {
      steps {
        script {
          if (isUnix()) {
            sh '''python3 -m pip install --upgrade pip
pip install -r requirements.txt'''
          } else {
          bat """py -3 -m pip install --upgrade pip
py -3 -m pip install -r requirements.txt"""
          }
        }
      }
    }
    stage('Run tests') {
      steps {
        script {
          if (isUnix()) {
            sh 'python3 -m pytest -q --headless --browser_name=chrome --junitxml=Reports/results.xml'
          } else {
            bat 'py -3 -m pytest -q --headless --browser_name=chrome --junitxml=Reports/results.xml'
          }
        }
      }
    }
    stage('Publish HTML Report') {
      steps {
        publishHTML([
          reportDir: 'Reports',
          reportFiles: 'report.html',
          reportName: 'Automation HTML Report',
          keepAll: true,
          alwaysLinkToLastBuild: true,
          allowMissing: true
        ])
      }
    }
    stage('Publish results') {
      steps {
        junit 'Reports/results.xml'
        archiveArtifacts artifacts: 'Reports/**, Screenshots/**', allowEmptyArchive: true
      }
    }
  }
  post {
    always {
      junit 'Reports/results.xml'
      archiveArtifacts artifacts: 'Reports/**, Screenshots/**', allowEmptyArchive: true
      echo 'Pipeline completed'
    }
  }
}