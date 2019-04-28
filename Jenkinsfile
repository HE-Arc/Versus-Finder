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
        sh 'pytz src/ --exit-zero --output-file pytz-output.txt'
      }
    }
  }
  post {
    always {
      junit 'pytz-output.xml'
    }
    failure {
      echo 'Failed!'
    }
    success {
      echo 'Done!'
    }
  }
}