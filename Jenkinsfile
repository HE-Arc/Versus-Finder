 pipeline {
  agent {
    docker 'python:3.6.1'
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'flake8 src/ --exit-zero --output-file flake8-output.txt'
        sh 'flake8_junit flake8-output.txt flake8-output.xml'
      }
    }
  }
  post {
    always {
      junit 'flake8-output.xml'
    }
    failure {
      echo 'Failed!'
    }
    success {
      echo 'Done!'
    }
  }
}