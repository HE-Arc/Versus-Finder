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
        sh 'ls -a ./sonar-scanner-3.3.0.1492-linux/bin/'
        sh 'cd ./bin/ '
        sh 'ls -a'
		    sh '(./sonar-scanner  -Dsonar.projectKey=Versusfinder   -Dsonar.organization=skogarmadr-github   -Dsonar.sources=.   -Dsonar.host.url=https://sonarcloud.io )'
	    }
    }
  }
}