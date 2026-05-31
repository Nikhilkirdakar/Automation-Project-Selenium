pipeline {
  agent any
  triggers {
    // Run once every morning at ~6:00 (use H for stable hashing)
    cron('H 6 * * *')
  }
  environment {
    PYTHON = 'python3'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install dependencies') {
      steps {
        sh 'python -m pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run tests') {
      steps {
        sh 'pytest -q --headless --browser_name=chrome --junitxml=Reports/results.xml'
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
      echo 'Pipeline completed'
    }
  }
}
