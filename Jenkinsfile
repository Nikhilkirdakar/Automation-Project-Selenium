pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat "py -3 -m pip install -r requirements.txt"
            }
        }

        stage('Run tests') {
            steps {
                bat "py -3 -m pytest -q --junitxml=Reports/results.xml"
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([
                    reportDir: 'Reports',
                    reportFiles: 'index.html',
                    reportName: 'HTML Report'
                ])
            }
        }
    }

    post {
        always {
            junit 'Reports/results.xml'
            archiveArtifacts artifacts: '**/Reports/**', fingerprint: true
        }
    }
}