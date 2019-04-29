pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'export PATH=./sonar-scanner-3.3.0.1492-linux/bin:$PATH'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
    stage('QualityTest') { 
            steps {
              sh 'echo test'
	    }
    }
  }
}