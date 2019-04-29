pipeline {
  agent {
    docker { image 'python:3.7.1' }
  }
  stages {
    stage('Install dependencies') {
      steps {
        sh 'echo test'
      }
    }
    stage('Test') {
      steps {
        sh 'python --version'
      }
    }
    stage('QualityTest') { 
            steps {
        sh './sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner -h'
        
	    }
    }
  }
}