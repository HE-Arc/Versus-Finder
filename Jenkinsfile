pipeline {
  agent {
    docker 'python:3.7.3'
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
  }
  post {
    always {
      junit ''
    }
    failure {
      echo 'Failed!'
    }
    success {
      echo 'Done!'
    }
  }
}