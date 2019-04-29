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
        sh 'sonar-scanner -h'
      }
    }
    stage('QualityTest') { 
            steps {
		    sh '(sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io )'
	    }
    }
  }
}