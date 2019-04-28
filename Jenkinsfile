pipeline {
  agent {
    docker { image 'python:3.7.1' }
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
      echo 'Test'
    }
    failure {
      echo 'Failed!'
    }
    success {
      echo 'Done!'
    }
  }
}